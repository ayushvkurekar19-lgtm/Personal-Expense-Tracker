# Personal Expense Tracker

A beginner-friendly web application built with Python, Streamlit, and SQLite.

## Modules

### 1. Expense Management
- Add, view, edit, and delete expense records.
- Record amount, category, date, payment method, and optional notes.
- Export expense records to CSV.

### 2. Budget Monitoring & Analytics
- Set a monthly budget.
- View monthly spending and remaining budget.
- See budget usage and category-wise spending.

## Requirements
- Python 3.10 or later recommended
- Git
- Internet connection for the first dependency installation

## Run on Windows PowerShell

Open PowerShell in this project folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks environment activation, use this for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The app normally opens at `http://localhost:8501`.

## Database
The application creates `expenses.db` automatically in the project folder when it first runs. The database is intentionally excluded from Git because it contains local user-entered expense data.

## Suggested manual test cases
1. Add an expense with a name, amount, category, date, and payment method.
2. Confirm the record appears in the expense table.
3. Edit the amount or category and save.
4. Delete a test expense.
5. Set a monthly budget and save it.
6. Add expenses dated in the selected month and verify the total.
7. Check that category-wise analytics appear for that month.
8. Download the expense table as CSV.

## Jira
Suggested Jira work items:
- Set up SQLite database and expense table
- Design the Add Expense form
- Implement expense record management
- Implement monthly budget setting
- Implement spending analytics dashboard
- Test expense management and database operations

## GitHub
Do not commit `.env` files, passwords, personal data, or the generated SQLite database.
