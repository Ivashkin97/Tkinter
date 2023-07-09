#1 (код от урока 7)
#Загрузили функции модуля tkinter
from tkinter import *

#функция моргания
def toggle_eyes():
    #получаем текущий цвет заливки глаза 
    current_color = c.itemcget(eye_left,'fill')

    #меняем цвет заливки глаза
    if current_color == 'white':
        new_color = c.body_color
    else:
        new_color = 'white'
    
    #получаем текущее положение зрачка (видим/невидим)
    current_state = c.itemcget(pupil_left, 'state')

    #меняем текущее положение на противоположное
    if current_state == HIDDEN:
        new_state = NORMAL
    else:
        new_state = HIDDEN

    #меняем конфигурацию зрачка
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state = new_state)


    #меняем конфигурацию виджетов глаз
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)



    #ждем полсекунды и снова вызываем функцию перерисовки глаз
    root.after(500, toggle_eyes) 

#функция - показать счастье
def show_happy(event):
    #проверим, что координаты мышки над головой
    if (20<= event.x <= 350) and (20<= event.y <=100):
        #показываем щёчки
        c.itemconfigure(cheek_left,state=NORMAL)
        c.itemconfigure(cheek_right,state=NORMAL)
        #показываем счастливую улыбку
        c.itemconfigure(mouth_happy,state=NORMAL)
        #прячем нормальную улыбку
        c.itemconfigure(mouth_normal,state=HIDDEN)

#функция - спрятать счастье
def hide_happy(event):
    #прячем щёчки
    c.itemconfigure(cheek_left,state=HIDDEN)
    c.itemconfigure(cheek_right,state=HIDDEN)
    #прячем счастливую улыбку
    c.itemconfigure(mouth_happy,state=HIDDEN)
    #показываем нормальную улыбку
    c.itemconfigure(mouth_normal,state=NORMAL)







#запускаем tkinter и создаем окно
root = Tk()
root.title("Питомец")
#создаём холст размером 400x400 пикселей
c = Canvas(root, width=400, height=400)
#поменял цвет фона холста и ширину рамки
c.configure(bg="skyblue", highlightthickness=10)

#здест будет создан питомец
#сохраняем цвет питомца в переменную c.body_color
c.body_color = "magenta"
#рисуем тело
body = c.create_oval(35,20,365,350, outline=c.body_color,fil=c.body_color)
#рисуем левое ушко
ear_left=c.create_polygon(75,80,75,10,165,70,outline=c.body_color,\
                          fill=c.body_color)
#рисуем правое ушко
ear_right=c.create_polygon(270,45,325,10,325,77,outline=c.body_color,\
                          fill=c.body_color)
#рисуем ротик
mouth_normal=c.create_line(170,250,200,272,230,250,width=2, smooth=1)

#рисуем левую лапку
foot_left=c.create_oval(65,320,145,360,outline=c.body_color,fill=c.body_color,)

#рисуем правую лапку
foot_right=c.create_oval(250,320,330,360,outline=c.body_color,fill=c.body_color,)

#рисуем левый глазик
eye_left=c.create_oval(130,110,160,170,outline="black",fill="white")
#рисуем правый глазик
eye_right=c.create_oval(230,110,260,170,outline="black",fill="white")

#рисуем левый зрачок
pupil_left = c.create_oval(140,145,150,155,outline="black",fill="black")
#рисуем правый зрачок
pupil_right = c.create_oval(240,145,250,155,outline="black",fill="black")

#румянец
cheek_left = c.create_oval(70,180,120,230,outline='pink',fill='pink',state=HIDDEN)
cheek_right = c.create_oval(280,180,330,230,outline='pink',fill='pink',state=HIDDEN)

#счастливая улыбка
mouth_happy = c.create_line(170,250,200,282,230,250,smooth=1,width=2,state=HIDDEN)



#упорядочивает содержимое холста
c.pack()

#вызываем функцию моргания
toggle_eyes()

#связываем событие - клик мышки над головой питомца с вызовом функции - показать счастье
c.bind('<Motion>',show_happy)

#связываем событие - выход мышки за пределы окна с вызовом функции - спрятать счастье

c.bind('<Leave>',hide_happy)

#запускается функция, которая будет отслеживать события
#такие, например, как клик мышкой
root.mainloop()