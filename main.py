import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def solution_turtle(solution, x, y):
    papa4 = Turtle()
    papa4.hideturtle()
    papa4.penup()
    papa4.speed(0)
    papa4.setposition(x, y)
    papa4.write(f"{solution}")


def coordinates(answer):
    if answer in state_list:
        correct_a = data[data.state == answer]
        x_cord = int(correct_a["x"])
        y_cord = int(correct_a["y"])
        solution_turtle(answer, x_cord, y_cord)
        return x_cord, y_cord
    else:
        return False


data = pandas.read_csv("50_states.csv")
state_list = list(data.state)
game_is_on = True
i = 0
correct_guesses = []
while game_is_on:

    answer_state = screen.textinput(title=f"{i}/50 correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in state_list if state not in correct_guesses]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    if coordinates(answer_state) and i != 50:
        coordinates(answer_state)
        correct_guesses.append(answer_state)
        i += 1
        if i == 50:
            game_is_on = False
    elif not coordinates(answer_state) and i != 50:
        answer_state = screen.textinput(title=f"{i}/50 correct", prompt="What's another state's name?")


