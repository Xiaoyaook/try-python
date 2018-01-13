from datetime import datetime

from flask import Flask, render_template, redirect, request, abort
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# 连接数据库
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine(app)

#
class Todo(db.Document):
    meta = {
        'collection': 'todo',
        'ordering': ['-create_at'],
        'strict': False,
    }

    task = db.StringField()
    create_at = db.DateTimeField(default=datetime.now)
    is_completed = db.BooleanField(default=False)

    def to_dict(self):
        return {
            'id': str(self.id),
            'task': self.task,
            'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            'is_completed': self.is_completed
        }


@app.route('/', methods=['GET'])
def index():

    todos = Todo.objects().all()   # 查询所有数据

    return render_template('index.html', todos=todos)


@app.route('/', methods=['POST'])
def add_todo():
    content = request.form.get('content', None)
    if not content:
        abort(400)
    todo = Todo(task=content, is_completed=False)

    # 使用 save() 方法添加数据
    todo.save()

    return redirect('/')


@app.route('/list/<taskname>')
def detail(taskname):

    todo = Todo.objects.get_or_404(task=taskname)

    return render_template('project.html', todo=todo)

if __name__ == '__main__':
    app.run()
