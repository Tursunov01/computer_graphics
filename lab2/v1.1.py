from tkinter import *
from tkinter import messagebox
import copy
from math import cos, sin, pi, sqrt


def draw_points(points):
    
    for line in points[0]:
        canv.create_line(line)

    # эллипсы
    for oval in points[1]:
        canv.create_line(oval)


def start_points(ox, oy):
    points = [[], []]

    #left foot
    points[0].append([[567, 430], [567, 455]])
    points[0].append([[583, 430], [583, 455]])

    #right foot
    points[0].append([[555, 455], [567, 455]])
    points[0].append([[583, 455], [595, 455]])
    
    #left hand
    points[0].append([[563, 374], [563, 382]])
    points[0].append([[525, 355], [563, 374]])

    #right hand
    points[0].append([[587, 374], [587, 382]])
    points[0].append([[625, 355], [587, 374]])
    #antenn
    points[0].append([[575, 305], [590, 275]])
    points[0].append([[575, 305], [560, 275]])
    points[0].append([[560, 275], [540, 275]])
    points[0].append([[590, 275], [610, 275]])

    #smile
    points[0].append([[565, 325], [585, 325]])

    #body
    body = form_ellipse([ox, oy + 45], 30, 45)
    for i in range(len(body)):
        points[1].append(body[i])

    #face
    face = form_ellipse([ox, oy - 25], 25, 25)
    for i in range(len(face)):
        points[1].append(face[i])

    #eye
    eye1 = form_ellipse([ox + 10, oy - 30], 5, 5)
    for i in range(len(eye1)):
        points[1].append(eye1[i])

    eye2 = form_ellipse([ox - 10, oy - 30], 5, 5)
    for i in range(len(eye2)):
        points[1].append(eye2[i])

    return points


def form_ellipse(centre, a, b):
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

def transfer(dx, dy):
    stack.append(copy.deepcopy(stack[-1]))
    for form in stack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] += dx
                coord[1] += dy

    rebuild_scene()


def restart():
    canv.delete("all")
    draw_points(stack[-1])


def reset():
    stack.append(start_points(OX, OY))
    restart()


def cancel():
    if len(stack) > 1:
        stack.pop(-1)
        restart()


def zoomer(kx, ky, xc, yc):
    stack.append(copy.deepcopy(stack[-1]))
    for form in stack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] = (coord[0] - xc - OX) * kx + xc + OX
                coord[1] = (coord[1] - yc - OY) * ky + yc + OY

    restart()


def turn(xc, yc, angle):
    stack.append(copy.deepcopy(stack[-1]))
    for form in stack[-1]:
        for figure in form:
            for coord in figure:
                coord[0] -= OX
                coord[1] -= OY
                new_x = xc + (coord[0] - xc) * d_cos(angle) + (coord[1] - yc) * d_sin(angle)
                new_y = yc - (coord[0] - xc) * d_sin(angle) + (coord[1] - yc) * d_cos(angle)
                coord[0] = new_x
                coord[1] = new_y
                coord[0] += OX
                coord[1] += OY

    restart()


def d_cos(a):
    return cos(a * pi / 180)


def d_sin(a):
    return sin(a * pi / 180)


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
    if key == "Переместить":
        code, dx, dy = checker(key)
        if code == -1:
            messagebox.showerror("Ошибка!"
            , "Данные для перемещения введены неверно.\nПроверьте на правельность ввода")
            table_name1.delete(0, END)
            table_name2.delete(0, END)
            table_name1.focus_set()
            return -1
        else:
            transfer(dx, dy)
    if key == "Повернуть":
        code, c, degree = checker(key)
        if code == -1:
            messagebox.showerror("Ошибка!"
            , "Данные для поворота введены неверно.\nПроверьте на правельность ввода")
            table_name3.delete(0, END)
            table_name3.focus_set()
            return -1
        else:
            canv.delete("all")
            turn(0, 0, degree)
    if key == "Масштабирование":
        code, kx, ky = checker(key)
        if code == -1:
            messagebox.showerror("Ошибка!"
            , "Данные для масштабирования введены неверно.\nПроверьте на правельность ввода")
            table_name4.delete(0, END)
            table_name5.delete(0, END)
            table_name4.focus_set()
            return -1
        else:
            zoomer(kx, ky, 0, 0)
    if key == "Нач. состояние":
        reset()
        
    if key == "Назад":
        cancel()


# Main window
root = Tk()
root.title("grasshopper")
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

can_h = 680
can_w = 1150

OX = can_w / 2
OY = can_h / 2
stack = []

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

# Main programm
Points = start_points(OX, OY)
draw_points(Points)
stack.append(Points)

root.mainloop()
