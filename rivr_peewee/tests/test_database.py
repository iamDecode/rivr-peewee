import os
import unittest
from peewee import SqliteDatabase, Model
from rivr_peewee import Database


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = SqliteDatabase(':memory:')

    def test_raises_when_database_not_configured(self):
        with self.assertRaises(Exception):
            Database()

    def test_uses_given_database(self):
        database = Database(database=self.db)
        self.assertEqual(database.database, self.db)

    def test_uses_env_for_database(self):
        os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
        database = Database()

        self.assertEqual(database.database.database, ':memory:')
        del os.environ['DATABASE_URL']

    #

    def test_database_model(self):
        database = Database(database=self.db)
        self.assertEqual(database.Model._meta.database, self.db)

