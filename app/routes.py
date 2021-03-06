from app import app, api
# from flask import request
from flask_restful import Resource, abort, reqparse


# @app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
# @app.route('/index', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def index():
#     if request.method == 'GET':
#         return 'Read'
#     elif request.method == 'POST':
#         return 'Write'
#     elif request.method == 'PUT':
#         return 'Insert'
#     elif request.method == 'DELETE':
#         return 'Delete'
#     else:
#         return 'Hello, World!'

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '??????'},
    'todo3': {'task': 'profit!'}
}


def abort_if_todo_doesnot_exists(todo_id):
    if todo_id not in TODOS:
        abort(404, message='Todo {} doesn`t exist'.format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnot_exists(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnot_exists(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')