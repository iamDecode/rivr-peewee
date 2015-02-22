from rivr import serve, Router
from rivr.middleware import MiddlewareController
from rivr_peewee import Database
from rivr_peewee.views import ListView, DetailView
from rivr_jinja import JinjaMiddleware
from jinja2 import Environment, DictLoader
import peewee


## Models:

database = Database(peewee.SqliteDatabase('example.sqlite'))

class Task(database.Model):
    text = peewee.CharField()

    def __str__(self):
        return self.text


## Views

class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


## Templates

TASK_LIST_TEMPLATE = """
<h1>Tasks</h1>

<ul>
  {% for task in task_list %}
    <li><a href="/tasks/{{ task.id }}">{{ task }}</a></li>
  {% endfor %}
</ul>
"""

TASK_DETAIL_TEMPLATE = """
<a href="/">View all tasks</a>

<h1>Task</h1>
<p>{{ task }}</p>
"""


if __name__ == '__main__':
    try:
        Task.create_table()
        Task.create(text='My first task')
        Task.create(text='Another task')
    except:
        # Database is already created
        pass

    loader = DictLoader({
        'task_list.html': TASK_LIST_TEMPLATE,
        'task_detail.html': TASK_DETAIL_TEMPLATE,
    })
    environment = Environment(loader=loader)

    router = Router(
        (r'^$', TaskListView.as_view()),
        (r'^tasks/(?P<pk>[\d]+)$', TaskDetailView.as_view()),
    )

    view = MiddlewareController.wrap(router,
        database,
        JinjaMiddleware(environment)
    )

    serve(view)

