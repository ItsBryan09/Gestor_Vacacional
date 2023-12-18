from typing import Optional
from sqlalchemy.orm import Session
from fastapi import FastAPI
from jose import JWTError, jwt
from datetime import datetime, timedelta
from schemas import OAuth2PasswordRequestForm
from crud import create_employee, EmpleadoCreate, verify_token
from database import SessionLocal, engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Depends, HTTPException, status
from crud import restar_dias, read_empleado, get_solicitudes_por_nomina, edit_empleado, get_employee_data
from crud import delete_empleado, get_vacation_by_employee_id, get_all_empleados, get_all_solicitudes
from schemas import EmpleadoCreate, Mis_solicitudes, dias_vacaciones, View_Solicitudes, EmpleadoEdit, LeerEmpleados, SolicitudCreate, View_Vacaciones_Schema
from fastapi.security import OAuth2PasswordBearer
from models import Empleado, Base, Solicitudes
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext


Base.metadata.create_all(bind=engine)


app = FastAPI()


# Configura el middleware CORS
origins = [
    "http://localhost",
    "http://192.168.105.93:8080",
    "http://localhost:8080",
    "http://127.0.0.1:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

# Configuración de SQLAlchemy
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Configuración de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Configuración de seguridad
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ///////////////////////TODAS LAS FUNCIONES POST\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# añádir una nueva solicitud
@app.post("/add_solicitud/")
async def crear_solicitud(solicitud: SolicitudCreate):
    db = SessionLocal()
    try:
        nueva_solicitud = Solicitudes(**solicitud.dict())

        db.add(nueva_solicitud)
        db.commit()
        db.refresh(nueva_solicitud)

        return {"mensaje": "Solicitud creada exitosamente", "id_solicitud": nueva_solicitud.id}

    except Exception as e:
        db.rollback()
        print(f"Error interno del servidor: {str(e)}")
        raise HTTPException(
            status_code=500, detail="Error interno del servidor. Consulta los registros del servidor para obtener más detalles.")

    finally:
        db.close()


# Ruta cuando se añade un nuevo empleado
@app.post("/add_empleado/")
async def create_employee_route(employee_input: EmpleadoCreate, db: SessionLocal = Depends(get_db)):
    created_employee = create_employee(db, employee_input)
    return {"message": "Empleado creado", "empleado": created_employee}


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub: str = payload.get("sub")
        if sub is None:
            raise credentials_exception
        token_data = {"sub": sub}
    except JWTError:
        raise credentials_exception
    return token_data


# Funciones de utilidad para el token
def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Ruta para obtener el token
@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: SessionLocal = Depends(get_db)
):
    user = db.query(Empleado).filter(
        Empleado.email == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    expires_delta = timedelta(minutes=30)
    expires_at = datetime.utcnow() + expires_delta

    to_encode = {"sub": form_data.username, "exp": expires_at}
    access_token = create_access_token(to_encode)

    return {"access_token": access_token, "token_type": "bearer"}


# //////////////////////////////////TODAS LAS FUNCIONES DELETE\\\\\\\\\\\\\\\\\\\\\\\


# Eliminar un empleado por su numero de nomina
@app.delete("/delete_empleados/{num_nomina}")
def delete_employee(num_nomina: int, db: Session = Depends(get_db)):
    return delete_empleado(num_nomina, db)


# //////////////////////////////////TODAS LAS FUNCIONES PUT\\\\\\\\\\\\\\\\\\\\\\\\\


# Restar dias vacaciones cuando el administrador acepte una solicitud
@app.put("/restar_dias/{id}", response_model=dias_vacaciones)
async def editar_dias_restates(id: int, dias_data: dias_vacaciones, db: Session = Depends(get_db)):
    return restar_dias(id, dias_data, db)


# Editar a un empleado por su numero de nomina
@app.put("/edit_empleado/{num_nomina}", response_model=EmpleadoEdit)
def update_employee(num_nomina: int, empleado_data: EmpleadoEdit, db: Session = Depends(get_db)):
    return edit_empleado(num_nomina, empleado_data, db)


# Ruta protegida cuando el usuario quiere cambiar su contraseña
@app.put("/edit_password")
async def change_password(
    new_password: str,
    current_user: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    hashed_password = pwd_context.hash(new_password)

    db.query(Empleado).filter(Empleado.email == current_user["sub"]).update(
        {"password": hashed_password})
    db.commit()
    return {"message": "Password updated successfully"}


# ///////////////////////////TODAS LAS FUNCIONES GET\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Buscar un empleado por su numero de nomina
@app.get("/search_empleado/{num_nomina}", response_model=LeerEmpleados)
def read_employee(num_nomina: int, db: Session = Depends(get_db)):
    empleado_data = read_empleado(num_nomina, db)
    if not empleado_data:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado_data


# Buscar todos los empleados
@app.get("/get_all_empleados")
def get_all_employees(db: Session = Depends(get_db)):
    empleados = get_all_empleados(db)
    return empleados


# Consultar la vista a las vacaciones por numero de nomina
@app.get("/view_vacaciones/{num_nomina}", response_model=View_Vacaciones_Schema)
def query_vacaciones(num_nomina: int, db: Session = Depends(get_db)):
    return get_vacation_by_employee_id(num_nomina, db)


# Ruta protegida cuando se incia session
@app.get("/protected")
async def protected_route(email: str = Depends(verify_token), db: Session = Depends(get_db)):
    return get_employee_data(email, db)


# Ruta protegida que requiere autenticación
@app.get("/Session_Activa")
def protected_route(email: str = Depends(get_current_user)):
    return {"message": "Esta es una ruta protegida"}


# Busca todas las solicitudes
@app.get("/get_all_solicitudes")
def get_todas_solicitudes(db: Session = Depends(get_db)):
    empleados = get_all_solicitudes(db)
    return empleados


# Ruta para obtener todas las solicitudes por número de nómina
@app.get("/solicitudes/{num_nomina}", response_model=list[Mis_solicitudes])
def read_solicitudes(num_nomina: int):
    db = SessionLocal()
    solicitudes = get_solicitudes_por_nomina(num_nomina, db)
    if not solicitudes:
        raise HTTPException(
            status_code=404, detail="No se encontraron solicitudes para ese número de nómina")

    # Convertir instancias de SQLAlchemy a diccionarios
    solicitudes_dict = [s.__dict__ for s in solicitudes]

    # Eliminar la clave '_sa_instance_state' que no es necesaria
    for s in solicitudes_dict:
        s.pop('_sa_instance_state', None)

    return solicitudes_dict

@app.get("/protected_route")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"You have access to this route."}