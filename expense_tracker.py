"""Simple command-line expense tracker.

Run:  python expense_tracker.py
Expenses are saved to expenses.csv so they are still there next time.
"""
import csv
from datetime import date
from pathlib import Path

FILE = Path("expenses.csv")
FIELDS = ["date", "category", "amount", "note"]


def load_expenses():
    """Read all expenses from the CSV file (empty list if it doesn't exist yet)."""
    if not FILE.exists():
        return []
    with FILE.open(newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["amount"] = float(row["amount"])
    return rows


def save_expense(expense):
    """Append one expense to the CSV file, writing the header if the file is new."""
    is_new = not FILE.exists()
    with FILE.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(expense)


def total_by_category(expenses):
    """Return {category: total amount spent}."""
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals


def total_by_month(expenses):
    """Return {'YYYY-MM': total amount spent}."""
    totals = {}
    for e in expenses:
        month = e["date"][:7]
        totals[month] = totals.get(month, 0) + e["amount"]
    return totals


def ask_amount():
    """Keep asking until the user types a valid positive number."""
    while True:
        text = input("Amount ($): ").strip()
        try:
            amount = float(text)
            if amount <= 0:
                raise ValueError
            return round(amount, 2)
        except ValueError:
            print("Please enter a number greater than 0.")


def ask_date():
    """Ask for a date (YYYY-MM-DD); pressing Enter uses today."""
    while True:
        text = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if not text:
            return date.today().isoformat()
        try:
            return date.fromisoformat(text).isoformat()
        except ValueError:
            print("Please use the format YYYY-MM-DD, like 2026-11-08.")


def add_expense():
    category = input("Category (e.g. food, books, transport): ").strip().lower() or "other"
    amount = ask_amount()
    when = ask_date()
    note = input("Note (optional): ").strip()
    save_expense({"date": when, "category": category, "amount": amount, "note": note})
    print(f"Saved ${amount:.2f} for {category}.")


def show_all():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    print(f"\n{'Date':<12}{'Category':<14}{'Amount':>9}  Note")
    for e in sorted(expenses, key=lambda x: x["date"]):
        print(f"{e['date']:<12}{e['category']:<14}{e['amount']:>9.2f}  {e['note']}")


def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    print("\nSpending by category:")
    by_cat = total_by_category(expenses)
    for cat, amt in sorted(by_cat.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<14}${amt:>8.2f}")
    print("\nSpending by month:")
    for month, amt in sorted(total_by_month(expenses).items()):
        print(f"  {month:<14}${amt:>8.2f}")
    print(f"\nTotal: ${sum(by_cat.values()):.2f}")


def main():
    menu = {"1": ("Add an expense", add_expense),
            "2": ("View all expenses", show_all),
            "3": ("Show summary", show_summary)}
    while True:
        print("\n--- Expense Tracker ---")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("4. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        if choice in menu:
            menu[choice][1]()
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
