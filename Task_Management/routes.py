# routes.py

from flask import Blueprint, jsonify, request
from models import task_store

api = Blueprint('api', __name__)

from flask import request, jsonify

@api.route('/v1/tasks', methods=['POST'])
def add_tasks():
    data = request.json

   
    if 'title' in data:
        task = task_store.add_task(data['title'])
        return jsonify({"id": task.id}), 201

   
    elif 'tasks' in data and isinstance(data['tasks'], list):
        new_tasks = task_store.bulk_add_tasks(data['tasks'])
        return jsonify({"tasks": [task.to_dict() for task in new_tasks]}), 201

    else:
     
        return "Invalid input format", 400


@api.route('/v1/tasks', methods=['GET'])
def list_tasks():
    return jsonify({"tasks": task_store.get_all_tasks()}), 200

@api.route('/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_store.get_task(task_id)
    if not task:
        return jsonify({"error": "There is no task at that id"}), 404
    return jsonify(task.to_dict()), 200

@api.route('/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_store.delete_task(task_id)
    return '', 204




@api.route('/v1/tasks', methods=['DELETE'])
def bulk_delete_tasks():
    data = request.json
    if not data or 'tasks' not in data or not isinstance(data['tasks'], list):
       
        return "Invalid input format", 400

   
    task_ids = [task['id'] for task in data['tasks'] if 'id' in task]

   
    if not task_ids:
        
        return "No valid task IDs provided", 400

  
    task_store.bulk_delete_tasks(task_ids)

    
    return '', 204


@api.route('/v1/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = task_store.get_task(task_id)
    if not task:
        return jsonify({"error": "There is no task at that id"}), 404
    data = request.json
    task_store.update_task(task_id, data.get('title'), data.get('is_completed'))
    return '', 204


