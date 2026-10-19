# Personal Expense Tracker

A beginner-friendly web application built using Python, Streamlit, and SQLite to manage personal expenses and monitor monthly spending.

## Features

### 1. Expense Management
- Add, view, edit, and delete expense records.
- Store expense title, amount, category, date, payment method, and optional notes.
- Export expense records to CSV.

### 2. Budget Monitoring & Analytics
- Set and save a monthly budget.
- View total spending and remaining budget for the selected month.
- View budget usage and category-wise spending.
- Display an over-budget warning when spending exceeds the budget.

## Technology Stack

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Database:** SQLite
- **Version Control:** Git and GitHub
- **Project Management:** Jira

## Requirements

- Python 3.10 or later recommended
- Git
- Internet connection for the initial dependency installation

## Installation and Setup (Windows PowerShell)

1. Open PowerShell in the project folder.
2. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

3. Activate the virtual environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the required packages:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Start the application:

   ```powershell
   python -m streamlit run app.py
   ```

6. Open the local URL shown in the terminal, normally:

   `http://localhost:8501`

### If PowerShell blocks environment activation

Run the following commands in the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Then start the application using:

```powershell
python -m streamlit run app.py
```

## Database

The application uses SQLite to store expense records and monthly budgets. The database file, `expenses.db`, is created in the project folder when the application initializes the database.

The generated database is excluded from Git to avoid committing local expense data.

## Manual Testing

The following functionality has been manually tested:

- Adding, viewing, editing, and deleting expense records.
- Setting a monthly budget.
- Calculating monthly spending and remaining budget.
- Displaying category-wise spending analytics.
- Showing an over-budget warning when expenses exceed the budget.
- Retaining saved data after browser refresh.
- Retaining saved data after restarting the Streamlit server.

Additional test cases can include invalid inputs, empty records, and CSV export verification.

## Jira Project Management

Jira is used to organize project work, track implementation progress, and document testing.

Key work items include:

- Set up SQLite database and expense table.
- Design the Add Expense form.
- Implement expense record management.
- Implement monthly budget setting.
- Implement spending analytics dashboard.
- Test expense management and database operations.

## GitHub and Data Safety

- Source code is maintained in Git and GitHub.
- Do not commit `.env` files, passwords, credentials, or personal expense data.
- The generated SQLite database is excluded from version control through `.gitignore`.
