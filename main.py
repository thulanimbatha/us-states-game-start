# use turtle to show screen
from os import stat
import turtle
import pandas

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

data = pandas.read_csv("50_states.csv") # access data
all_states = data["state"].to_list()    # list of states

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another State's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        break
    # check answer
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # create turtle
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        # access row data
        state_data_row = data[data.state == answer_state]
        state_name.goto(int(state_data_row["x"]), int(state_data_row["y"]))
        state_name.write(answer_state)

# turtle.mainloop()

# screen.exit on click exits as soon as coordinate is found
# screen.exitonclick() 

# TODO 1: generate csv file containing incorrect/forgotten guessees

