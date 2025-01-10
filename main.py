
class Category:
    
    """
    A class to represent a budget category.
    Attributes:
    -----------
    category : str
        The name of the category.
    amount : float
        The current balance of the category.
    ledger : list
        A list to store all transactions (deposits and withdrawals).
    Methods:
    --------
    __str__():
        Returns a string representation of the category ledger.

    deposit(amount, description=''):
        Adds a deposit to the ledger.

    withdraw(amount, description=''):
        Adds a withdrawal to the ledger if there are sufficient funds.

    get_balance():
        Returns the current balance of the category.

    transfer(amount, other_category):
        Transfers an amount to another category if there are sufficient funds.

    check_funds(amount):
        Checks if there are sufficient funds for a withdrawal or transfer.
        Returns a string representation of the category ledger. 
    """
        
    

    def __init__(self,category):
        self.category = category
        self.amount = 0
        self.ledger = []

        
    def __str__(self):
        result = ''

        category_length = len(self.category)
        stars = '*' * ((30 - category_length)//2)
        result += stars + self.category + stars
        result = result[0:30]
        
        for item in self.ledger:
            desc = item['description'][0:23];
            amount = "%.2f" % item['amount']    # display 2 decimal places
            spaces = ' '*(30-(len(desc)+len(amount)))
            result += f'\n{desc}{spaces}{amount}'
            
        result += f'\nTotal: {self.get_balance()}'
        return result
        
    
    """
        Adds a deposit to the ledger.
        Parameters:
        -----------
        amount : float
            The amount to be deposited.
        description : str, optional
            The description of the deposit (default is an empty string).
    """
    def deposit(self,amount,description=''):
        self.amount += amount
        self.ledger.append({'amount':amount,'description':description})


    """
        Adds a withdrawal to the ledger if there are sufficient funds.
        Parameters:
        -----------
        amount : float
            The amount to be withdrawn.
        description : str, optional
            The description of the withdrawal (default is an empty string).
        Returns:
        --------
        bool
            True if the withdrawal was successful, False otherwise.
    """
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({'amount':-amount,'description':description})
            return True
        else:
            return False

    def get_balance(self):
        return self.amount  


    """
        Transfers an amount to another category if there are sufficient funds.
        Parameters:
        -----------
        amount : float
            The amount to be transferred.
        other_category : Category
            The category to which the amount will be transferred.
        Returns:
        --------
        bool
            True if the transfer was successful, False otherwise.
    """
    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {other_category.category}')
            other_category.deposit(amount,f'Transfer from {self.category}')
            return True
        return False


    """
        Checks if there are sufficient funds for a withdrawal or transfer.
        Parameters:
        -----------
        amount : float
            The amount to be checked.
        Returns:
        --------
        bool
            True if there are sufficient funds, False otherwise.
    """
    def check_funds(self,amount):
        if self.amount >= amount:
            return True
        return False
    


"""
    Creates a bar chart representing the percentage of spending for each category.
    categories : list
        A list of Category objects.
    return:
    -----------
    str
        A string representation of the spend chart.
"""
def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    
    total_spending = 0
    spendings = []
    for item in categories:
        category_spendings = 0
        for entry in item.ledger:
            if entry['amount'] < 0:
                category_spendings += abs(entry['amount'])
        total_spending += category_spendings
        spendings.append([category_spendings,item.category])


    percentages = [[round(((item[0]/total_spending)*100), 1), item[1]] for item in spendings]
    

    cols = len(percentages)*3+1
    rows = 12
    x_axis = [int(_) for _ in range(100,-10,-10)]
    for row in x_axis:
        line = ''
        if row != 100:
            line += ' '
        if row == 0:
            line += ' '
        line += f'{row}| '
        for entry in percentages:
            if entry[0] >= row:
                line += 'o  '
            else:
                line += '   '
        chart += line + '\n'

    tab = '    '
    y_axis = tab+'-'*cols
    chart += y_axis

    max_len = max([len(item[1]) for item in percentages])

    for _ in range(max_len):
        new_line = tab + ' '
        for item in percentages:
            if _ < len(item[1]) :
                new_line += f'{item[1][_]}  '
            else:
                new_line += '   '
        chart += '\n'+new_line

    return chart

    

food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')


food.deposit(1000, 'deposit')
food.withdraw(100, 'groceries')
food.withdraw(15, 'restaurant and more food for dessert')
food.transfer(50, clothing)

clothing.deposit(200)
clothing.withdraw(25,'t-shirts')

auto.deposit(500)
auto.withdraw(80, 'bike washer')

categories = [food,clothing,auto]
print(create_spend_chart(categories))