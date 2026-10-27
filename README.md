# tareas-plataformas-abiertas
API de Estudiantes - Plataformas Abiertas

## Requisitos previos
- Python 3.9 o superior

## Instalación y ejecución en Windows

### 1. Activar el entorno virtual
En PowerShell o CMD, desde la raíz del proyecto:
```powershell
# En PowerShell:
.\venv\Scripts\Activate.ps1

# En CMD (Símbolo del sistema):
.\venv\Scripts\activate.bat
```
> *Nota para PowerShell*: Si aparece un error de permisos de ejecución de scripts, puedes habilitarlo con:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación
Desde la raíz del proyecto:
```bash
python estudiantes/run.py
```
O ingresando a la carpeta `estudiantes`:
```bash
cd estudiantes
python run.py
```

El servidor iniciará en `http://127.0.0.1:5000`.

---

## Endpoints de la práctica: Métodos HTTP (GET, POST, PUT, DELETE)

### 1. Obtener todos los estudiantes
* **Método:** `GET`
* **URL:** `http://127.0.0.1:5000/estudiantes`
* **Respuesta:**
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
* **URL:** `http://127.0.0.1:5000/estudiantes`
* **Body (JSON):**
```json
{
    "nombre": "Pedro"
}
```
* **Respuesta:**
```json
{
    "mensaje": "Estudiante agregado correctamente.",
    "estudiante": "Pedro"
}
```

### 3. Actualizar un estudiante
* **Método:** `PUT`
* **URL:** `http://127.0.0.1:5000/estudiantes/1`
* **Body (JSON):**
```json
{
    "nombre": "Pedro Ramírez"
}
```
* **Respuesta:**
```json
{
    "mensaje": "Estudiante actualizado correctamente.",
    "id": 1
}
```

### 4. Eliminar un estudiante
* **Método:** `DELETE`
* **URL:** `http://127.0.0.1:5000/estudiantes/1`
* **Respuesta:**
```json
{
    "mensaje": "Estudiante eliminado correctamente.",
    "id": 1
}
```

---

## Endpoints de la práctica anterior
- **GET** `http://127.0.0.1:5000/estudiantes/api/v1/hola`: devuelve `"hola mundo"`.
- **GET** `http://127.0.0.1:5000/estudiantes/api/v1/saludo`: con Body JSON `{"nombre": "Leonardo", "apellido": "Da vinci"}`, devuelve `{"saludo": "Hola Leonardo Da vinci"}`.
- **GET** `http://127.0.0.1:5000/estudiantes/api/v1/saludo`: sin nombre, devuelve `{"saludo": "Debe de ingresar el nombre del estudiante."}`.
