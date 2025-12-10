import arithmetic
import geometry
print("Hello, World!")

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))

arithmetic.add(num1, num2)
arithmetic.subtract(num1, num2)

len = int(input("Enter length : "))
br = int(input("Enter breadth : "))

geometry.calc_rect_area(len, br)
geometry.calc_rect_peri(len, br)
