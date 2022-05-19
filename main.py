# use turtle to show screen
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
# add the shape first
screen.addshape(image)
# then show added shape
turtle.shape(image)
# we already have the coordinates
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

answer_state = screen.textinput(title="Guess The State", prompt="What's another State's name?")
print(answer_state)

turtle.mainloop()

# screen.exit on click exits as soon as coordinate is found
# screen.exitonclick() 

# TODO 1: convert guess to title case
# TODO 2: CHeck is the guess is among the 50 States
# TODO 3: Write correct guess onto the map
# TODO 4: Use a loop to allow the user to keep guessing
# TODO 5: Record the correct guesses in a list
# TODO 6: Keep track of the score
