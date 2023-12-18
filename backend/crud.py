from typing import Optional
from jose import JWTError, jwt
from datetime import timedelta
from models import Empleado
from fastapi import Depends
from fastapi import HTTPException, status
from passlib.context import CryptContext
from datetime import datetime
from sqlalchemy.orm import Session
from models import Vista_solicitud, Solicitudes, Vista_Vacaciones
from schemas import EmpleadoCreate, SolicitudCreate, EmpleadoEdit, View_Vacaciones_Schema, dias_vacaciones, LeerEmpleados
from database import SessionLocal, engine
from datetime import datetime, date
from fastapi.security import OAuth2PasswordBearer
from typing import Dict
# Configuración para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración de seguridad
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


# ////////////////////////////////FUNCIONES ADD\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Funcion para creaer un nuevo empleado
def create_employee(db: Session, employee_input: EmpleadoCreate):
    hashed_password = pwd_context.hash(employee_input.password)

    create_empleado = Empleado(
        num_nomina=employee_input.num_nomina,
        nombre=employee_input.nombre,
        email=employee_input.email,
        jefe_directo=employee_input.jefe_directo,
        departamento=employee_input.departamento,
        fecha_ingreso=employee_input.fecha_ingreso,
        is_active=employee_input.is_active,
        sucursal=employee_input.sucursal,
        password=hashed_password,
        rol_user=employee_input.rol_user,
    )

    db.add(create_empleado)
    db.commit()
    db.refresh(create_empleado)

    return create_empleado

# ////////////////////////////////FUNCIONES UPDATE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Restar dias vacaciones cuando el Administrador acepte una solicitud
def restar_dias(id: int, dias_data: dias_vacaciones, db: Session):
    dias = db.query(Solicitudes).filter(
        Solicitudes.id == id).first()
    if dias is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrado")

    for key, value in dias_data.dict().items():
        setattr(dias, key, value)

    db.commit()
    db.refresh(dias)

    return {"dias_solicitados": dias.dias_solicitados, "dias_restantes": dias.dias_restantes, "status": dias.status}


# Editar un empleado por su numero de nomina
def edit_empleado(num_nomina: int, empleado_data: EmpleadoEdit, db: Session):
    empleado = db.query(Empleado).filter(
        Empleado.num_nomina == num_nomina).first()

    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    fecha_ingreso = empleado_data.fecha_ingreso
    today = date.today()

    if fecha_ingreso >= today:
        raise HTTPException(
            status_code=400,
            detail="La fecha de ingreso debe ser una fecha pasada al día de hoy"
        )

    allowed_fields = ["nombre", "email", "jefe_directo", "departamento",
                      "fecha_ingreso", "is_active", "sucursal", "rol_user"]

    for field in allowed_fields:
        if hasattr(empleado_data, field):
            setattr(empleado, field, getattr(empleado_data, field))

    db.commit()
    db.refresh(empleado)

    empleado_dict = empleado.__dict__
    empleado_dict.pop("_sa_instance_state", None)

    return empleado_dict


# ////////////////////////////////FUNCIONES DELETE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Eliminar un empleado por su numero de nomina
def delete_empleado(num_nomina: str, db: Session):
    db_empleado = db.query(Empleado).filter(
        Empleado.num_nomina == num_nomina).first()

    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    db.delete(db_empleado)
    db.commit()
    return {"message": "Empleado eliminado exitosamente"}


# ////////////////////////////////FUNCIONES SEARCH\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Buscar un empleado de la ruta protegia por su email
def get_employee_data(email: str, db: Session) -> dict:
    empleado = db.query(Empleado).filter(Empleado.email == email).first()

    if empleado:
        return {
            "num_nomina": empleado.num_nomina,
            "nombre": empleado.nombre,
            "email": empleado.email,
            "jefe_directo": empleado.jefe_directo,
            "departamento": empleado.departamento,
            "fecha_ingreso": empleado.fecha_ingreso,
            "is_active": empleado.is_active,
            "sucursal": empleado.sucursal,
            "rol_user": empleado.rol_user,
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )


# Función para obtener todas las solicitudes por número de nómina
def get_solicitudes_por_nomina(num_nomina: int, db):
    return db.query(Solicitudes).filter(Solicitudes.num_nomina == num_nomina).all()


# Función para leer un empleado por número de nómina
def read_empleado(num_nomina: int, db: Session):
    empleado = db.query(Empleado).filter(
        Empleado.num_nomina == num_nomina).first()

    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    nombre_jefe_directo = None
    if empleado.jefe_directo is not None:
        jefe_directo = db.query(Empleado).filter(
            Empleado.num_nomina == empleado.jefe_directo).first()
        if jefe_directo:
            nombre_jefe_directo = jefe_directo.nombre

    empleado_data = LeerEmpleados(
        num_nomina=empleado.num_nomina,
        nombre=empleado.nombre,
        jefe_directo=empleado.jefe_directo,
        email=empleado.email,
        departamento=empleado.departamento,
        fecha_ingreso=empleado.fecha_ingreso,
        is_active=empleado.is_active,
        sucursal=empleado.sucursal,
        rol_user=empleado.rol_user
    )

    return empleado_data


# Funcion para buscar todos los empleados
def get_all_empleados(db: Session):
    empleados = db.query(Empleado).all()
    return empleados


# Funcion que busca la vista_vacaciones
def get_vacation_by_employee_id(num_nomina: int, db: Session, limit: int = 1):
    vacations = db.query(Vista_Vacaciones).filter(
        Vista_Vacaciones.num_nomina == num_nomina).limit(limit).first()

    if vacations is None:
        raise HTTPException(
            status_code=404, detail="Vacaciones no encontradas para el empleado")
    vacations_data = View_Vacaciones_Schema(
        num_nomina=vacations.num_nomina,
        nombre=vacations.nombre,
        fecha_ingreso=vacations.fecha_ingreso,
        anios_servicio=vacations.anios_servicio,
        dias_vacaciones=vacations.dias_vacaciones,
        dias_restantes_vacaciones=vacations.dias_restantes_vacaciones
    )

    return vacations_data


# Funcion para buscar todos las solicitudes
def get_all_solicitudes(db: Session):
    solicitudes = db.query(Solicitudes).all()
    return solicitudes


# Función que busca la vista_solicitud por numero de nomina
def get_solicitud_id(num_nomina: int, db: Session):
    solicitudes = db.query(Vista_solicitud).filter(
        Vista_solicitud.num_nomina == num_nomina).order_by(Vista_solicitud.fecha_solicitud.desc()).all()

    if not solicitudes:
        raise HTTPException(
            status_code=404, detail="Vista no encontrada para el empleado")

    solicitud = solicitudes[-1]

    return solicitud

# ////////////////////////////////FUNCIONES EXTRAS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Verifica si hay Token activo
def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return email