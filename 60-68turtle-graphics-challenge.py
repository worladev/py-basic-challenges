
### CHALLENGES AFTER LESSON ON [TURTLE GRAPHICS] ###
import random
import turtle


'''No60
Draw a square
'''
turtle.shape("turtle")
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()


'''No61
Draw a triangle
'''
#SOLUTION 1
for i in range(0,3):
    turtle.forward(100)
    turtle.right(120)

turtle.exitonclick()

#SOLUTION 2
for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)

turtle.exitonclick()


'''No62
Draw a circle
'''
for i in range(0,36):
    turtle.forward(15)
    turtle.right(10)

turtle.exitonclick()


'''No63
Draw three squares in a row with a gap between each. Fill them
using three different colors.
'''
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.exitonclick()


'''No64
Draw a five-pointed star
'''
for i in range(0,5):
    turtle.forward(100)
    turtle.right(145)

turtle.exitonclick()


'''No65
Write the numbers as shown below, starting at the bottom of
the number one. (As shown below is 1 2 3)
'''

turtle.left(90)
turtle.forward(100)
turtle.right(90)

turtle.penup()
turtle.forward(50)

turtle.pendown()
turtle.forward(65)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(65)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(65)

turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(45)
turtle.right(180)
turtle.forward(45)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

turtle.hideturtle()

turtle.exitonclick()


'''No66
Draw an octagon that uses a different color
(randomly selected from a list of six possible colors)
for each line
'''
colors = ["red", "yellow", "blue", "green", "black", "violet"]

for i in range(0, 8):
    turtle.color(random.choice(colors), '')
    turtle.forward(100)
    turtle.right(45)
    
turtle.exitonclick()


'''No67
Create the following pattern. (pattern cannot be replicated here)
'''
for i in range(0, 10):
    turtle.right(35)
    for i in range(0,8):
        turtle.forward(100)
        turtle.right(45)
    
turtle.exitonclick()


'''No68
Draw a pattern that will change each time the program is run.
Use the random function to pick the number of lines, the 
length of each line and the angle of each turn.
'''
lines = random.randint(5, 20)
for l in range(0, lines):
    length = random. randint(25, 100)
    rotate = random.randint(1, 200)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()

