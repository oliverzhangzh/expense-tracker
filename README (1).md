# Expense Tracker

A simple command-line expense tracker written in Python. Log what you spend, then see
totals by category and by month. Data is saved to a CSV file so it persists between runs.

## Features

- Add expenses with a date, category, amount, and optional note
- View all expenses sorted by date
- Summarize spending by category and by month
- Input validation for amounts and dates
- Data saved to `expenses.csv` using Python's built-in `csv` module
- Unit tests for the summary functions

## How to Run

Requires Python 3.8 or newer. No extra libraries are needed to run the tracker.

```
python expense_tracker.py
```

To run the tests:

```
pip install pytest
python -m pytest
```

## Example

```
--- Expense Tracker ---
1. Add an expense
2. View all expenses
3. Show summary
4. Quit

Spending by category:
  books         $   40.00
  food          $   12.50

Spending by month:
  2026-10       $   12.50
  2026-11       $   40.00

Total: $52.50
```

## Files

- `expense_tracker.py`: the program
- `test_expense_tracker.py`: unit tests for the totals functions

## What I'd add next

- [e.g. delete an expense, filter by month, or a monthly budget warning]
