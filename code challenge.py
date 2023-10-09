# Function to calculate total monthly expenses
def calculate_total_expenses(rent, electric, water, internet, personal, groceries):
    total_expenses = rent + electric + water + internet + personal + groceries
    return total_expenses

# Input variables for monthly expenses
rent = float(input("Enter monthly rent: $"))
electric = float(input("Enter monthly electric bill: $"))
water = float(input("Enter monthly water bill: $"))
internet = float(input("Enter monthly internet bill: $"))
personal = float(input("Enter monthly personal expenses: $"))
groceries = float(input("Enter monthly groceries expenses: $"))

#Calculate Total Expenses 
