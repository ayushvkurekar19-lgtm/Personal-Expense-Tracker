import pandas as pd
from database import get_connection

def add_expense(title, amount, category, expense_date, payment_method, notes=""):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO expenses
               (title, amount, category, expense_date, payment_method, notes)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (title, amount, category, expense_date, payment_method, notes)
        )

def get_expenses():
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT id, title, amount, category, expense_date, payment_method, notes
               FROM expenses ORDER BY expense_date DESC, id DESC"""
        ).fetchall()
    return pd.DataFrame([dict(row) for row in rows],
                        columns=["id", "title", "amount", "category", "expense_date",
                                 "payment_method", "notes"])

def update_expense(expense_id, title, amount, category, expense_date, payment_method, notes=""):
    with get_connection() as conn:
        conn.execute(
            """UPDATE expenses
               SET title=?, amount=?, category=?, expense_date=?, payment_method=?, notes=?
               WHERE id=?""",
            (title, amount, category, expense_date, payment_method, notes, expense_id)
        )

def delete_expense(expense_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
