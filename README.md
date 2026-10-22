# tareas-plataformas-abiertas
Práctica 2 - API estudiantes

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

### 2. Instalar dependencias (ya configuradas en el entorno virtual)
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

## Endpoints disponibles
- **GET** `http://127.0.0.1:5000/estudiantes/api/v1/hola`: devuelve `"hola mundo"`.
- **GET** `http://127.0.0.1:5000/estudiantes/api/v1/saludo`: con Body JSON `{"nombre": "Leonardo", "apellido": "Da vinci"}`, devuelve `{"saludo": "Hola Leonardo Da vinci"}`.
- **GET** `http://127.0.0.1:5000/estudiantes/api/v1/saludo`: sin nombre, devuelve `{"saludo": "Debe de ingresar el nombre del estudiante."}`.
