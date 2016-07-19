import turtle
from math import sin

x= str( input())

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(100)
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red", "red")
t1.shapesize(2)
t1.speed(100)

def draw_number(t,x):

    t.penup()
    t.backward(400)
    length=50
    t.penup
    for i in range(len(x)):

        if x[i]=='1':
            digit_one(t,length)
            t.forward(length/2)
        if x[i]=='2':
            digit_two(t,length)
        if x[i]=='3':
            digit_rub(t,length)
            t.penup()
            t.forward(length/2)
        if x[i]=='4':
            digit_four(t,length)
        if x[i]=='5':
            digit_five(t,length)
            t.penup()
            t.forward(length/2)
        if x[i]=='6':
            digit_six(t,length)
            t.penup()
            t.forward(length/2)
        if x[i]=='7':
            digit_seven(t,length)
        if x[i]=='8':
            digit_eight(t,length)
            t.penup()
            t.forward(length/2)
        if x[i]=='9':
            digit_nine(t,length)
            t.penup()
            t.forward(length/2)
        if x[i]=='0':
            digit_zero(t,length)
            t.penup()
            t.forward(length/2)


    t.hideturtle()
def digit_zero(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    t.penup()
    t.forward(length)
    t.pendown()
    t.left(90)
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(length/2)
        t.left(90)
  #обратный ход
    t.right(90)
    t.penup()
    t.backward(length)
def digit_one(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.left(90)
    t.forward(length)
    t.left(90+45)
    t.forward(length*sin(45*3.141592/180))
    #обратный ход
    t.backward(length*sin(45*3.141592/180))
    t.right(90+45)
    t.backward(length)
    t.right(90)
    t.penup()

def digit_two(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [180, -135, 45, 90]
    A = [ L1,   L2, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)


def digit_rub(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [45, 135,-135,135]
    A = [ L2, L1,L2, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

def digit_five(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2

    B = [0, 90, 90, -90,-90]
    A = [ L1,L1, L1, L1,L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

def digit_four(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = length
    B = [90, 180,-90,-90]
    A = [ L2, L1,L1, L1]

    t.penup()
    t.forward(L1*2)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

def digit_six(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = length
    B = [90, -90, 180, 90,90,-90,-90]
    A = [ L2,L1, L1, L1,L1,L1,L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

def digit_seven(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = length/2
    L2 = (length*sin(45*3.141592/180))
    B = [90, -45, 135]
    A = [ L1,L2, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

def digit_eight(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
    """
    L1 = length/2
    B = [0, 90, 90,90,180,0,-90,-90]
    A = [ L1,L1, L1,L1,L1,L1,L1,L1]

    t.penup()
    t.forward(L1)
    t.pendown()

    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)

    A.reverse()
    B.reverse()

    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

def digit_nine(t,length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
    """
    L1 = length/2
    L2 = (length*sin(45*3.141592/180))
    B = [45, 135, -90,-90,-90]
    A = [ L2,L1, L1,L1,L1]

    t.penup()
    t.forward(L1)
    t.pendown()

    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)

    A.reverse()
    B.reverse()

    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)

draw_number(t,x)