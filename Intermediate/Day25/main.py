import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A. - State guessing game")
screen.bgpic("Intermediate/Day25/blank_states_img.gif")

states = pandas.read_csv("Intermediate/Day25/50_states.csv")
states_list = states.state.to_list()

game_is_on = True
tries = 3
score = 0
answered_state_names = []
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States correct (Remaining tries: {tries})", prompt="What's another state's name?")
    if answer_state in states_list:
        if answer_state in answered_state_names:
            pass
        else:
            answered_state_names.append(answer_state)
            state = states[states["state"] == answer_state].iloc[0]

            correct_answer = turtle.Turtle(visible=False)
            correct_answer.penup()
            correct_answer.speed("fastest")
            correct_answer.goto(float(state.x), float(state.y))
            correct_answer.write(arg=state.state, font=("Arial", 8, "normal"))

            score += 1
    else:
        tries -= 1
        if tries == 0:
            game_is_on = False


turtle.mainloop()