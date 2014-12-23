import rivr
import rivr_peewee
import peewee


database = rivr_peewee.Database(peewee.SqliteDatabase('example.sqlite'))

class Task(database.Model):
    text = peewee.CharField()

    def __str__(self):
        return self.text

@database
def view(request):
    def render(accumulator, task):
        return accumulator + '<li>{}</li>'.format(task)

    text = '<ul>' + reduce(render, Task.select(), '') + '</ul>'
    return rivr.Response(text)


if __name__ == '__main__':
    try:
        Task.create_table()
        Task.create(text='My first task')
        Task.create(text='Another task')
    except:
        # Database is already created
        pass

    rivr.serve(view)

