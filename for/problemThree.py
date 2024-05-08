# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.


expense_list = [2340, 2500, 2100, 3100, 2980]

num = input("Enter a number: ")
num = int(num)

if num in expense_list:
    print("Occurred")
else:
    print("Not occurred")
