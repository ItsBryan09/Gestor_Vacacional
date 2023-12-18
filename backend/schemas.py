from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import date


# Todo el schema de empleado
class EmpleadoCreate(BaseModel):
    num_nomina: int
    nombre: str
    email: str
    jefe_directo: int
    departamento: str
    fecha_ingreso: date
    is_active: bool
    sucursal: str
    password: str
    rol_user: str


# actualizar password
class UpdatePassword(BaseModel):
    new_password: str


# Lee al empleado por separado
class LeerEmpleados(BaseModel):
    num_nomina: int
    nombre: str
    email: str
    jefe_directo: int
    departamento: str
    fecha_ingreso: date
    is_active: bool
    sucursal: str
    rol_user: str


# Editar empleado
class EmpleadoEdit(BaseModel):
    nombre: str
    email: str
    jefe_directo: int
    departamento: str
    fecha_ingreso: date
    is_active: bool
    sucursal: str
    rol_user: str


class vista_solicitud(BaseModel):

    num_nomina: int
    nombre: str
    jefe_directo: int
    departamento: str
    fecha_solicitud: date
    fecha_inicio: date
    fecha_fin: date
    dias_solicitados: int
    dias_restantes: int
    fecha_reincorporacion: date
    status: str


class SolicitudCreate(BaseModel):
    # id: int
    num_nomina: int
    fecha_solicitud: date
    fecha_inicio: date
    fecha_fin: date
    dias_solicitados: int
    fecha_reincorporacion: date
    dias_restantes: int
    nombre: str
    email: str
    fecha_ingreso: date
    dias_vacaciones: int
    status: str


# Restar dias vacaciones
class dias_vacaciones(BaseModel):
    dias_solicitados: int
    dias_restantes: int
    status: str


class View_Vacaciones_Schema(BaseModel):
    num_nomina: int
    nombre: str
    fecha_ingreso: date
    anios_servicio: int
    dias_vacaciones: int
    dias_restantes_vacaciones: int


class View_Solicitudes(BaseModel):

    num_nomina: int
    nombre: str
    jefe_directo: int
    departamento: str
    fecha_solicitud: date
    fecha_inicio: date
    fecha_fin: date
    dias_solicitados: int
    fecha_reincorporacion: date
    dias_restantes: int


# Lee las solicitudes por un numero de nomina
class Mis_solicitudes(BaseModel):
    id: int
    num_nomina: int
    fecha_solicitud: date
    fecha_inicio: date
    fecha_fin: date
    dias_solicitados: int
    fecha_reincorporacion: date
    dias_restantes: int
    nombre: str
    email: str
    fecha_ingreso: date
    dias_vacaciones: int
    status: str

# /////////////////////////////////////////


class Token:
    def __init__(self, access_token: str, token_type: str):
        self.access_token = access_token
        self.token_type = token_type