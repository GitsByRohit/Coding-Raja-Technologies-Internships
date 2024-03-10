


# Define a function to add an expense
def add_expense(expenses, category, amount, description=""):
  """Adds an expense to the given dictionary.

  Args:
      expenses: A dictionary to store expenses. (category, [amount, description])
      category: The category of the expense (e.g., "Groceries", "Rent").
      amount: The amount of the expense.
      description: (Optional) A description of the expense.
  """
  if category not in expenses:
    expenses[category] = []
  expenses[category].append((amount, description))

# Define a function to display the expenses
def display_expenses(expenses):
  """Prints the expenses in a formatted way.

  Args:
      expenses: A dictionary containing expenses. (category, [amount, description])
  """
  total_expense = 0
  for category, transactions in expenses.items():
    print(f"\nCategory: {category}")
    for amount, description in transactions:
      print(f"\t- Amount: ₹{amount:.2f} ({description})")
      total_expense += amount
  print(f"\nTotal Expense: ₹{total_expense:.2f}")

# Initialize an empty dictionary to store expenses
expenses = {}

# Main loop to interact with the user
while True:
  # Display options
  print("\nBudget Tracker")
  print("1. Add Expense")
  print("2. Display Expenses")
  print("3. Exit")

  # Get user choice
  choice = input("Enter your choice: ")

  # Handle user choice
  if choice == "1":
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description (optional): ")
    add_expense(expenses, category, amount, description)
  elif choice == "2":
    if not expenses:
      print("No expenses added yet.")
    else:
      display_expenses(expenses)
  elif choice == "3":
    break
  else:
    print("Invalid choice. Please try again.")

print("Exiting Budget Tracker.")


