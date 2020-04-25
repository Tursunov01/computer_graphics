from tkinter import *
from tkinter import messagebox
from math import *
import copy

#Оформление окна
root = Tk()
root.title("Triangle")
root.geometry("150x680+1150+10")
root.resizable(False, False)

draw = Tk()
draw.title("Triangle")
draw.geometry("1150x680+0+10")
draw.resizable(False, False)

canv = Canvas(draw, width=1150, height=680, bg="lightgrey", cursor="pencil")
canv.grid(row = 0, column = 0, sticky = W)

head1 = Label(text = "Меню", font = "Helvetica 18 bold")
head1.grid(row = 0, column = 0 ,pady = 10, sticky = W, columnspan = 2)

table_name1 = Entry(root, width = 8)
table_name1.grid(row = 1, column = 0, padx = 3 ,pady = 5, sticky = W, columnspan = 2)
table_name1.focus_set()

head1 = Label(text = "dx", font = "Helvetica 10 bold")
head1.grid(row = 1, column = 1 ,pady = 10, sticky = W, padx = 10)

table_name2 = Entry(root, width = 8)
table_name2.grid(row = 2, column = 0, padx = 3 ,pady = 10, sticky = W, columnspan = 2)

head1 = Label(text = "dy", font = "Helvetica 10 bold")
head1.grid(row = 2, column = 1 ,pady = 10, sticky = W, padx = 10)

table_name3 = Entry(root, width = 8)
table_name3.grid(row = 4 ,column = 0, padx = 3 ,pady = 10, sticky = W, columnspan = 2)

head1 = Label(text = "degree", font = "Helvetica 10 bold")
head1.grid(row = 4, column = 1 ,pady = 10, sticky = W, padx = 10)

table_name4 = Entry(root, width = 8)
table_name4.grid(row = 6, column = 0, padx = 3 ,pady = 5, sticky = W, columnspan = 2)

head = Label(text = "kx", font = "Helvetica 10 bold")
head.grid(row = 6, column = 1 ,pady = 10, sticky = W, padx = 10)

table_name5 = Entry(root, width = 8)
table_name5.grid(row = 7, column = 0, padx = 3 ,pady = 10, sticky = W, columnspan = 2)

head1 = Label(text = "ky", font = "Helvetica 10 bold")
head1.grid(row = 7, column = 1 ,pady = 10, sticky = W, padx = 10)


ActionsStack = []



def draw_points(points):
    for oval in points[1]:
        canv.create_line(oval, fill="black", width=2)
        
        
def get_ellipse(centre, a, b):
    ellipse = []
    num = 200
    step = abs(a) * 2 / num

    for i in range(num):
        x = -a + step * i
        y = sqrt((1 - (x ** 2) / (a ** 2)) * b ** 2)
        x1 = -a + step * (i + 1)
        y1 = sqrt((1 - (x1 ** 2) / (a ** 2)) * b ** 2)
        ellipse.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])
    for i in range(num):
        x = -a + step * i
        y = -sqrt((1 - (x ** 2) / (a ** 2)) * b ** 2)
        x1 = -a + step * (i + 1)
        y1 = -sqrt((1 - (x1 ** 2) / (a ** 2)) * b ** 2)
        ellipse.append([[x + centre[0], y + centre[1]], [x1 + centre[0], y1 + centre[1]]])
    return ellipse

def get_default_points(xc, yc):
    points = [[], []]
    body = get_ellipse([xc, yc + 45], 30, 45)
    for i in range(len(body)):
        points[1].append(body[i])
    face = get_ellipse([xc, yc - 25], 25, 25)
    for i in range(len(face)):
        points[1].append(face[i])

    eye1 = get_ellipse([xc + 10, yc - 30], 5, 5)
    for i in range(len(eye1)):
        points[1].append(eye1[i])

    eye2 = get_ellipse([xc - 10, yc - 30], 5, 5)
    for i in range(len(eye2)):
        points[1].append(eye2[i])
    return points

def mover(dx, dy, kx, ky, xc, yc, angle, xc1, yc1):
    #голова
##    canv.create_oval(  xc + kx *((xc1 + (550 - xc1) * cos(angle) + (290 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (550 - xc1) * sin(angle) + (290 - yc1) * cos(angle)) + dy - yc)
##                     , xc + kx *((xc1 + (600 - xc1) * cos(angle) + (340 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (600 - xc1) * sin(angle) + (340 - yc1) * cos(angle)) + dy - yc), outline="black", fill="lightgreen", width=2)
    #тело
