import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A. - State guessing game")
screen.bgpic("Intermediate/Day25/blank_states_img.gif")

states = pandas.read_csv("Intermediate/Day25/50_states.csv")


game_is_on = True
tries = 3
while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    if len(states[states["state"] == answer_state]) > 0:
        state = states[states["state"] == answer_state].iloc[0]
        #print(state)

        correct_answer = turtle.Turtle(visible=False)
        correct_answer.penup()
        correct_answer.speed("fastest")
        correct_answer.goto(float(state.x), float(state.y))
        correct_answer.write(arg=str(state.state), font=("Arial", 8, "normal"))
    else:
        tries -= 1
        if tries == 0:
            game_is_on = False


turtle.mainloop()