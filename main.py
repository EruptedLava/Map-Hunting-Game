try:
    import turtle
    import pandas

    FILE_NAME = "states.csv"

    ALIGNMENT = "center"
    FONT = ("Couriel", 12, "normal")

    screen = turtle.Screen()
    image = "india.gif"

    screen.title("Bharat Ko Jano")
    screen.setup(900,1000)
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv(FILE_NAME)
    all_states = data["state"].to_list()

    print(len(all_states))

    guessed_states = []

    while len(guessed_states)< 30:

        answer_state = screen.textinput(title=f"{len(guessed_states)}/30 states correct", prompt="What's the another state name??").capitalize()

        if answer_state.lower() == "exit":
            lost_states = []
            for state in all_states:
                if state not in guessed_states:
                    lost_states.append(state)
            df = pandas.DataFrame(lost_states)
            df.to_csv("States_to_learn.csv")

            break

        if answer_state in guessed_states:
            print("Don't repeate the state name it is already guessed")

        elif answer_state in all_states:
            print(answer_state)
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(answer_state,align = ALIGNMENT,font = FONT)

except Exception as e:
    print(e)
