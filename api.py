from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}


class Index(Resource):
    def __init__(self):
        pass

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(Index, '/')
api.add_resource(TodoSimple, '/api/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
