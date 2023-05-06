Session Transcript/README File

Introduction
I will be demonstrating the features I implemented in the Expense Tracker app. I have implemented the following features:

0. Quit
1. Adding a category
2. Modifying a category
3. Showing all the categories
4. Adding a transaction
5. Deleting a transaction
6. Showing all the transactions
7. Summarizing transactions by date
8. Summarizing transactions by month
9. Summarizing transactions by year
10. Summarizing transactions by category
11. Print this menu

Running pylint
I will begin by running pylint to check my code's adherence to guidelines. I run the following command in my terminal:

pylint transaction.py

The output of the pylint command shows that there are no major issues with the code.

Running pytest
Next, I will run pytest to test the Transaction class methods. I run the following command in my terminal:

pytest test_transaction.py

The output of the pytest command shows that all the tests have passed successfully.

Running tracker.py
Finally, I will run the tracker.py file and demonstrate all the implemented features. I run the following command in my terminal:

python tracker.py
The app displays the following menu:

Welcome to the Expense Tracker!
Please select an option from the menu below:
0. Quit
1. Show Categories
2. Add Category
3. Modify Category
4. Show Transactions
5. Add Transactions
6. Delete Transaction
7. Summarize Transactions by Date
8. Summarize Transactions by Month
9. Summarize Transactions by Year
10. Summarize Transactions by Category
11. Print This Menu

Adding a category
I choose choice 2 to include a category. I must enter the category name when using the app. I type "Groceries" and hit the enter key. The program displays a success message after adding the category to the database.

Modifying a category
I choose option 3 in order to change a category. I am prompted by the software to enter the old category name and the new category name. I press enter after typing "Groceries" and "Food" separately. The application updates the database's category and displays a success message.

Showing all the categories
I choose option 1 to see every category. The program displays all of the categories after retrieving them from the database.

Adding a transaction
To include a transaction, I choose option 5. I must enter the item number, quantity, category, date, and description when using the app. I type the necessary data and press Enter. The application displays a success message after adding the transaction to the database.

Deleting a transaction
To remove a transaction, I choose option 6. I must input the item number of the transaction to remove on the app's popup. I press enter after entering the transaction's item number from my earlier addition. The application displays a success message after removing the transaction from the database.

Showing all the transactions
I choose option 4 to display every transaction. The program displays all of the transactions it has retrieved from the database.

Summarizing transactions by date
I choose option 7 to list transactions chronologically. The program pulls every transaction out of the database, groups them by date, and shows how much money was spent on each date.

Summarizing transactions by month
To list transactions by month, I choose option 8. The software pulls every transaction out of the database, sorts them by month, and shows the total amount spent in each.

Summarizing transactions by year
I decide to use option 9 to list transactions by year. The application pulls every transaction out of the database, sorts them by year, and displays the total amount spent in each transaction.