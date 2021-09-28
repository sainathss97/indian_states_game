import turtle
import pandas as pd
data = pd.read_csv('28_states.csv')
screen =  turtle.Screen()
screen.title("Guess The States")
state_list = data['state'].to_list()
image = "india_outline.gif"
screen.screensize(800,1500)
screen.register_shape(image)
turtle.shape(image)

tim = turtle.Turtle('circle')
tim.penup()
tim.hideturtle()
guess =[]
for _ in range(len(state_list)):
    answer = screen.textinput(title=f'Guess the State remaing{len(guess)}/{len(state_list)}',prompt="Enter the state").title()


    if answer in state_list:
        x = float(data[data['state'] == answer]['x'])
        y = float(data[data['state'] == answer]['y'])
        tim.goto(x,y)
        tim.dot()
        tim.write(answer,align ='center')
        guess.append(answer)
        screen.title(f"remaing{len(guess)}/{len(state_list)}")
    elif answer =='Stop' or answer =='Exit':
        break
        exit()
turtle.clear()
missing =[]
for sta in state_list:
    if sta not in guess:
        missing.append(sta)
print(f"You have to learn remaing : {len(missing)}")
missing_states = pd.Series(missing)
missing_states.to_csv('learn_states.csv')
turtle.mainloop()
#screen.exitonclick()