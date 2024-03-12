class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"Expense: {self.name}, Category: {self.category}, Amount: ${self.amount:.2f}"



def main():
    print("Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    # Get user input for expense.
    expense = get_user_expenses()

    # Write
    save_expense_to_file(expense, expense_file_path)

    summarize_expense(expense_file_path)


def get_user_expenses():
    print("Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        select_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if select_index in range(len(expense_categories)):
            select_category = expense_categories[select_index]
            new_expense = Expense(name=expense_name, category=select_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense :{expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path):
    print(f"Summarizing User Expenses")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=str(expense_name), amount=float(expense_amount), category=str(expense_category)
            )
            expenses.append(line_expense)
    
    for expense in expenses:
        print(expense)


if __name__ == "__main__":
    main()

