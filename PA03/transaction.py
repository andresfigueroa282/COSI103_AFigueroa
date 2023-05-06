import sqlite3
import datetime
import os

class Transaction:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            item_number INTEGER,
                            date DATE,
                            category TEXT,
                            amount REAL,
                            description TEXT
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                            category TEXT
                            )''')

        self.conn.commit()
    
    def show_categories(self):
        self.cursor.execute('SELECT DISTINCT category FROM transactions')
        categories = self.cursor.fetchall()
        print()
        print("Categories:")
        for idx, category in enumerate(categories):
            print(f'{idx + 1}. {category[0]}')
    
    def add_category(self, category):
        self.cursor.execute('INSERT INTO categories (category) VALUES (?)', (category,))
        self.conn.commit()
    
    def modify_category(self, category, new_category):
        self.cursor.execute('UPDATE transactions SET category = ? WHERE category = ?', (new_category, category))
        self.cursor.execute('UPDATE categories SET category = ? WHERE category = ?', (new_category, category))
        self.conn.commit()
    
    def show_transactions(self):
        self.cursor.execute('SELECT * FROM transactions')
        transactions = self.cursor.fetchall()
        print()
        print("Transactions:")
        for transaction in transactions:
            print(f'{transaction[0]}: {transaction[2]} {transaction[3]} {transaction[4]}')
    
    def add_transaction(self, item_number, date, category, amount, description):
        self.cursor.execute('INSERT INTO transactions (item_number, date, category, amount, description) VALUES (?, ?, ?, ?, ?)', (item_number, date, category, amount, description))
        self.cursor.execute('INSERT INTO categories (category) VALUES (?)', (category,))
        self.conn.commit()

    def modify_transaction(self, item_number):
        self.cursor.execute('SELECT * FROM transactions WHERE item_number = ?', (item_number,))
        transaction = self.cursor.fetchone()
        print(f'1. Date: {transaction[2]}')
        print(f'2. Category: {transaction[3]}')
        print(f'3. Amount: {transaction[4]}')
        print(f'4. Description: {transaction[5]}')
        choice = input('Enter the number of the field to modify: ')
        if choice == '1':
            new_date = input('Enter the new date: ')
            self.cursor.execute('UPDATE transactions SET date = ? WHERE item_number = ?', (new_date, item_number))
            self.conn.commit()
        elif choice == '2':
            new_category = input('Enter the new category: ')
            self.cursor.execute('UPDATE transactions SET category = ? WHERE item_number = ?', (new_category, item_number))
            self.conn.commit()
        elif choice == '3':
            new_amount = input('Enter the new amount: ')
            self.cursor.execute('UPDATE transactions SET amount = ? WHERE item_number = ?', (new_amount, item_number))
            self.conn.commit()
        elif choice == '4':
            new_description = input('Enter the new description: ')
            self.cursor.execute('UPDATE transactions SET description = ? WHERE item_number = ?', (new_description, item_number))
            self.conn.commit()
        else:
            print('Invalid choice. Please try again.')
    
    def delete_transaction(self, item_number):
        self.cursor.execute('DELETE FROM transactions WHERE item_number = ?', (item_number,))
        self.conn.commit()

    def summarize_by_date(self):
        self.cursor.execute('SELECT date, SUM(amount) FROM transactions GROUP BY date')
        transactions = self.cursor.fetchall()
        for transaction in transactions:
            print(f'{transaction[0]}: {transaction[1]}')

    def summarize_by_month(self):
        self.cursor.execute('SELECT strftime("%m", date), SUM(amount) FROM transactions GROUP BY strftime("%m", date)')
        transactions = self.cursor.fetchall()
        for transaction in transactions:
            print(f'{transaction[0]}: {transaction[1]}')

    def summarize_by_year(self):
        self.cursor.execute('SELECT strftime("%Y", date), SUM(amount) FROM transactions GROUP BY strftime("%Y", date)')
        transactions = self.cursor.fetchall()
        for transaction in transactions:
            print(f'{transaction[0]}: {transaction[1]}')
    
    def summarize_by_category(self):
        self.cursor.execute('SELECT category, SUM(amount) FROM transactions GROUP BY category')
        transactions = self.cursor.fetchall()
        for transaction in transactions:
            print(f'{transaction[0]}: {transaction[1]}')
    