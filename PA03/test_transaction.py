import unittest
import sqlite3
from transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_setUp(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        self.assertEqual(transaction.db_name, db_name)
        self.assertIsInstance(transaction.conn, sqlite3.Connection)
        self.assertIsInstance(transaction.cursor, sqlite3.Cursor)
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [])
        self.cursor.execute('SELECT * FROM categories')
        self.assertEqual(self.cursor.fetchall(), [])

    def test_show_categories(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        self.cursor.execute('INSERT INTO categories (category) VALUES (?)', ('Groceries',))
        self.cursor.execute('INSERT INTO categories (category) VALUES (?)', ('Gas',))
        self.cursor.execute('INSERT INTO categories (category) VALUES (?)', ('Rent',))
        self.conn.commit()
        self.assertEqual(transaction.show_categories(), ['Groceries', 'Gas', 'Rent'])

    def test_add_category(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_category('Groceries')
        self.cursor.execute('SELECT * FROM categories')
        self.assertEqual(self.cursor.fetchall(), [('Groceries',)])
        transaction.add_category('Gas')
        self.cursor.execute('SELECT * FROM categories')
        self.assertEqual(self.cursor.fetchall(), [('Groceries',), ('Gas',)])
        transaction.add_category('Rent')
        self.cursor.execute('SELECT * FROM categories')
        self.assertEqual(self.cursor.fetchall(), [('Groceries',), ('Gas',), ('Rent',)])

    def test_modify_category(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_category('Groceries')
        transaction.add_category('Gas')
        transaction.add_category('Rent')
        transaction.modify_category('Groceries', 'Food')
        self.cursor.execute('SELECT * FROM categories')
        self.assertEqual(self.cursor.fetchall(), [('Food',), ('Gas',), ('Rent',)])
        transaction.modify_category('Gas', 'Car')
        self.cursor.execute('SELECT * FROM categories')
        self.assertEqual(self.cursor.fetchall(), [('Food',), ('Car',), ('Rent',)])
        transaction.modify_category('Rent', 'Housing')
        self.cursor.execute('SELECT * FROM categories')
        self.assertEqual(self.cursor.fetchall(), [('Food',), ('Car',), ('Housing',)])

    def test_show_transactions(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        self.assertEqual(transaction.show_transactions(), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])

    def test_add_transaction(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries')])
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas')])
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        transaction.add_transaction(4, '2020-01-04', 'Groceries', 50, 'Groceries')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent'), (4, '2020-01-04', 'Groceries', 50.0, 'Groceries')])
    
    def test_modify_transaction(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        transaction.modify_transaction(1, '2020-01-01', 'Groceries', 50, 'Groceries')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 50.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        transaction.modify_transaction(2, '2020-01-02', 'Gas', 25, 'Gas')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 50.0, 'Groceries'), (2, '2020-01-02', 'Gas', 25.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        transaction.modify_transaction(3, '2020-01-03', 'Rent', 500, 'Rent')
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(1, '2020-01-01', 'Groceries', 50.0, 'Groceries'), (2, '2020-01-02', 'Gas', 25.0, 'Gas'), (3, '2020-01-03', 'Rent', 500.0, 'Rent')])

    def test_delete_transaction(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        transaction.delete_transaction(1)
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        transaction.delete_transaction(2)
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [(3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        transaction.delete_transaction(3)
        self.cursor.execute('SELECT * FROM transactions')
        self.assertEqual(self.cursor.fetchall(), [])

    def test_summarize_by_date(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        self.assertEqual(transaction.summarize_by_date('2020-01-01'), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries')])
        self.assertEqual(transaction.summarize_by_date('2020-01-02'), [(2, '2020-01-02', 'Gas', 50.0, 'Gas')])
        self.assertEqual(transaction.summarize_by_date('2020-01-03'), [(3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        self.assertEqual(transaction.summarize_by_date('2020-01-04'), [])

    def test_summarize_by_month(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        transaction.add_transaction(4, '2020-02-01', 'Groceries', 50, 'Groceries')
        transaction.add_transaction(5, '2020-02-02', 'Gas', 25, 'Gas')
        transaction.add_transaction(6, '2020-02-03', 'Rent', 500, 'Rent')
        self.assertEqual(transaction.summarize_by_month('2020-01'), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        self.assertEqual(transaction.summarize_by_month('2020-02'), [(4, '2020-02-01', 'Groceries', 50.0, 'Groceries'), (5, '2020-02-02', 'Gas', 25.0, 'Gas'), (6, '2020-02-03', 'Rent', 500.0, 'Rent')])
        self.assertEqual(transaction.summarize_by_month('2020-03'), [])

    def test_summarize_by_year(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        transaction.add_transaction(4, '2021-01-01', 'Groceries', 50, 'Groceries')
        transaction.add_transaction(5, '2021-01-02', 'Gas', 25, 'Gas')
        transaction.add_transaction(6, '2021-01-03', 'Rent', 500, 'Rent')
        self.assertEqual(transaction.summarize_by_year('2020'), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (2, '2020-01-02', 'Gas', 50.0, 'Gas'), (3, '2020-01-03', 'Rent', 1000.0, 'Rent')])
        self.assertEqual(transaction.summarize_by_year('2021'), [(4, '2021-01-01', 'Groceries', 50.0, 'Groceries'), (5, '2021-01-02', 'Gas', 25.0, 'Gas'), (6, '2021-01-03', 'Rent', 500.0, 'Rent')])
        self.assertEqual(transaction.summarize_by_year('2022'), [])

    def test_summarize_by_category(self):
        db_name = 'test_tracker.db'
        transaction = Transaction(db_name)
        transaction.add_transaction(1, '2020-01-01', 'Groceries', 100, 'Groceries')
        transaction.add_transaction(2, '2020-01-02', 'Gas', 50, 'Gas')
        transaction.add_transaction(3, '2020-01-03', 'Rent', 1000, 'Rent')
        transaction.add_transaction(4, '2021-01-01', 'Groceries', 50, 'Groceries')
        transaction.add_transaction(5, '2021-01-02', 'Gas', 25, 'Gas')
        transaction.add_transaction(6, '2021-01-03', 'Rent', 500, 'Rent')
        self.assertEqual(transaction.summarize_by_category('Groceries'), [(1, '2020-01-01', 'Groceries', 100.0, 'Groceries'), (4, '2021-01-01', 'Groceries', 50.0, 'Groceries')])
        self.assertEqual(transaction.summarize_by_category('Gas'), [(2, '2020-01-02', 'Gas', 50.0, 'Gas'), (5, '2021-01-02', 'Gas', 25.0, 'Gas')])
        self.assertEqual(transaction.summarize_by_category('Rent'), [(3, '2020-01-03', 'Rent', 1000.0, 'Rent'), (6, '2021-01-03', 'Rent', 500.0, 'Rent')])
        self.assertEqual(transaction.summarize_by_category('Car'), [])
    