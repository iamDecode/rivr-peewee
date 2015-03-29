rivr-peewee
===========

[![Build Status](http://img.shields.io/travis/rivrproject/rivr-peewee/master.svg?style=flat)](https://travis-ci.org/rivrproject/rivr-peewee)

rivr integration for the peewee database ORM.

## Installation

```bash
$ pip install rivr-peewee
```

## Usage

```python
from rivr_peewee import Database
```

### Creating a database

You can create a database with the `DATABASE_URL` environment variable using the following:

```python
database = Database()
```

Or you can provide a specific environmental variable to use, and/or a default database URL:

```python
database = Database(env='DATABASE_URL',
                    default='sqlite:///Users/kylef/database.sqlite')
```

You can also explicitly create a database and use it as follows:

```python
database = Database(peewee.SqliteDatabase(':memory:'))
```

### Building your models

The database object has a Model property to use as a base class for your models:

```python
class User(database.Model):
    pass
```

### Middleware

The database object itself is a rivr middleware which handles connecting and disconnecting to the database.

You can wrap a specific view in this:

```python
app = database(router)
```

Or via a decorator:

```python
@database
def view(request):
    return Response('Hello World')
```

#### Middleware Controller

You can also use rivr’s middleware controller:

```python
from rivr.middleware import MiddlewareController

app = MiddlewareController.wrap(router,
    database,
    ExampleMiddleware(),
)
```

## License

rivr-peewee is released under the BSD license. See [LICENSE](LICENSE).
