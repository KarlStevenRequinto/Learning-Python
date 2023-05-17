# 1 - Course Overview
# 2 - Data Types
# 3 - Conditionals and Imports
    # if, elif, else
    # logical operators
    # and, or, not
    # importing modules
# 4 - List and Loops
# 5 - Dictionaries, JSON, Pip
    # venv envi
# 6 - Functions

# ========================================================
# total = 0
# expenses = []
# for i in range(7):
#     expenses.append(float(input("enter an expense:")))

# total = sum(expenses)

# print("You spent $", total, sep="")

import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()
print(json)
