from flask import Blueprint, render_template, url_for, redirect, request
from models.todo import db, Todos


todos = Blueprint('urls', __name__)


@todos.get('/')
@todos.get('/home')
def index():
    tasks = Todos.query.count()
    return render_template('home.html', title='Todos', tasks=tasks)


@todos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        todo = request.form['todo']
        db.session.add(Todos(task=todo))
        db.session.commit()
        return redirect(url_for('urls.tasks'))
    return render_template('task.html', title='Create Task')


@todos.get('/tasks')
def tasks():
    tasks = Todos.query.all()
    return render_template('todos.html', title='All Tasks', tasks=tasks)


@todos.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todos.query.get(id)
    if request.method == 'POST':
        task.task = request.form['task']
        db.session.commit()
        return redirect(url_for('urls.tasks'))
    return render_template('update.html', title='Update Task', task=task)


@todos.get('/delete/<int:id>')
def delete(id):
    db.session.delete(Todos.query.get(id))
    db.session.commit()
    return redirect(url_for('urls.tasks'))
