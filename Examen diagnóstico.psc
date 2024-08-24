Funcion prom <- Calificacion_final (calificaciones_)
	Definir prom Como Real
	Definir calificacion_ Como Entero
	prom = 0
	Para Cada calificacion_ De calificaciones_
		prom = prom + calificacion_
	FinPara
	prom = prom / 3
	Escribir prom
Fin Funcion



Algoritmo Examen_diagnostico
	Definir numero_alumnos, i, j Como Entero
	Definir calificaciones_aprobadas, calificaciones Como Entero
	Definir nombre_alumnos Como Caracter
	Definir calificacion, mayor_calificacion, menor_calificacion Como Real
	Definir nombre_alumno Como Cadena
	Definir promedio, promedio_alumnos Como Real
	
	Escribir Sin Saltar "Ingrese el número de alumnos que desea promediar: "
	Leer numero_alumnos
	
	Dimension nombre_alumnos[numero_alumnos]
	Dimension promedio_alumnos[numero_alumnos]
	Dimension calificaciones_aprobadas[numero_alumnos]
	Dimension calificaciones[3]
	
	Para i Desde 0 Hasta numero_alumnos - 1 Hacer
		
		Escribir Sin Saltar "Nombre del estudiante: "
		Leer nombre_alumno
		Escribir "Las calificaciones deben de ser en el formato (0 - 100)"
		
		Para j Desde 0 Hasta 2 Hacer
			Escribir Sin Saltar "Calificación ", j, " de ", nombre_alumno, ": "
			Leer calificacion
			calificaciones[j] <- calificacion
		Fin Para
		
		promedio_alumnos[i] = Calificacion_final(calificaciones)
		Escribir promedio_alumnos[i]
		nombre_alumnos[i] = nombre_alumno
	Fin Para
	
	Escribir "REPROBADOS:"
	
	menor_calificacion = promedio_alumnos[0]
	Para i Desde 0 Hasta numero_alumnos - 1 Con Paso 1 Hacer
		Si promedio_alumnos[i] < 70 Entonces
			Escribir "---> El alumno ", nombre_alumnos[i], " está reprobado..."
		Sino
			Si menor_calificacion > promedio_alumnos[i] Y menor_calificacion >= 70 Entonces
				menor_calificacion = promedio_alumnos[i]
			FinSi
		Fin Si
	Fin Para
	
	Escribir "Mejor y menor calificación:"
	
	mayor_calificacion = promedio_alumnos[0]
	Para i Desde 0 Hasta numero_alumnos - 1 Con Paso 1 Hacer
		Si mayor_calificacion < promedio_alumnos[i] Entonces
			mayor_calificacion = promedio_alumnos[i]
		Fin Si
	Fin Para
	
	Para i Desde 0 Hasta numero_alumnos - 1 Con Paso 1 Hacer
		Si mayor_calificacion == promedio_alumnos[i] Entonces
			Escribir "----- ", nombre_alumnos[i], " tuvo la mejor calificación: ", mayor_calificacion
		Fin Si
		
		Si menor_calificacion == promedio_alumnos[i] Entonces
			Escribir "----- ", nombre_alumnos[i], " tuvo la menor calificación: ", menor_calificacion
		Fin Si
	Fin Para
	
FinAlgoritmo
