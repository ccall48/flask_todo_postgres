from flask import Flask
from models.todo import db
from routes.urls import todos
from routes.paginate_test import pagetest


app = Flask(__name__)
app.register_blueprint(todos)
app.register_blueprint(pagetest)

app.config['SECRET_KEY'] = 'N9ZH7S9QVB435IyFPxwD0yKwxX5pMNbNojH69dmK7w5hPyQ8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@flask_todo_db:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ------------------------------------------------------------------------------
# APP COMMANDS
# ------------------------------------------------------------------------------
@app.cli.command('initdb')
def initdb():
    db.drop_all()
    db.create_all()
    print('Dropped database and recreated.')


@app.cli.command('createdb')
def createdb():
    db.create_all()
    print('todo database created.')


db.app = app
db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
