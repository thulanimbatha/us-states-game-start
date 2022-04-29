# use turtle to show screen
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
# add the shape first
screen.addshape(image)
# then show added shape
turtle.shape(image)

screen.exitonclick()