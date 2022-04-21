import budget
from budget import create_spend_chart

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())

clothing = budget.Category("Clothing")
food.transfer(100, clothing)
clothing.withdraw(25.55)
clothing.withdraw(10)
#print(clothing.get_balance())

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
auto.transfer(50, food)
#print(auto.get_balance())
#print(food)
print(clothing)

#print(create_spend_chart([food, clothing, auto]))