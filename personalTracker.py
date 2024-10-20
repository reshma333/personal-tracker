from datetime import datetime
import pandas as pd
da = datetime.now()
import os
print(da)
expense_List = []  # Global list to store expenses
def addExpense():
  dateOfExpense = input("Please enter the date of expense: in YYYY-MM-DD format: ")
  dateObject = datetime.strptime(dateOfExpense, '%Y-%m-%d')
  date = dateObject.strftime('%Y-%m-%d')
  #month = dateObject.strftime('%Y-%m)
  categoryOfExpense = input("Enter the category of the expense, such as Food or Travel: ")
  amount = input("Enter Amount spent: ")
  description = input("please give a brief of this expense: ")
  expenses = {"dateOfExpense":date,"categoryOfExpense":categoryOfExpense,"amount":amount,"description":description}
  return expenses

def createExpenseList():
  global expense_List
  expense = addExpense()
  expense_List.append(expense)
  return expense_List

def viewExpense(expensesList):
  for expense in expensesList:
    allItems = validateExpenseList(expense)
    if allItems == True:
      for expenseDetails, value in expense.items():
           print(f"{expenseDetails}: {value}")
    else:
            print("Skipped an incomplete expense entry")
       
def validateExpenseList(expensesList):
  Required_key = ["dateOfExpense", "categoryOfExpense", "amount", "description"]
  for key in Required_key:
    if key not in expensesList:
       return False
  return True

def Tracking(expense):
    budget = float(input("Enter your total amount as your monthly budget: "))
    totalExpense = 0
    for exp in expense:  # Changed variable name to avoid confusion
        if validateExpenseList(exp):
            totalExpense += float(exp["amount"])  # Using float instead of int
    print(f"Your Total Expense (${totalExpense:.2f})")
    if totalExpense > budget:
        print(f"Your Expense (${totalExpense:.2f}) exceeded your budget (${budget:.2f})")
    else:
        remaining = budget - totalExpense
        print(f"You have ${remaining:.2f} left in your budget")

def totalExpense(expense):
    #budget = float(input("Enter your total amount as your monthly budget: "))
    totalExpense = 0
    for exp in expense:  # Changed variable name to avoid confusion
        if validateExpenseList(exp):
            totalExpense += float(exp["amount"])  # Using float instead of int
    print(f"Your Total Expense (${totalExpense:.2f})")
    return totalExpense


def saveExpense(expense):

  filePath = "/content/expense.csv"
  if os.path.exists(filePath):
  
      old_data = pd.read_csv(filePath)
      data = pd.DataFrame(expense)
      updateData = pd.concat([old_data, data], ignore_index=True) 
      updateData.to_csv(filePath, index=False)
      #print("Expenses saved successfully", updateData)

  else:
    updateData = pd.DataFrame(expense)
    updateData.to_csv(filePath, index=False)
    #print("Expenses saved successfully", updateData)
	
def loadExpense():
  try:
        data = pd.read_csv("/content/expense.csv")
        print("your saved expenses\n",data)
        return data.to_dict('records')
  except FileNotFoundError:
        print("No previous expense file found. Starting with an empty expense list.")
        return []

def personalExpense():
  global expenses
  expenses_old=loadExpense()
  
  while True:
     #print("expense_List in expenseList function", expenses)
     print("\n===== Expense Tracker Menu =====")
     print("0. New expense for new month")
     print("1. Add expense")
     print("2. View expenses")
     print("3. Track budget")
     print("4. Save expenses")
     print("5. Get the total expense")
     print("6. Exit")
            
     choice = input("Enter your choice (0-6): ")
     if choice == '0':
          print("your save expenses will be removed/n.")
          conf = input("Press yes/ no.")
          if conf=='yes':
            expenses = []
            expenses_old = []
            print("Starting a new month with an empty expense list.")
            expenses = createExpenseList()
          elif conf=='no':
            break
          else:
            print("Press yes/ no  to continue.")
        
     if choice == '1':
          expenses = createExpenseList()
     elif choice == '2':
          expenses=  expenses+expenses_old
          viewExpense(expenses)
     elif choice == '3':
          Tracking(expenses)
     elif choice == '4':
          saveExpense(expenses)
     elif choice == '5':
          totalExpense(expenses)
     elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
     else:
          print("Invalid choice. Please enter a number between 0 and 6.")
personalExpense()
