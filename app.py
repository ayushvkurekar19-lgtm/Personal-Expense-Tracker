import streamlit as st
import pandas as pd
from database import init_db
from expenses import add_expense, get_expenses, update_expense, delete_expense
from analytics import set_monthly_budget, get_monthly_budget, monthly_summary, category_summary

st.set_page_config(page_title="Personal Expense Tracker", page_icon="💸", layout="wide")
init_db()

st.title("💸 Personal Expense Tracker")
st.caption("Track expenses, manage your monthly budget, and understand your spending.")

page = st.sidebar.radio(
    "Choose a module",
    ["Expense Management", "Budget Monitoring & Analytics"]
)

if page == "Expense Management":
    st.header("Module 1: Expense Management")
    with st.form("add_expense_form", clear_on_submit=True):
        left, right = st.columns(2)
        with left:
            title = st.text_input("Expense name", placeholder="e.g. Lunch")
            amount = st.number_input("Amount (₹)", min_value=0.01, step=10.0, format="%.2f")
            category = st.selectbox(
                "Category",
                ["Food", "Transport", "Shopping", "Bills", "Education", "Health", "Entertainment", "Other"]
            )
        with right:
            expense_date = st.date_input("Date")
            payment_method = st.selectbox("Payment method", ["Cash", "UPI", "Card", "Net Banking", "Other"])
            notes = st.text_input("Notes (optional)")
        submitted = st.form_submit_button("Add expense", type="primary")
        if submitted:
            if not title.strip():
                st.error("Please enter an expense name.")
            else:
                add_expense(title.strip(), amount, category, str(expense_date), payment_method, notes.strip())
                st.success("Expense added successfully.")
                st.rerun()

    st.subheader("Expense records")
    records = get_expenses()
    if records.empty:
        st.info("No expenses yet. Add your first expense using the form above.")
    else:
        st.dataframe(records, use_container_width=True, hide_index=True)
        st.download_button(
            "Download expenses as CSV",
            data=records.to_csv(index=False).encode("utf-8"),
            file_name="expenses.csv",
            mime="text/csv"
        )

        st.subheader("Edit or delete an expense")
        options = {
            f"#{int(row['id'])} — {row['title']} (₹{float(row['amount']):.2f})": int(row["id"])
            for _, row in records.iterrows()
        }
        selected_label = st.selectbox("Choose an expense", list(options.keys()))
        selected_id = options[selected_label]
        row = records.loc[records["id"] == selected_id].iloc[0]

        with st.form("edit_expense_form"):
            c1, c2 = st.columns(2)
            with c1:
                edit_title = st.text_input("Expense name", value=str(row["title"]))
                edit_amount = st.number_input("Amount (₹)", min_value=0.01, value=float(row["amount"]), step=10.0)
                edit_category = st.selectbox(
                    "Category",
                    ["Food", "Transport", "Shopping", "Bills", "Education", "Health", "Entertainment", "Other"],
                    index=["Food", "Transport", "Shopping", "Bills", "Education", "Health", "Entertainment", "Other"].index(row["category"])
                )
            with c2:
                edit_date = st.date_input("Date", value=pd.to_datetime(row["expense_date"]).date())
                methods = ["Cash", "UPI", "Card", "Net Banking", "Other"]
                current_method = row["payment_method"] if row["payment_method"] in methods else "Other"
                edit_method = st.selectbox("Payment method", methods, index=methods.index(current_method))
                edit_notes = st.text_input("Notes", value=str(row["notes"] or ""))
            save = st.form_submit_button("Save changes")
            if save:
                if not edit_title.strip():
                    st.error("Please enter an expense name.")
                else:
                    update_expense(selected_id, edit_title.strip(), edit_amount, edit_category,
                                   str(edit_date), edit_method, edit_notes.strip())
                    st.success("Expense updated.")
                    st.rerun()

        if st.button("Delete selected expense", type="secondary"):
            delete_expense(selected_id)
            st.success("Expense deleted.")
            st.rerun()

else:
    st.header("Module 2: Budget Monitoring & Analytics")
    today = pd.Timestamp.today()
    col1, col2 = st.columns(2)
    with col1:
        budget_month = st.date_input("Choose month", value=today.replace(day=1).date())
    month_key = budget_month.strftime("%Y-%m")
    current_budget = get_monthly_budget(month_key)
    with col2:
        new_budget = st.number_input("Monthly budget (₹)", min_value=0.0, value=float(current_budget), step=500.0)
    if st.button("Save monthly budget", type="primary"):
        set_monthly_budget(month_key, new_budget)
        st.success("Monthly budget saved.")
        st.rerun()

    spent, count = monthly_summary(month_key)
    remaining = new_budget - spent
    m1, m2, m3 = st.columns(3)
    m1.metric("Monthly budget", f"₹{new_budget:,.2f}")
    m2.metric("Total spent", f"₹{spent:,.2f}")
    m3.metric("Remaining", f"₹{remaining:,.2f}", delta=f"{count} expense(s)")

    if new_budget > 0:
        progress = min(spent / new_budget, 1.0)
        st.progress(progress, text=f"{(spent / new_budget * 100):.1f}% of budget used")
        if spent > new_budget:
            st.error(f"You are over budget by ₹{spent - new_budget:,.2f}.")
        elif spent >= new_budget * 0.8:
            st.warning("You have used at least 80% of your monthly budget.")
        else:
            st.success("You are currently within your monthly budget.")

    st.subheader("Category-wise spending")
    categories = category_summary(month_key)
    if categories.empty:
        st.info("No expenses found for this month. Add expenses in Module 1 to see analytics.")
    else:
        st.bar_chart(categories.set_index("category")["total"])
        st.dataframe(categories, use_container_width=True, hide_index=True)
