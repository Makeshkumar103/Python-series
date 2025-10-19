from tabulate import tabulate
# Replace the expense print section in view_expenses() with:
print(tabulate(rows, headers=["ID", "Date", "Category", "Amount", "Description"], tablefmt="grid"))

import pandas as pd
# Example: View expenses as a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM expenses", conn)
print(df)

from rich.console import Console
from rich.table import Table

console = Console()

def view_expenses():
    table = Table(title="Expenses")
    table.add_column("ID", style="cyan")
    table.add_column("Date", style="magenta")
    table.add_column("Category", style="green")
    table.add_column("Amount", style="yellow")
    table.add_column("Description", style="blue")
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(str(row[0]), row[1], row[2], f"{row[3]:.2f}", row[4])
    console.print(table)
