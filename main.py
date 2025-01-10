class Category:
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
        
    
    def deposit(self,amount,description=''):
        self.amount += amount
        self.ledger.append({'amount':amount,'description':description})

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({'amount':-amount,'description':description})
            return True
        else:
            return False

    def get_balance(self):
        return self.amount  

    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {other_category.category}')
            other_category.deposit(amount,f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self,amount):
        if self.amount >= amount:
            return True
        return False
    

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)