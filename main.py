import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_data = pd.read_csv("50_states.csv")

guessed_states = []

is_still_game = True
score = 0


def results_to_csv(guessed, states):
    size = 50
    result_states = {
        "Missing States": [],
    }
    all_states = states["state"]

    for item in all_states:
        if item not in guessed:
            result_states["Missing States"].append(item)
    user_name = screen.textinput("Enter Name", "Please enter your name:")
    result = pd.DataFrame(result_states)
    result.to_csv(f"{user_name}'s un-guessed states.csv")


def game_over():
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
    pen.goto(0, -20)
    pen.write("Please see the un-guessed.csv file for un-guessed states", align="center", font=("Arial", 15, "bold"))
    global is_still_game
    is_still_game = False
    results_to_csv(guessed_states, states_data)
    time.sleep(3)
    screen.bye()


def game_finished():
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("CONGRATULATIONS!", align="center", font=("Arial", 30, "bold"))
    pen.goto(0, 0)
    pen.write("You've guessed all of the states!", align="center", font=("Arial", 20, "bold"))
    global is_still_game
    is_still_game = False


def continue_game():
    existing_state = states_data[states_data.state == capitalized_answer]
    pen.hideturtle()
    pen.penup()
    pen.goto(existing_state["x"].item(), existing_state["y"].item())
    pen.write(capitalized_answer, align="center", font=("Arial", 10, "bold"))
    global score
    score += 1
    guessed_states.append(capitalized_answer)


title = "Guess a State"
prompt = "Input a state's name(Press Cancel to end game)"
pen = turtle.Turtle()

while is_still_game:
    if score != 0:
        title = f"{score}/50 State Guessed"
        prompt = "Input next state's name(Press Cancel to end game)"
    answer_state = screen.textinput(title, prompt)
    capitalized_answer = ""
    if not answer_state:
        game_over()
    if answer_state:
        capitalized_answer = answer_state.title()
        if states_data["state"].str.contains(capitalized_answer).any():
            continue_game()
    if len(guessed_states) == 50:
        game_finished()
