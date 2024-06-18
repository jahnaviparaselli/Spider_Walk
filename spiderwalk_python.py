6import turtle
import math

# Define the spider shape
spider_shape = ((-10,0), (-10,10), (0,15), (10,10), (10,0), (5,-10), (-5,-10), (-10,0))

# Add the spider shape to the turtle module
turtle.register_shape('spider', spider_shape)

# Create a function to get the number of sides from the user
def get_num_sides():
    num_sides = turtle.textinput("Input", "Enter the number of sides for the polygon:")
    num_sides = int(num_sides)
    return num_sides

# Call the get_num_sides() function to get the number of sides
num_sides = get_num_sides()

# Calculate the interior angle of the polygon
int_angle = ((num_sides * 180) - 360) / num_sides

# Calculate the length of each side
side_length = int(75 * 1 / (2 * math.sin(math.pi / num_sides)))

# Calculate the angle offset for odd-sided polygons
if num_sides % 2 == 1:
    angle_offset = 90
else:
    angle_offset = 0
# Calculate the radius of the spider web
radius = 2.5*side_length * num_sides / (2 * math.pi)

# Create a turtle object and set its speed
t = turtle.Turtle()
t.speed(2)

# Set the turtle shape to the spider shape
t.shape('spider')

# Draw the radial threads of the spider web
for i in range(num_sides):
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.setheading(360 / num_sides * i + angle_offset)
    t.forward(radius)

# Create another turtle object for drawing the polygon
t = turtle.Turtle()
t.speed(1)

# Set the turtle shape to the spider shape
t.shape('spider')

# Position the turtle at the center of the polygon
t.penup()
t.setposition(-side_length/2, -side_length/(2*math.tan(math.pi/num_sides)))
t.pendown()

# Draw the polygon
for i in range(num_sides):
    t.forward(side_length)
    t.left(360 / num_sides)

# Wait for the user to close the window
turtle.done()