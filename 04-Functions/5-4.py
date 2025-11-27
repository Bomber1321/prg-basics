import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(60)
pen.color("red")
# Side length
side_length = 0
pen.hideturtle()
# Draw a square
for i in range(10000):
    side_length=side_length+(i%2)+1
    pen.forward(side_length)
    pen.right(90)

# Hide the turtle and finish

window.mainloop()