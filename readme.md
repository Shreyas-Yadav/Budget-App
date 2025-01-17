# Budget App

A Python-based budgeting application designed to help users track and manage their personal finances. The app provides an intuitive command-line interface where users can create budget categories, track expenses, and visualize spending patterns through automatically generated charts.

## Features

- Create multiple budget categories
- Add deposits to categories
- Make withdrawals from categories
- Transfer funds between categories
- Check the balance of each category
- Generate a spend chart to visualize spending

## Class: Category

### Attributes:

- `category`: The name of the category.
- `amount`: The current balance of the category.
- `ledger`: A list to store all transactions (deposits and withdrawals).

### Methods:

- `__str__()`: Returns a string representation of the category ledger.
- `deposit(amount, description='')`: Adds a deposit to the ledger.
- `withdraw(amount, description='')`: Adds a withdrawal to the ledger if there are sufficient funds.
- `get_balance()`: Returns the current balance of the category.
- `transfer(amount, other_category)`: Transfers an amount to another category if there are sufficient funds.
- `check_funds(amount)`: Checks if there are sufficient funds for a withdrawal or transfer.

## Function: create_spend_chart(categories)

Creates a bar chart representing the percentage of spending for each category.

### Parameters:

- `categories`: A list of Category objects.

### Returns:

- A string representation of the spend chart.

## Usage

1. Run the `main.py` script.
2. Follow the on-screen prompts to add new categories, select categories, and perform transactions.
3. View the spend chart by calling the `create_spend_chart(categories)` function.

### Example

```python
food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')

food.deposit(1000, 'deposit')
food.withdraw(100, 'groceries')
food.withdraw(15, 'restaurant and more food for dessert')
food.transfer(50, clothing)

clothing.deposit(200)
clothing.withdraw(25, 't-shirts')

auto.deposit(500)
auto.withdraw(80, 'bike washer')

categories = [food, clothing, auto]
print(create_spend_chart(categories))
```

## Running the Script

1. Run the `main.py` script.
2. You will be presented with the following options:
   - Add new category
   - Select category
   - Exit

### Menu Options

- **Add new category**: Allows you to create a new budget category.
- **Select category**: Allows you to select an existing category and perform transactions (Deposit, Withdraw, Check Balance, Transfer Balance).
- **Exit**: Exits the application.

### Example Interaction

```plaintext
Select operation:
1. Add new category
2. Select category
3. Exit
Enter valid option: 2

0 : Food
1 : Clothing
2 : Auto
-1 : None
Enter index of category: 0

0: Deposit
1: Withdraw
2: Check Balance
3: Transfer Balance
Enter valid transaction: 1
```