##    canv.create_oval(  xc + kx *((xc1 + (545 - xc1) * cos(angle) + (340 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (545 - xc1) * sin(angle) + (340 - yc1) * cos(angle)) + dy - yc)
##                     , xc + kx *((xc1 + (605 - xc1) * cos(angle) + (430 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (605 - xc1) * sin(angle) + (430 - yc1) * cos(angle)) + dy - yc), outline="black", fill="lightgreen", width=2)
    #левая нога
    draw_points(ActionsStack[-1])
    canv.create_line(  xc + kx *((xc1 + (567 - xc1) * cos(angle) + (430 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (567 - xc1) * sin(angle) + (430 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (567 - xc1) * cos(angle) + (455 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (567 - xc1) * sin(angle) + (455 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    
    canv.create_line(  xc + kx *((xc1 + (583 - xc1) * cos(angle) + (430 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (583 - xc1) * sin(angle) + (430 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (583 - xc1) * cos(angle) + (455 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (583 - xc1) * sin(angle) + (455 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    #правая нога
    canv.create_line(  xc + kx *((xc1 + (555 - xc1) * cos(angle) + (455 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (555 - xc1) * sin(angle) + (455 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (567 - xc1) * cos(angle) + (455 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (567 - xc1) * sin(angle) + (455 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)

    canv.create_line(  xc + kx *((xc1 + (583 - xc1) * cos(angle) + (455 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (583 - xc1) * sin(angle) + (455 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (595 - xc1) * cos(angle) + (455 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (595 - xc1) * sin(angle) + (455 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    ##левая рука
    canv.create_line(  xc + kx *((xc1 + (563 - xc1) * cos(angle) + (374 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (563 - xc1) * sin(angle) + (374 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (563 - xc1) * cos(angle) + (382 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (563 - xc1) * sin(angle) + (382 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (525 - xc1) * cos(angle) + (355 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (525 - xc1) * sin(angle) + (355 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (563 - xc1) * cos(angle) + (374 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (563 - xc1) * sin(angle) + (374 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    ##правая рука
    canv.create_line(  xc + kx *((xc1 + (587 - xc1) * cos(angle) + (374 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (587 - xc1) * sin(angle) + (374 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (587 - xc1) * cos(angle) + (382 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (587 - xc1) * sin(angle) + (382 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (625 - xc1) * cos(angle) + (355 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (625 - xc1) * sin(angle) + (355 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (587 - xc1) * cos(angle) + (374 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (587 - xc1) * sin(angle) + (374 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
##    ## правый глаз
##    canv.create_oval(  xc + kx *((xc1 + (580 - xc1) * cos(angle) + (305 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (580 - xc1) * sin(angle) + (305 - yc1) * cos(angle)) + dy - yc)
##                     , xc + kx *((xc1 + (590 - xc1) * cos(angle) + (315 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (590 - xc1) * sin(angle) + (315 - yc1) * cos(angle)) + dy - yc), outline="black", fill="black", width=1)
##    ## левый глаз
##    canv.create_oval(  xc + kx *((xc1 + (560 - xc1) * cos(angle) + (305 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (560 - xc1) * sin(angle) + (305 - yc1) * cos(angle)) + dy - yc)
##                     , xc + kx *((xc1 + (570 - xc1) * cos(angle) + (315 - yc1) * sin(angle)) + dx - xc)
##                     , yc + ky *((yc1 - (570 - xc1) * sin(angle) + (315 - yc1) * cos(angle)) + dy - yc), outline="black", fill="black", width=1)
##    антенна
    canv.create_line(  xc + kx *((xc1 + (575 - xc1) * cos(angle) + (305 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (575 - xc1) * sin(angle) + (305 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (590 - xc1) * cos(angle) + (275 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (590 - xc1) * sin(angle) + (275 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    
    canv.create_line(  xc + kx *((xc1 + (575 - xc1) * cos(angle) + (305 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (575 - xc1) * sin(angle) + (305 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (560 - xc1) * cos(angle) + (275 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (560 - xc1) * sin(angle) + (275 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    
    canv.create_line(  xc + kx *((xc1 + (560 - xc1) * cos(angle) + (275 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (560 - xc1) * sin(angle) + (275 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (540 - xc1) * cos(angle) + (275 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (540 - xc1) * sin(angle) + (275 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    
    canv.create_line(  xc + kx *((xc1 + (590 - xc1) * cos(angle) + (275 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (590 - xc1) * sin(angle) + (275 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (610 - xc1) * cos(angle) + (275 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (610 - xc1) * sin(angle) + (275 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)
    
##  улыбка  
    canv.create_line(  xc + kx *((xc1 + (565 - xc1) * cos(angle) + (325 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (565 - xc1) * sin(angle) + (325 - yc1) * cos(angle)) + dy - yc)
                     , xc + kx *((xc1 + (585 - xc1) * cos(angle) + (325 - yc1) * sin(angle)) + dx - xc)
                     , yc + ky *((yc1 - (585 - xc1) * sin(angle) + (325 - yc1) * cos(angle)) + dy - yc), fill="black", width=2)


def replace(dx, dy):
    global ActionsStack 
    ActionsStack.append(copy.deepcopy(ActionsStack[-1]))
    for form in ActionsStack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] += dx
                coord[1] += dy

def zoomer(kx, ky):
    global ActionsStack 
    ActionsStack.append(copy.deepcopy(ActionsStack[-1]))
    for form in ActionsStack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] = xc + kx * (coord[0] - xc)
                coord[1] = yc + ky * (coord[1] - yc)

def turn(angle):
    global ActionsStack
    ActionsStack.append(copy.deepcopy(ActionsStack[-1]))
    for form in ActionsStack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] -= 0
                coord[1] -= 0
                new_x = xc + (coord[0] - xc) * cos(angle * pi / 180) + (coord[1] - yc) * sin(angle * pi / 180)
                new_y = yc - (coord[0] - xc) * sin(angle * pi / 180) + (coord[1] - yc) * cos(angle * pi / 180)
                coord[0] = new_x
                coord[1] = new_y
                coord[0] += 0
                coord[1] += 0

def check_point(data):
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "."}
    for i in range(0, len(data)):
        a = set(data[i])
        if data[i].isalpha() == True or a.issubset(numbers) == False:
            return -1
    return 0

def checker(key):
    if key == "Переместить":
        dx1 = table_name1.get()
        dy1 = table_name2.get()
        if dx1 == "" and dy1 != "":
            dx1 = 0
            code = check_point(dy1)
            if code == 0:
                dy1 = float(dy1)
                return 0, dx1, dy1
            else:
                return -1, -1, -1
        if dy1 == "" and dx1 != "":
            dy1 = 0
            code = check_point(dx1)
            if code == 0:
                dx1 = float(dx1)
                return 0, dx1, dy1
            else:
                return -1, -1, -1
        if dy1 == "" and dx1 == "":
            dy1 = 0
            dx1 = 0
            return 0, dx1, dy1
        if dy1 != "" and dx1 != "":
            code = check_point(dx1)
            if code == 0:
                dx1 = float(dx1)
                code = check_point(dy1)
                if code == 0:
                    dy1 = float(dy1)
                    return 0, dx1, dy1
                else:
                    return -1, -1, -1
            else:
                return -1, -1, -1
    if key == "Повернуть":
        degree1 = table_name3.get()
        code = check_point(degree1)
        if code == 0:
            degree1 = float(degree1)
            return 0, -1, degree1
        else:
            return -1, -1, -1
    if key == "Масштабирование":
        kx1 = table_name4.get()
        ky1 = table_name5.get()
        if kx1 == "" and ky1 != "":
            kx1 = 1
            code = check_point(ky1)
            if code == 0:
                ky1 = float(ky1)
                return 0, kx1, ky1
            else:
                return -1, -1, -1
        if ky1 == "" and kx1 != "":
            ky1 = 1
            code = check_point(kx1)
            if code == 0:
                kx1 = float(kx1)
                return 0, kx1, ky1
            else:
                return -1, -1, -1
        if ky1 == "" and kx1 == "":
            ky1 = 1
            kx1 = 1
            return 0, kx1, ky1
        if ky1 != "" and kx1 != "":
            code = check_point(kx1)
            if code == 0:
                kx1= float(kx1)
                code = check_point(ky1)
                if code == 0:
                    ky1 = float(ky1)
                    return 0, kx1, ky1
                else:
                    return -1, -1, -1
            else:
                return -1, -1, -1


def options(key):
    global m_x, m_y, z_x, z_y, xc, yc, sum_degree, keys, dx, dy, kx, ky, degree
    if key == "Переместить":
        keys.append(key)
        code, dx, dy = checker(key)
        if code == -1:
            messagebox.showerror("Ошибка!"
            , "Данные для перемещения введены неверно.\nПроверьте на правельность ввода")
            table_name1.delete(0, END)
            table_name2.delete(0, END)
            table_name1.focus_set()
            return -1
        else:
            canv.delete("all")
            m_x += dx
            m_y += dy
            replace(dx, dy)
            if z_x == 1 and z_y == 1 and sum_degree == 0:
                mover(m_x, m_y, 1, 1, 0, 0, 0, 0, 0)
            elif z_x == 1 and z_y == 1 and sum_degree != 0:
                angle = (sum_degree * pi) / 180
                mover(m_x, m_y, 1, 1, 0, 0, angle, xc, yc)
            elif (z_x != 1 or z_y != 1) and sum_degree == 0:
                mover(m_x, m_y, z_x, z_y, xc, yc, 0, 0, 0)
            elif (z_x != 1 or z_y != 1) and sum_degree != 0:
                angle = (sum_degree * pi) / 180
                mover(m_x, m_y, z_x, z_y, xc, yc, angle, xc, yc)
    if key == "Повернуть":
        keys.append(key)
        code, c, degree = checker(key)
        if code == -1:
            messagebox.showerror("Ошибка!"
            , "Данные для поворота введены неверно.\nПроверьте на правельность ввода")
            table_name3.delete(0, END)
            table_name3.focus_set()
            return -1
        else:
            canv.delete("all")
            sum_degree += degree
            angle = (sum_degree * pi) / 180
            turn(angle)
            if z_x == 1 and z_y == 1:
                mover(m_x, m_y, 1, 1, 0, 0, angle, xc, yc)
            else:
                mover(m_x, m_y, z_x, z_y, xc, yc, angle, xc, yc)
            return 0
    if key == "Масштабирование":
        keys.append(key)
        code, kx, ky = checker(key)
        if code == -1:
            messagebox.showerror("Ошибка!"
            , "Данные для масштабирования введены неверно.\nПроверьте на правельность ввода")
            table_name4.delete(0, END)
            table_name5.delete(0, END)
            table_name4.focus_set()
            return -1
        else:
            z_x *= kx
            z_y *= ky
            zoomer(kx, ky)
            canv.delete("all")
            angle = (sum_degree * pi) / 180
            if sum_degree == 0:
                mover(m_x, m_y, z_x, z_y, xc, yc, 0, 0, 0)
            else:
                mover(m_x, m_y, z_x, z_y, xc, yc, angle, xc, yc)
    if key == "Нач. состояние":
        keys = []
        canv.delete("all")
        mover(0, 0, 1, 1, 0, 0, 0, 0, 0)
        m_x = 0
        m_y = 0
        z_x = 1
        z_y = 1
        sum_degree = 0
    if key == "Назад":
        if len(keys) != 0: 
            canv.delete("all")
            back = keys[len(keys) - 1]
            if back == "Переместить":
                del keys[len(keys) - 1]
                m_x -= dx
                m_y -= dy
                if z_x == 1 and z_y == 1 and sum_degree == 0:
                    mover(m_x, m_y, 1, 1, 0, 0, 0, 0, 0)
                elif z_x == 1 and z_y == 1 and sum_degree != 0:
                    angle = (sum_degree * pi) / 180
                    mover(m_x, m_y, 1, 1, 0, 0, angle, xc, yc)
                elif (z_x != 1 or z_y != 1) and sum_degree == 0:
                    mover(m_x, m_y, z_x, z_y, xc, yc, 0, 0, 0)
                elif (z_x != 1 or z_y != 1) and sum_degree != 0:
                    angle = (sum_degree * pi) / 180
                    mover(m_x, m_y, z_x, z_y, xc, yc, angle, xc, yc)
            if back == "Масштабирование":
                del keys[len(keys) - 1]
                z_x /= kx
                z_y /= ky
                angle = (sum_degree * pi) / 180
                if sum_degree == 0:
                    mover(m_x, m_y, z_x, z_y, xc, yc, 0, 0, 0)
                else:
                    mover(m_x, m_y, z_x, z_y, xc, yc, angle, xc, yc)
            if back == "Повернуть":
                del keys[len(keys) - 1]
                sum_degree -= degree
                angle = (sum_degree * pi) / 180
                if z_x == 1 and z_y == 1:
                    mover(m_x, m_y, 1, 1, 0, 0, angle, xc, yc)
                else:
                    mover(m_x, m_y, z_x, z_y, xc, yc, angle, xc, yc)



move = lambda x = "Переместить": options(x)
scale = lambda x = "Повернуть": options(x)
zoom = lambda x = "Масштабирование": options(x)
back = lambda x = "Назад": options(x)
start = lambda x = "Нач. состояние": options(x)




button1 = Button(text = "Переместить", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = move)
button1.grid(row = 3, column = 0, pady = 10 ,sticky = W, columnspan = 2)

button2 = Button(text = "Повернуть", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = scale)
button2.grid(row = 5, column = 0, pady = 10 ,sticky = W, columnspan = 2)

button3 = Button(text = "Масштабирование", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = zoom)
button3.grid(row = 8, column = 0, pady = 10 ,sticky = W, columnspan = 2)

button4 = Button(text = "Назад", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = back)
button4.grid(row = 9, column = 0, pady = 10 ,sticky = W, columnspan = 2)

button5 = Button(text = "Нач. состояние", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = start)
button5.grid(row = 10, column = 0, pady = 10 ,sticky = W, columnspan = 2)


m_x = 0
m_y = 0
z_x = 1
z_y = 1
xc = 575
yc = 340
sum_degree = 0
keys = []
dx = 0
dy = 0
kx = 1
ky = 1
degree = 0
Points = get_default_points(575, 340)
draw_points(Points)
ActionsStack.append(Points)
mover(0, 0, 1, 1, 0, 0, 0, 0, 0)

root.mainloop()

    
        


