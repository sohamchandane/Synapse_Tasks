import math
from functools import reduce
import time

request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transactions": [
        {"amount": -9000.00, "category": "Creatives"},
        {"amount": 7000.00, "category": "Sponsor"},
        {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    
    "Arham": {
        "balance": 5000.00,
        "transactions": [
        {"amount": 8000.00, "category": "Stalls"},
        {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    
    "Unnati": {
        "balance": 3500.00,
        "transactions": [
        {"amount": -5000.00, "category": "Attraction"},
        {"amount": 2500.00, "category": "Promo"},
        {"amount": -900.00, "category": "Lighting"},
        {"amount":-3000.00, "category": "Games"}
        ]
    },
    
    "Gaurang": {
        "balance": 2000.00,
        "transactions": [
        {"amount": -1500.00, "category": "Website"},
        {"amount": -1000.00, "category": "C2C"},
        {"amount": -500.00, "category": "Posters"}
        ]
    }
}

def total_spending(request_spending, account_id, category):
    transactionList = request_spending[f"{account_id}"]["transactions"]
    specificTransaction = list(filter(lambda dtn: dtn["category"] == category and dtn["amount"]<0, transactionList))

    amountSpent = 0
    if len(specificTransaction)==1:
        amountSpent = math.fabs(specificTransaction[0]["amount"])

    return f"\nAccount ID: {account_id}\n\tCategory: \t{category}\n\tAmount spent: \t{amountSpent}"

print(total_spending(request_spending, "Gaurang", "C2C"))
print(total_spending(request_spending, "Mahek", "Creatives"))
print(total_spending(request_spending, "Arham", "Stalls"))
print(total_spending(request_spending, "Unnati", "Attraction"))
time.sleep(1)

print("\n\n***** EVENT STATUS: STARTED *****")
time.sleep(1)
print("***** EVENT STATUS: ONGOING *****")
time.sleep(1)
print("***** EVENT STATUS: FINISHED *****\n\n")
time.sleep(1)


print("\n\t*****BALANCE SHEET*****")
def account_balance(request_spending, account_id):
    accountBalance = request_spending[f"{account_id}"]["balance"]
    
    #THIS SHOULD BE USED IF GIVEN BALANCE IS INITIAL BALANCE AND NOT BALANCE
    '''transactionList = request_spending[f"{account_id}"]["transactions"]
    transactionList = list(map(lambda dtn: dtn["amount"], transactionList))
    transactionList = list(filter(lambda value: value>=0, transactionList))
    accountBalance = request_spending[f"{account_id}"]["balance"] + sum(transactionList)'''
    
    return f"Account ID: {account_id}\tBalance: {accountBalance}"

print(account_balance(request_spending, "Mahek"))
print(account_balance(request_spending, "Arham"))
print(account_balance(request_spending, "Unnati"))
print(account_balance(request_spending, "Gaurang"))
time.sleep(1)


print("\n\t*****MONEY OWED*****")
def money_owed(request_spending, account_id):
    transactionList = request_spending[f"{account_id}"]["transactions"]
    transactionList = list(map(lambda dtn: dtn["amount"], transactionList))
    moneyOwed = request_spending[f"{account_id}"]["balance"] + sum(transactionList)
    
    if moneyOwed>0:
        return f"Money Owed by {account_id}: 0"
    return f"Money Owed by {account_id}: {math.fabs(moneyOwed)}"

print(money_owed(request_spending, "Mahek"))
print(money_owed(request_spending, "Arham"))
print(money_owed(request_spending, "Unnati"))
print(money_owed(request_spending, "Gaurang"))
time.sleep(1)