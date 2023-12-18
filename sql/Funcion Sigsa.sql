SELECT actualizar_vista_empleados();

CREATE OR REPLACE FUNCTION actualizar_vista_vacaciones()
RETURNS VOID AS $$
BEGIN
    -- Lógica de actualización aquí
    UPDATE vista_vacaciones
    SET 
        anios_servicios = date_part('year', age(CURRENT_DATE, fecha_ingreso)),
        dias_vacaciones = CASE
                            WHEN date_part('year', age(CURRENT_DATE, fecha_ingreso)) < 1 THEN 0
                            WHEN date_part('year', age(CURRENT_DATE, fecha_ingreso)) <= 35 THEN cv.dias_vacaciones
                            ELSE 32
                          END,
        dias_restantes_vacaciones = COALESCE(cv.dias_vacaciones, 0) - COALESCE(s.dias_solicitados, 0)
    FROM config_vacaciones cv
    LEFT JOIN (
        SELECT num_nomina, 
               sum(CASE WHEN status = 'aceptado' AND EXTRACT(year FROM fecha_solicitud) = EXTRACT(year FROM CURRENT_DATE) THEN dias_solicitados ELSE 0 END) AS dias_solicitados
        FROM solicitudes
        GROUP BY num_nomina
    ) s ON vista_vacaciones.num_nomina = s.num_nomina
    WHERE date_part('year', age(CURRENT_DATE, vista_vacaciones.fecha_ingreso)) = cv.anios_servicio::double precision OR cv.anios_servicio IS NULL;
END;
$$ LANGUAGE plpgsql;
