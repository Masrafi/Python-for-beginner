# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def calculate_area( base, height):
    return (1 / 2) + base * height


base = input("Enter base: ")
height = input("Enter height: ")

base = int(base)
height = int(height)

result = calculate_area(base, height)
print(result)
