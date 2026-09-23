total = 0
number_of_expenses = int(input("How many expenses do you want to enter? "))
for i in range(number_of_expenses):
    expense = float(input("Enter expense amount: ₹"))
    total = total + expense
print("Total Spent: ₹", total)