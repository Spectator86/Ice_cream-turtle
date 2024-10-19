from turtle import *

def modern_goto(x, y):
    penup()
    goto(x, y)
    pendown()

#многогранник
def draw(paths, length, color):
    #Цикл for создаёт локальную переменную i
    #После каждой итерации(повторения) i увеличивается на 1
    #Оператор in роверяет есть ли i в диапозоне который указан в поле range
    #В данном случае количество итераций равно количествву граней

    fillcolor(color)

    begin_fill()
    
    for i in range(paths):
        #Всё что указано ниже будет выполняться столько раз сколько граней указано при вызове функции
        forward(length/3)
        left(360/paths)

    end_fill()

#стаканчик
def glass(length, color):
    fillcolor(color)
    backward(length/3)

    begin_fill()

    forward(length)
    right(120)
    forward(length)
    right(120)
    forward(length)
    right(120)
    forward(length)

    end_fill()

def icecream(x, y, size, ice_cream_color, glass_color):
    modern_goto(x, y)
    
    #Функция draw принимает два аргумента
    #Первый агрумент означает число граней многогранника
    #Второй аргумент означает длину линии многогранника
    draw(10, size, ice_cream_color)

    #переход
    left(90)
    forward(size/6)
    right(90)

    glass(size, glass_color)
    

#hideturtle скрывает черепашку т.е. самой черепашки не видно, но её след видно
hideturtle()

#pensize изменяет толщину черепашки на число которое указано в аргументе
pensize(5)

icecream(0, 0, 150, "purple", "brown")

