import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
path = "50_states.csv"
score = 0
df = pd.read_csv(path)

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{score}/50", prompt="What's another state name").title()

    def check_in_csv():
        return answer_state in df["state"].values

    if answer_state == "Exit":
        break
                
    if check_in_csv():
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        row = df[df.state == answer_state]
        tim.goto(int(row.x), int(row.y))
        tim.write(answer_state)
        score += 1


screen.exitonclick()