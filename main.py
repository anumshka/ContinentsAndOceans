import turtle as turtle
import time
import pandas

scr = turtle.Screen()
scr.addshape("img.gif")
turtle.shape("img.gif")
Run = True
already_done = []
while Run:
    answer = scr.textinput(title="Enter your input", prompt="Name any ocean or continent.Press Q to quit.").title()
    data = pandas.read_csv("names.csv")
    name_list = data["Location"].to_list()

    # Quitting the game and displaying all the answers
    if answer == "Q":
        not_done = []
        for names in name_list:
            if names not in already_done:
                not_done.append(names)
        for i in not_done:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            pick = data[data["Location"] == i]
            t.goto(int(pick["x"]), int(pick["y"]))
            t.write(i)
        Run = False
        break

    # Matching the input with the data
    if answer in name_list:
        # Prompting if an already entered value is entered
        if answer in already_done:
            show = turtle.Turtle()
            show.hideturtle()
            show.penup()
            show.goto(-300, -150)
            show.color("red")
            show.write("That is already done")
            time.sleep(1)
            show.clear()
        # Accepting the input if new value is entered
        else:
            already_done.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            pick = data[data["Location"] == answer]
            t.goto(int(pick["x"]), int(pick["y"]))
            t.write(answer)
    # Checking invalid inputs
    else:
        show = turtle.Turtle()
        show.hideturtle()
        show.penup()
        show.goto(-300, -150)
        show.color("red")
        show.write("Oops!You got it wrong")
        time.sleep(1)
        show.clear()

scr.exitonclick()
