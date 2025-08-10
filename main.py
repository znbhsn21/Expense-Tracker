import os
import json
import argparse
from datetime import datetime

file_path = "expenses.json"

def read_expenses():

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: The JSON file is corrupt.")
        user_input = input("Do you want to delete the corrupt file and proceed? (yes/no): ").strip().lower()
        if user_input == 'yes':
            os.remove(EXPENSES_FILE)
            print("The corrupt file has been deleted. Proceeding with an empty list.")
            return []
        else:
            print("Please delete the corrupt file manually to proceed.")
            exit(1)

def write_expenses(expenses):

    with open(file_path, "w") as f:
        json.dump(expenses, f, indent = 4)

def get_month(month):

    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][month - 1]

def add_expenses(description, amount):

    if amount <= 0:
        print("Invalid, amount must be greater than zero")
        return

    try:
        amount = float(amount)
        if round(amount, 2) != amount:
            raise ValueError("Amount must have at least two decimal places")
    except ValueError as e:
        print(f"{e}")
        return

    expenses = read_expenses()

    if len(expenses) == 0:
        expense_id = 1
    else:
        expense_id = expenses[-1]["id"] + 1

    expenses.append({
        "id":expense_id,
        "description":description,
        "amount":amount,
        "date":datetime.now().isoformat()
    })

    write_expenses(expenses)

    print(f'Expense "{description}" added successfully (id:{expense_id})')

def delete_expense(expense_id):
    if(os.path.exists(file_path)):
        expenses = read_expenses()
        updated_expenses = [expense for expense in expenses if expense["id"] != expense_id]
        with open(file_path, "w") as f:
            json.dump(updated_expenses, f, indent=4)
            print(f'Expense Deleted (id:{expense_id})')
    else:
        print("There is nothing to delete")

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

parser_add = subparsers.add_parser("add", help="Add a new expense")
parser_add.add_argument("--description", required=True, type=str, help="Description of expense")
parser_add.add_argument("--amount", required=True, type=float, help="Amount of expense")

parser_delete = subparsers.add_parser("delete", help="Delete an expense")
parser_delete.add_argument("--id", required=True, type=int, help="ID of the expense to delete")

args = parser.parse_args()

match args.command:
    case "add":
        add_expenses(args.description, args.amount)
    case "delete":
        delete_expense(args.id)






