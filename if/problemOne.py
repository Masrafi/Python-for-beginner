# Identify even & odd number

num = input("Enter a number: ")

print(type(num))
num = int(num)

if num % 2 == 0:
    print("Even")
else:
    print("odd")

# or

print("Ternary operator demo")
n = input("Enter a number:")
n = int(n)
message = "Number is even" if n % 2 == 0 else "Number is odd"
print(message)
