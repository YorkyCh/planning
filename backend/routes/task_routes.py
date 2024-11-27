from flask import Blueprint, jsonify, request
from models.task import create_task, get_all_tasks, delete_task
from models.project import get_project_by_id

task_bp = Blueprint('task_bp', __name__)
    
# INFO create
@task_bp.route('/api/tasks', methods=["POST"])
def add_task():
    data = request.get_json()
    project_id = data.get("project_id")
    description = data.get("description")
    name = data.get("name")

    if not get_project_by_id(project_id):
        return jsonify({"message": "Project does not exist"})

    if project_id and description and name:
        create_task(project_id, description, name)
        return jsonify({"message": "Task created successfully"}), 201
    else:
        return jsonify({"message": "Project_id and description are required"}), 400 
    
# INFO get all tasks based on project id
@task_bp.route('/api/tasks/project/<int:project_id>', methods=["GET"])
def get_tasks_by_project(project_id):
    tasks = get_all_tasks(project_id)
    return jsonify({"tasks": tasks})

@task_bp.route('/api/tasks/<int:task_id>', methods=["DELETE"])
def remove_task(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted successfully"}), 200