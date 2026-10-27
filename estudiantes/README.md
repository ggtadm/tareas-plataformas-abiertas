# API de Estudiantes - Alumno: Greivin Gonzalez Trejos

## Descripción
API en Python con Flask para el curso de Plataformas Abiertas. Contiene endpoints para conocer el funcionamiento de los métodos HTTP más utilizados (GET, POST, PUT y DELETE).

---

## Endpoints - Práctica: Métodos HTTP (GET, POST, PUT, DELETE)

### 1. Obtener todos los estudiantes
* **Método:** `GET`
* **Ruta:** `/estudiantes` (o `/estudiantes/api/v1/estudiantes`)
* **Respuesta (200 OK):**
```json
{
    "mensaje": "Lista de estudiantes obtenida correctamente.",
    "estudiantes": [
        "Ana",
        "Carlos",
        "María"
    ]
}
```

### 2. Agregar un estudiante
* **Método:** `POST`
* **Ruta:** `/estudiantes` (o `/estudiantes/api/v1/estudiantes`)
* **Body (raw JSON):**
```json
{
    "nombre": "Pedro"
}
```
* **Respuesta (200 OK):**
```json
{
    "mensaje": "Estudiante agregado correctamente.",
    "estudiante": "Pedro"
}
```

### 3. Actualizar un estudiante
* **Método:** `PUT`
* **Ruta:** `/estudiantes/1` (o `/estudiantes/api/v1/estudiantes/1`)
* **Body (raw JSON):**
```json
{
    "nombre": "Pedro Ramírez"
}
```
* **Respuesta (200 OK):**
```json
{
    "mensaje": "Estudiante actualizado correctamente.",
    "id": 1
}
```

### 4. Eliminar un estudiante
* **Método:** `DELETE`
* **Ruta:** `/estudiantes/1` (o `/estudiantes/api/v1/estudiantes/1`)
* **Respuesta (200 OK):**
```json
{
    "mensaje": "Estudiante eliminado correctamente.",
    "id": 1
}
```

---

## Endpoints anteriores (Práctica 2)
- **GET** `/estudiantes/api/v1/hola`: devuelve `"hola mundo"`.
- **GET** `/estudiantes/api/v1/saludo`: recibe `nombre` y `apellido`. Devuelve `{"saludo": "Hola NOMBRE APELLIDO"}`.
- **GET** `/estudiantes/api/v1/saludo` (sin nombre): devuelve `{"saludo": "Debe de ingresar el nombre del estudiante."}`.
