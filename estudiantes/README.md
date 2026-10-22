# Práctica 2 - API de estudiantes - Alumno: Greivin Gonzalez Trejos

## Descripción
API en Python con Flask, curso de Plataformas Abiertas, practica 2 

## Endpoints
- GET `/estudiantes/api/v1/hola`: muestra `"hola mundo"`.
- GET `/estudiantes/api/v1/saludo`: recibe en el Body (JSON) o por Query Params `nombre` y `apellido`. Muestra `{"saludo": "Hola NOMBRE APELLIDO"}`.
- GET `/estudiantes/api/v1/saludo` (sin nombre): muestra `{"saludo": "Debe de ingresar el nombre del estudiante."}`.

