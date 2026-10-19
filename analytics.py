import pandas as pd
from database import get_connection

def set_monthly_budget(month, amount):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO budgets (month, amount) VALUES (?, ?)
               ON CONFLICT(month) DO UPDATE SET amount=excluded.amount""",
            (month, amount)
        )

def get_monthly_budget(month):
    with get_connection() as conn:
        row = conn.execute("SELECT amount FROM budgets WHERE month=?", (month,)).fetchone()
    return float(row["amount"]) if row else 0.0

def monthly_summary(month):
    with get_connection() as conn:
        row = conn.execute(
            """SELECT COALESCE(SUM(amount), 0) AS spent, COUNT(*) AS count
               FROM expenses WHERE substr(expense_date, 1, 7)=?""",
            (month,)
        ).fetchone()
    return float(row["spent"]), int(row["count"])

def category_summary(month):
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT category, ROUND(SUM(amount), 2) AS total
               FROM expenses WHERE substr(expense_date, 1, 7)=?
               GROUP BY category ORDER BY total DESC""",
            (month,)
        ).fetchall()
    return pd.DataFrame([dict(row) for row in rows], columns=["category", "total"])
