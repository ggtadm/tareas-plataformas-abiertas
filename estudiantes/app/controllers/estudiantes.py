import json
import re
from flask import Blueprint, jsonify, request

estudiantes_endpoints = Blueprint('estudiantes_endpoints', __name__)

# ==========================================
# Endpoints de la práctica anterior
# ==========================================

@estudiantes_endpoints.route('/hola', methods=['GET'])
def hola():
    return jsonify("hola mundo"), 200

@estudiantes_endpoints.route('/saludo', methods=['GET'])
@estudiantes_endpoints.route('/saludo/<nombre>', methods=['GET'])
@estudiantes_endpoints.route('/saludo/<nombre>/<apellido>', methods=['GET'])
def saludo(nombre=None, apellido=None):
    # 1. Obtener desde JSON body (incluso si falta el header application/json en Postman)
    data = None
    try:
        data = request.get_json(force=True, silent=True)
    except Exception:
        pass

    if not isinstance(data, dict) and request.data:
        try:
            raw_text = request.data.decode('utf-8', errors='ignore').strip()
            if raw_text:
                data = json.loads(raw_text)
        except Exception:
            try:
                raw_text = request.data.decode('utf-8', errors='ignore')
                m_n = re.search(r'["\']?nombre["\']?\s*[:=]\s*["\']([^"\']+)["\']', raw_text, re.IGNORECASE)
                if m_n:
                    nombre = m_n.group(1).strip()
                m_a = re.search(r'["\']?apellido["\']?\s*[:=]\s*["\']([^"\']+)["\']', raw_text, re.IGNORECASE)
                if m_a:
                    apellido = m_a.group(1).strip()
            except Exception:
                pass

    if isinstance(data, dict):
        if not nombre:
            for k, v in data.items():
                if k.lower() in ['nombre', 'nombre_estudiante', 'nombre-estudiante', 'name', 'estudiante']:
                    if v and str(v).strip():
                        nombre = str(v).strip()
                        break
        if not apellido:
            for k, v in data.items():
                if k.lower() in ['apellido', 'apellidos', 'last_name', 'lastname']:
                    if v and str(v).strip():
                        apellido = str(v).strip()
                        break

    # 2. Obtener desde query params (URL ?nombre=...&apellido=...)
    if not nombre:
        for k, v in request.args.items():
            if k.lower() in ['nombre', 'nombre_estudiante', 'nombre-estudiante', 'name', 'estudiante']:
                if v and v.strip():
                    nombre = v.strip()
                    break
    if not apellido:
        for k, v in request.args.items():
            if k.lower() in ['apellido', 'apellidos', 'last_name', 'lastname']:
                if v and v.strip():
                    apellido = v.strip()
                    break

    # 3. Obtener desde form data
    if not nombre and request.form:
        for k, v in request.form.items():
            if k.lower() in ['nombre', 'nombre_estudiante', 'nombre-estudiante', 'name', 'estudiante']:
                if v and v.strip():
                    nombre = v.strip()
                    break
    if not apellido and request.form:
        for k, v in request.form.items():
            if k.lower() in ['apellido', 'apellidos', 'last_name', 'lastname']:
                if v and v.strip():
                    apellido = v.strip()
                    break

    # Validación si no se envía el nombre del estudiante
    if not nombre:
        return jsonify({
            "saludo": "Debe de ingresar el nombre del estudiante."
        }), 200

    # Construir el saludo con nombre y apellido
    nombre_completo = f"{nombre} {apellido}".strip() if apellido else nombre
    return jsonify({
        "saludo": f"Hola {nombre_completo}"
    }), 200


# ==========================================
# Nuevos Endpoints: Métodos HTTP (GET, POST, PUT, DELETE)
# ==========================================

# 1. Obtener todos los estudiantes
# Método: GET /estudiantes
@estudiantes_endpoints.route('/estudiantes', methods=['GET'])
@estudiantes_endpoints.route('/estudiantes/', methods=['GET'])
def get_estudiantes():
    return jsonify({
        "mensaje": "Lista de estudiantes obtenida correctamente.",
        "estudiantes": [
            "Ana",
            "Carlos",
            "María"
        ]
    }), 200


# 2. Agregar un estudiante
# Método: POST /estudiantes
@estudiantes_endpoints.route('/estudiantes', methods=['POST'])
@estudiantes_endpoints.route('/estudiantes/', methods=['POST'])
def add_estudiante():
    data = None
    try:
        data = request.get_json(force=True, silent=True)
    except Exception:
        pass

    if not isinstance(data, dict) and request.data:
        try:
            raw_text = request.data.decode('utf-8', errors='ignore').strip()
            if raw_text:
                data = json.loads(raw_text)
        except Exception:
            try:
                raw_text = request.data.decode('utf-8', errors='ignore')
                m = re.search(r'["\']?nombre["\']?\s*[:=]\s*["\']([^"\']+)["\']', raw_text, re.IGNORECASE)
                if m:
                    data = {'nombre': m.group(1).strip()}
            except Exception:
                pass

    nombre = "Pedro"
    if isinstance(data, dict) and data.get('nombre'):
        nombre = str(data['nombre']).strip()

    return jsonify({
        "mensaje": "Estudiante agregado correctamente.",
        "estudiante": nombre
    }), 200


# 3. Actualizar un estudiante
# Método: PUT /estudiantes/<id>
@estudiantes_endpoints.route('/estudiantes/<id>', methods=['PUT'])
def update_estudiante(id):
    try:
        id_val = int(id)
    except (ValueError, TypeError):
        id_val = id

    return jsonify({
        "mensaje": "Estudiante actualizado correctamente.",
        "id": id_val
    }), 200


# 4. Eliminar un estudiante
# Método: DELETE /estudiantes/<id>
@estudiantes_endpoints.route('/estudiantes/<id>', methods=['DELETE'])
def delete_estudiante(id):
    try:
        id_val = int(id)
    except (ValueError, TypeError):
        id_val = id

    return jsonify({
        "mensaje": "Estudiante eliminado correctamente.",
        "id": id_val
    }), 200
