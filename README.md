# Expense-Tracker
# 💰 Expense Tracker CLI

A simple and lightweight command-line tool to track, list, and summarize your expenses using a JSON file.

---

## ✨ Features

- **Add an expense** with description, amount, and timestamp  
- **Delete an expense** by ID  
- **List all expenses** with details  
- **Summarize total expenses**  
- **Get monthly summaries** for a specific month  
- **Handles corrupt JSON files** gracefully

---

## 📦 Requirements

- Python **3.10+** (uses `match` statement)
- No external libraries (Python standard library only)

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/expense-tracker-cli.git
cd expense-tracker-cli

# Run the script
python main.py --help

🚀 Usage
Run the script from your terminal:

bash
Copy
Edit
python main.py <command> [options]
📜 Commands
Command	Description	Example
add	Add a new expense	python main.py add --description "Coffee" --amount 3.50
delete	Delete an expense by ID	python main.py delete --id 2
list	List all expenses	python main.py list
summary	Show total of all expenses	python main.py summary
get	Show expenses for a specific month	python main.py get --month 8

📂 Data Storage
Expenses are saved in expenses.json in the same directory as main.py.

Example entry:

json
Copy
Edit
{
    "id": 1,
    "description": "Coffee",
    "amount": 3.50,
    "date": "2025-08-10T14:30:00.000000"
}
🛡 Error Handling
Corrupt file detection → prompts to delete or exit.

Invalid amount → must be positive and have at most two decimal places.

Empty file handling → commands work even if there’s no data.

💡 Example Session
bash
Copy
Edit
$ python main.py add --description "Lunch" --amount 12.75
Expense "Lunch" added successfully (id:1)

$ python main.py list
Here is the list of all expenses:
{'id': 1, 'description': 'Lunch', 'amount': 12.75, 'date': '2025-08-10T14:30:00.000000'}

$ python main.py summary
Total expenses: $12.75

$ python main.py get --month 8
Expense for August: $12.75
📄 License
This project is open-source and free to use.

https://roadmap.sh/projects/expense-tracker
