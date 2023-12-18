from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from database import Base
from sqlalchemy.orm import relationship

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Empleado(Base):
    __tablename__ = "empleados"

    num_nomina = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, index=True)
    jefe_directo = Column(Integer, ForeignKey('empleados.num_nomina'))
    nombre_jefe_directo = relationship('Empleado', remote_side=[num_nomina])
    departamento = Column(String, index=True)
    fecha_ingreso = Column(Date, index=True)
    is_active = Column(Boolean, default=True)
    sucursal = Column(String, index=True)
    password = Column(String, index=True)
    rol_user = Column(String, index=True)


class Vista_solicitud(Base):
    __tablename__ = "vista_solicitud"

    num_nomina = Column(Integer, primary_key=True)
    nombre = Column(String)
    jefe_directo = Column(Integer)
    departamento = Column(String)
    fecha_solicitud = Column(Date)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    dias_solicitados = Column(Integer)
    dias_restantes = Column(Integer)
    fecha_reincorporacion = Column(Date)


class Config_vacaciones(Base):
    __tablename__ = "config_vacaciones"

    anios_servicio = Column(Integer, primary_key=True)
    dias_vacaciones = Column(Integer)


class Solicitudes(Base):
    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True)
    num_nomina = Column(Integer, ForeignKey("empleados.num_nomina"))
    fecha_solicitud = Column(Date, index=True)
    fecha_inicio = Column(Date, index=True)
    fecha_fin = Column(Date, index=True)
    dias_solicitados = Column(Integer, index=True)
    fecha_reincorporacion = Column(Date, index=True)
    dias_restantes = Column(Integer, index=True)
    nombre = Column(String, index=True)
    email = Column(String, index=True)
    fecha_ingreso = Column(Date, index=True)
    dias_vacaciones = Column(Integer, index=True)
    status = Column(String, index=True)


class Vista_Vacaciones(Base):
    __tablename__ = "vista_vacaciones"

    # id = Column(Integer)
    num_nomina = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha_ingreso = Column(Date)
    anios_servicio = Column(Integer)
    dias_vacaciones = Column(Integer)
    dias_restantes_vacaciones = Column(Integer)