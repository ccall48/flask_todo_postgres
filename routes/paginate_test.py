from flask import Blueprint
from flask.templating import render_template
from models.todo import Todos


pagetest = Blueprint('test', __name__)
NUM_PAGES = 10


@pagetest.route('/views')
@pagetest.route('/views/<int:page>')
def views(page=1):
    if page is None:
        page = 1

    tasks = Todos.query.order_by(
            Todos.id.desc()
            ).paginate(page=page, per_page=NUM_PAGES, error_out=False, max_per_page=NUM_PAGES)

    return render_template(
        'paginate_test.html',
        tasks=tasks,
        title='views paginated'
    )
