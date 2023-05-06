import sqlite3
from transaction import Transaction

def main():
    db_name = 'tracker.db'
    transaction = Transaction(db_name)
    print('Welcome to the Expense Tracker!')
    print('Please select an option from the menu below:')
    print_menu()
    run(transaction)

def run(transaction):
    while True:
        choice = input('Enter your choice: ')
        if choice == '0':
            print('Goodbye!')
            break

        elif choice == '1': # Show Categories
            transaction.show_categories()

        elif choice == '2': # Add Category
            category_to_add = input('Enter the category to add: ')
            transaction.add_category(category_to_add)

        elif choice == '3': # Modify Category
            category_to_modify = input('Enter the category to modify: ')
            new_category = input('Enter the new category: ')
            transaction.modify_category(category_to_modify, new_category)

        elif choice == '4': # Show Transactions
            transaction.show_transactions()
            
        elif choice == '5': # Add Transaction
            item_number = int(input('Enter the item number: '))
            amount = float(input('Enter the amount: '))
            category = input('Enter the category: ')
            date = input('Enter the date (YYYY-MM-DD): ')
            description = input('Enter the description: ')
            transaction.add_transaction(item_number, date, category, amount, description)            

        elif choice == '6': # Delete Transaction
            transaction_to_delete = int(input('Enter the item number of the transaction to delete: '))
            transaction.delete_transaction(transaction_to_delete)
            

        elif choice == '7': # Summarize Transaction by Date
            transaction.summarize_by_date()
            
        elif choice == '8': # Summarize Transactions by Month
            transaction.summarize_by_month()          

        elif choice == '9': # Summarize Transactions by Year
            transaction.summarize_by_year()
            

        elif choice == '10': # Summarize Transactions by Category
            transaction.summarize_by_category()

        elif choice == '11': # Print This Menu
            print_menu()

        else:
            print('Invalid choice. Please try again.')
            print_menu()

def print_menu():
    print('Welcome to the Expense Tracker!')
    print('Please select an option from the menu below:')
    print('0. Quit')
    print('1. Show Categories')
    print('2. Add Category')
    print('3. Modify Category')
    print('4. Show Transactions')
    print('5. Add Transactions')
    print('6. Delete Transaction')
    print('7. Summarize Transactions by Date')
    print('8. Summarize Transactions by Month')
    print('9. Summarize Transactions by Year')
    print('10. Summarize Transactions by Category')
    print('11. Print This Menu')
    
if __name__ == '__main__':
    main()