#добавляем подсчет бонусов
#змейка врезается в бортик и умирает
#змейка пересекла саму себя и умерла
from tkinter import *
from time import *
from random import *

def draw_circle(x, y, r, color):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)

def draw_field():
    canvas.create_rectangle(0, 0, 1000, 600, fill="sienna")
    canvas.create_rectangle(25, 25, 975, 575, fill="green")

def draw_snake():
    i = 0
    while i < len(table_x):
        draw_circle(table_x[i], table_y[i], 25, "gold")
        i+= 1

def draw_bonus():
    draw_circle(xb, yb, 25, "red") #нарисовали бонус

def draw_count():
    Label(canvas, text = count).place(x=950, y=50)

def draw_all():
    draw_field()#рисуем поле
    draw_snake()#рисуем змею
    draw_bonus()#рисуем бонус
    draw_count()#выводим кол-во съеденых бонусов
    sleep(0.3)
    canvas.update()
#    canvas.delete("all")

def left(event):
    global vx, vy
    vx = -1
    vy = 0

def right(event):
    global vx, vy
    vx = 1
    vy = 0

def up(event):
    global vx, vy
    vx = 0
    vy = -1

def down(event):
    global vx, vy
    vx = 0
    vy = 1

def game_over():
    draw_field()
    draw_snake()
    draw_bonus()
    draw_count()
    canvas.update()
    Label(canvas, text = "Game over!", bg="red", font=24).place(x=450, y=0)


#основная программа
window = Tk()
window.title('Змейка')
canvas = Canvas(window, width=1000, height=600)
canvas.pack()

window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)

table_x = [300, 350, 400, 450]
table_y = [100, 100, 100, 100]

xb = 500
yb = 300

vx = -1
vy = 0

#пока змейка не съела ни одного бонуса
count = 0

#змейка пока не врезалась в себя
flag = False
while True:
    #змейка врезалась в бортик
    if (table_x[0] == 50) and (vx == -1):
        break
    else:
        if (table_x[0] == 950) and (vx == 1):
            break
        else:
            if (table_y[0] == 50) and (vy == -1):
                break
            else:
                if (table_y[0] == 550) and (vy == 1):
                    break

    #пересчитываем координаты змейки
    table_x.insert(0, table_x[0] + vx*50)
    table_y.insert(0, table_y[0] + vy*50)

    #если змейка съела бонус, то в случайном месте поля появляется новый,
    #при этом последний кружок змейкине удаляется - змейка растет

    if (table_x[0] == xb) and (table_y[0] == yb):
        #случайные координаты бонуса
        xb, yb = randrange(50, 950, 50), randrange(50, 550, 50)

        count += 1

    else:
        table_x.pop()
        table_y.pop()
    
    #проверяем, что змейка врезалась в себя
    for i in range(1, len(table_x)):
        if (table_x[0] == table_x[i]) and (table_y[0] == table_y[i]):
            flag = True
            break

    if flag:
        break
    else:
        draw_all()

game_over()

window.mainloop()