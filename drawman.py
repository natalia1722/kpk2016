from turtle import Turtle
default_scale = 10 #коэффициент масштабирования Чертежника, по умолчанию = 10
default_color = 'black' #цвет Чертежника, по умолчанию = "черный"
default_pen_size = 1 #толщина линии Чертежника, по умолчанию = 1

def init_drawman():
    """ Инициализация Чертежника"""
    global t, x_current, y_current, _drawman_scale, _drawman_pen_size
    t = Turtle()
    t.penup()
    shag = 40
    vod = 0.5
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale, shag, vod)
    drawman_pen_size(default_pen_size)
    #drawman_scale_2(shag, vod)

"""def drawman_scale_2(shag,vod):
    global _drawman_scale,
    _drawman_scale = shag/vod
    # print(_shag,_vod,_drawman_scale)
"""
def drawman_scale(scale, shag, vod):
    global _drawman_scale, _shag,_vod
    '''
    Масштаб
    shag - шаг сетки
    vod - единиц в одном делении сетки
    '''
    _shag = shag
    _vod = vod
    _drawman_scale = scale

def drawman_pen_size(pen_size):
    """Установка толщины линии Чертежника
    :param pen_size: толщина линии Чертежника, диапазон от 1 до 10
    """
    global _drawman_pen_size
    if pen_size > 10:
        _drawman_pen_size = t.pensize(10)
    elif pen_size < 1:
        _drawman_pen_size = t.pensize(1)
    else:
        _drawman_pen_size = t.pensize(pen_size)

# https://github.com/dinaflox/python0716/blob/master/drawman.py
def drawman_color(color):
    global _drawman_color
    _drawman_color = color
    t.color(color)

def test_drawman():
    """
    Тестирование работы Чертёжника
    :return: None
    """
    pen_down()
    axis()
    for i in range(5):
        on_vector(10, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)

def axis():
    global t, w, h, _drawman_scale, _vod
    t.speed(10)
    # t.turtlesize(2)
    # Вертикальные линии
    t.width(3)
    t.home()

    # Горизонтальные линии
     # t.reset()
     # t.tracer(0)
    t.color('#000000')
#
    t.write('  0,0')
#
    x = 0
    y = -10 * _shag
    coords = " " + str(x) + ", " + str(-10 * _vod)
    t.goto(x, y)
    t.write(coords)

#    Начинаем оси рисовать
    t.down()
    x=0
    y=10*_shag
    coords=str(x)+", "+str(10*_vod)
    t.goto(x, y-_shag/2)
    t.left(90)
    t.stamp()
    t.right(90)
    t.write(coords)
#
    t.up()
    x=-10*_shag
    y=0
    coords=str(-10*_vod)+", "+str(y)
    t.goto(x, y)
    t.write(coords)
#
    t.down()
    x=10*_shag
    y=0
    coords=str(10*_vod)+", "+str(y)
    t.goto(x, y)

    t.stamp()
    t.write(coords)

    pen_up()
    x_current = 0
    y_current = 0
    to_point(0, 0)

def drawman_draw_grid(color_grid):
    """
    рисует кооринтаную сетку без осей
    запоминает размер окна поля
    x_width - ширина окна поля в пикселах
    y_height - высота окна поля в пикселах
    :param color_grid: цвет линий сетки указывается пользователем Чертежника при вызове команды drawman_draw_grid(color)
    :return:
    """
    x_width = t.screen.window_width()
    y_height = t.screen.window_height()
    t.speed(25)
    drawman_draw_Hline(x_width, y_height, color_grid)
    drawman_draw_Vline(x_width, y_height, color_grid)
    pen_up()
    to_point(0, 0)
    t.speed(1)

def drawman_draw_Vline(x_width, y_height, color):
    """
    рисование линий сетки из центра поля (т.е. из начальной позиции Чертежника)
    рисует вертикальные линии сетки отельно по каждой четверти, учитывая масштабирование Четрежника
    :param color: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :param x_width: ширина окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :param y_height: высота окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :return:
    """
    x = 0
    y = 0
    t.goto(x, y)
    while x <= x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, y_height//2)
        t.penup()
        x = x + x_width//_drawman_scale

    x = 0
    y = 0
    t.goto(x, y)
    while x >= -x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, y_height//2)
        t.penup()
        x = x - x_width//_drawman_scale

    x = 0
    y = 0
    t.goto(x, y)
    while x >= -x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, -y_height//2)
        t.penup()
        x = x - x_width//_drawman_scale

    x = 0
    y = 0
    t.goto(x, y)
    while x <= x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, -y_height//2)
        t.penup()
        x = x + x_width//_drawman_scale


def drawman_draw_Hline(x_width, y_height, color):
    """
    рисование линий сетки из центра поля (т.е. из начальной позиции Чертежника)
    рисует горизонтальные линии сетки отельно по каждой четверти, учитывая масштабирование Четрежника
    :param color: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :param x_width: ширина окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :param y_height: высота окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    """
    y = 0
    x = 0
    t.goto(x, y)
    while y <= y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x_width//2, y)
        t.penup()
        y = y + y_height//_drawman_scale

    y = 0
    x = 0
    t.goto(x, y)
    while y >= -y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x_width//2, y)
        t.penup()
        y = y - y_height//_drawman_scale

    y = 0
    x = 0
    t.goto(x, y)
    while y >= -y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(-x_width//2, y)
        t.penup()
        y = y - y_height//_drawman_scale

    y = 0
    x = 0
    t.goto(x, y)
    while y <= y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(-x_width//2, y)
        t.penup()
        y = y + y_height//_drawman_scale

def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)


init_drawman()
if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(5)