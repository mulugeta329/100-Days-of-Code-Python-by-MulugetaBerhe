import turtle
import pandas as pd

# 1. Setup Screen & Background Image
screen = turtle.Screen()
screen.title("U.S. States Game - Vector Map Engine")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# 2. Load Coordinates Dataset
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# 3. Main Game Loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    )

    # Handle Exit condition
    if answer_state is None or answer_state.title() == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states, columns=["State"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    formatted_answer = answer_state.title()

    # Verify input against dataset
    if formatted_answer in all_states and formatted_answer not in guessed_states:
        guessed_states.append(formatted_answer)
        
        # Plot state name at exact map coordinates
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_data = data[data.state == formatted_answer]
        writer.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        writer.write(formatted_answer)