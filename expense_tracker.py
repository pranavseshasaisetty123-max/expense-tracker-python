print("Personal Expense Tracker")

expenses = []
try:

    file = open("expenses.txt", "r")

    for line in file:

        line = line.strip()

        data = line.split(",")

        expenses.append(
            [
                data[0],
                data[1],
                float(data[2])
            ]
        )

    file.close()

except FileNotFoundError:

    pass

def add_expense():
    expense_name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))

    expenses.append([expense_name, category, amount])

    print("Expense added successfully!")
def view_expenses():

    print("\nYour Expenses:")

    for expense in expenses:
        print(
            expense[0],
            "|",
            expense[1],
            "| ₹",
            expense[2]
        )
def show_total():
    total = 0
    for expense in expenses:
        total = total + expense[2]

    print(f"\nTotal Spending = ₹{total}")
def delete_expense():
    print("\nExpenses:")
    for i in range(len(expenses)):
        print(i,"-",expenses[i])
    index=int(input("Enter the expense number to be delete :"))
    expenses.pop(index)
    print("Expense deleted sucessfully!")

def category_summary():
    summary={}
    for expense in expenses:
        category=expense[1]
        amount=expense[2]
        if category in summary:
            summary[category] +=amount
        else:
            summary[category]=amount
    print("\nExpense Summary")
    for category,total in summary.items():
        print(category, ": ₹",total)   
def search_category():

    category_name = input("Enter category: ")

    print("\nMatching Expenses:")

    found = False

    for expense in expenses:

        if expense[1].lower() == category_name.lower():

            print(
                expense[0],
                "|",
                expense[1],
                "| ₹",
                expense[2]
            )

            found = True

    if not found:
        print("No expenses found.")

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Delete Expense")
    print("5. Save Expenses")
    print("6. Category Summary")
    print("7. Search By Catogory")
    print("8.Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
        
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        delete_expense()
       
    elif choice == "5":
        file= open("expenses.txt","w")
        for expense in expenses:
            file.write(f"{expense[0]},{expense[1]},{expense[2]}\n")
        file.close()
        print("Expenses saved sucessfully!")
    elif choice == "6":
        category_summary()
    elif choice =="7":
        search_category()
    elif choice == "8":
        print("Goodbye!")
        break


