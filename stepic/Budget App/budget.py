import math
from itertools import zip_longest

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total_withdraw = []

    def __str__(self):
         return f'{self.print_self()}'

    def deposit(self, amount, description=''):
        self.ledger_record = {"amount": amount, "description": description}
        self.ledger.append(self.ledger_record)

    def get_balance(self):
        balance = 0
        for record in self.ledger:
            balance += record["amount"]
        return balance

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger_record = {"amount": -amount, "description": description}
            self.ledger.append(self.ledger_record)
            self.total_withdraw.append(amount)
            return True
        else:
            return False

    def withdraw_sum(self):
        total = 0
        for entry in self.ledger:
            if entry['amount'] < 0 and 'Transfer' not in entry['description']:
                total += entry['amount']
        return -total


    def transfer(self, amount, to_category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f'Transfer to {to_category}')
            to_category.deposit(amount, description=f'Transfer from {self.category}')
            return True
        else:
            return False

    def print_self(self):
        n = (30 - len(str(self.category))) / 2  # Calculating how many * to print in title
        stars = '*' * int(n)
        title = f'{stars}{self.category}{stars}'

        print(title)
        # TODO Исправить - почему длина числа считается без символов после точки?
        for entry in self.ledger:
            amount_str = str(entry['amount'])[0:7]
            description_str = entry['description'][0:23]
            #print('Длина описания', len(description_str))
            #print('Длина числа', len(amount_str))
            spaces = (30 - len(description_str) - len(amount_str)) * ' '
            print(entry['description'][0:23], spaces, str("{:.2f}".format(entry['amount'])[0:7]))
        print('Total: ', str("{:.2f}".format(self.get_balance())[0:7]))



def create_spend_chart(list_of_categories):
    total = 0
    category_percent = {}

    # for item in list_of_categories:
    #     item_balance = item.get_balace()
    #     percent = (item_balance/ total * 100)/10
    #     category_percent[item] = int(percent)

    for item in list_of_categories:
        total += item.withdraw_sum()

    for item in list_of_categories:
        percent = (item.withdraw_sum() / total * 100)
        category_percent[item.category] = math.ceil(percent)

    values_as_list = [*category_percent.values()]

    x = 100  # For percentage column

    def roundup(number):
        return int(math.ceil(number / 10.0)) * 10

    print('Percentage spent by category')
    for n in range(11):
        print(f"{(3 - len(str(x)))*' '}{x}| ", end='')  # Printing percentage column
        for i in range(len(values_as_list)):
            if roundup(values_as_list[i]) >= x:
                print('o ', end=' ')  # Printing o if category percentage == percentage column
            else:
                print('  ', end=' ')
        print()
        x -= 10
    print(' '*3,'-'*(4+len(list_of_categories)*2))

    text = ''

    for name in list_of_categories:
        text += name.category
        text += ' '

    for letter in zip_longest(*text.split(), fillvalue=' '):
        print('    ','  '.join(letter))

#TODO почему-то если передать в метод transfer название другой категории,
# это триггерит print_self() видимо из-за def __str__(self)

#TODO глючит передача description при transfer - в print_self() отображается пустота вместо description трансфера