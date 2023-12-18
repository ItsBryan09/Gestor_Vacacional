SELECT * FROM vista_antiguedad

SELECT
    num_nomina,
    nombre,
    fecha_ingreso,
    CURRENT_DATE AS fecha_hoy,
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, fecha_ingreso)) AS anios_antiguedad
FROM
    empleados;
	
------------------------------------------------------------------------------
SELECT * FROM vista_vacaciones




/*SELECT e.num_nomina,
    e.nombre,
    e.fecha_ingreso,
    antiguedad.anios_servicio,
        CASE
            WHEN antiguedad.anios_servicio < 1::double precision THEN 0
            WHEN antiguedad.anios_servicio <= 35::double precision THEN cv.dias_vacaciones
            ELSE 32
        END AS dias_vacaciones,
    COALESCE(cv.dias_vacaciones, 0) - COALESCE(s.dias_solicitados, 0::bigint) AS dias_restantes_vacaciones
   FROM empleados e
     JOIN ( SELECT e_1.num_nomina,
            date_part('year'::text, age(CURRENT_DATE::timestamp with time zone, e_1.fecha_ingreso::timestamp with time zone)) AS anios_servicio
           FROM empleados e_1) antiguedad ON e.num_nomina = antiguedad.num_nomina
     LEFT JOIN config_vacaciones cv ON antiguedad.anios_servicio = cv.anios_servicio::double precision OR cv.anios_servicio IS NULL
     LEFT JOIN ( SELECT solicitud.num_nomina,
            sum(
                CASE
                    WHEN solicitud.estatus::text = 'aceptado'::text AND EXTRACT(year FROM solicitud.fecha_solicitud) = EXTRACT(year FROM CURRENT_DATE) THEN solicitud.dias_solicitados
                    ELSE 0
                END) AS dias_solicitados
           FROM solicitud
          GROUP BY solicitud.num_nomina) s ON e.num_nomina = s.num_nomina
  ORDER BY antiguedad.anios_servicio;*/
---------------------------------------------------------------------------------------
vista_solicitud

SELECT
    s.num_nomina AS numero_de_nomina,
    e.nombre AS nombre_del_empleado,
	e.jefe_directo,
	e.departamento,
    s.fecha_solicitud,
	s.fecha_inicio,
    s.fecha_fin,
	s.fecha_reincorporacion,
    s.dias_solicitados,
	s.dias_restantes
FROM
    solicitudes s
JOIN
    empleados e ON s.num_nomina = e.num_nomina;

----------------------------------------------------------------------------------------
vista historial 

SELECT solicitud.id, solicitud.num_nomina, empleados.nombre, solicitud.fecha_solicitud, solicitud.fecha_inicio, solicitud.fecha_fin, solicitud.dias_solicitados, solicitud.fecha_reincorporacion
FROM solicitud
JOIN empleados ON solicitud.num_nomina = empleados.num_nomina
WHERE solicitud.num_nomina = 1331;

---------------------------------------------------------------------------------------------------

 
				
				
				