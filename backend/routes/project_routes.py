from flask import Blueprint, jsonify, request
from models.project import create_project, get_all_projects, get_project_by_id, del_project_by_id

project_bp = Blueprint('project_bp', __name__)

@project_bp.route('/api/projects', methods=['GET'])
def get_data():
    projects = get_all_projects()
    return jsonify({"projects": projects})

@project_bp.route('/api/projects', methods=['POST'])
def add_project_route():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    if name and description:
        create_project(name, description)
        return jsonify({"message": "Project added successfully"}), 201
    else:
        return jsonify({"message": "Name and description are required"}), 400

@project_bp.route('/api/projects/<int:id>', methods=['GET'])
def get_project_route(id):
    project = get_project_by_id(id)
    if project:
        return jsonify({"project": project}), 200
    else:
        return jsonify({"message": "Project not found"}), 404

@project_bp.route('/api/projects/<int:id>', methods=["DELETE"])
def remove_project_route(id):
    deleted_project = del_project_by_id(id)
    if deleted_project:
        return jsonify({"message": "Project deleted successfully!"}), 200
    else:
        return jsonify({"message": "Project not found"}), 404