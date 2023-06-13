### CHALLENGES AFTER LESSON ON [MATHS] ###
print("\n")

import math

# 27 Ask the user to enter a number with lots of decimal places.
# Multiply this number by two and display the answer.
dec_num = float(input("Enter a number with lots of decimal places: "))
result = dec_num * 2
print(result)

# 28 Update program 027 so that it will display the snswer to
# two decimal places.
print("\n")
dec_num = float(input("Enter a number with lots of decimal places: "))
result = dec_num * 2
print(result)
print(f"{result} rounded to 2 decimal places: {round(result, 2)}")

# 29 Ask the user to enter an integer that is over 500.
# Work out the square root of that number and display
# it to two decimal places.
print("\n")
int_num = int(input("Enter an integer greater than 500: "))
if int_num > 500:
    square_root = math.sqrt(int_num)
    print(f"The square root of {int_num} is {round(square_root, 2)}")
else:
    print("Your number is not more than 500.")


# 30  Display pi to five decimal places.
print("\n")
print(round(math.pi, 5))

# 31 Ask the user to enter the radius of a circle
# (measurement from the centre point to the edge).
# Work out the area of the circle (pi*radius**2)
print("\n")
radius = float(input("Enter the radius: "))
area = math.pi * (radius**2)
print(f"The area of the circle is: {area}")


# 32 Ask for the radius and the depth of a cylinder and work
# out the total volume (circle area*depth) rounded to three
# decimal places.
print("\n")
radius = float(input("Enter the radius: "))
depth = float(input("Enter the depth: "))
circle_area = math.pi * (radius**2) 
total_volume = circle_area * depth
print(f"The volume is: {round(total_volume, 3)}")


# 33 Ask the user to enter two numbers. Use whole number
# division to divide the first number by the second and also
# work out the remainder and display the answer in a
# user-friendly way(e.g. if they enter 7 and 2 display "7
# divided by 2 is 3 with 1 remaining").
print("\n")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
whole_division = num1 // num2
remainder = num1 % num2
print(f"""{num1} divided by {num2} is {whole_division}
with {remainder} remaining.""")


# 34 Display the following message:
#       1) Square
#       2) Triangle
#
#       Enter a number:
# If the user enters 1, then it should ask them for the
# length of one of its sides and display the area. If they
# select 2, it should ask for the base and height of the
# triangle and display the area. If they type in anything
# else, it should give them a suitable error message.
print("\n")
print("1) Square \n2) Triangle ")
choice = int(input("Enter a number: "))
if choice == 1:
    length = float(input("Enter the lenght of one side: "))
    area_of_square = length**2
    print(f"The area of a square is: {area_of_square}")
elif choice == 2:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area_of_triangle = (base * height)/2
    print(f"The area of the Triangle is: {area_of_triangle}")
else:
    print("You have selected the wrong number.")