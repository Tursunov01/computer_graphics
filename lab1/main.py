from tkinter import *
from tkinter import messagebox
from itertools import permutations, combinations
from math import *
import numpy

#Оформление окна
root = Tk()
root.title("Triangle")
root.geometry("450x400+450+10")
root.resizable(False, False)
root.iconbitmap("triangle.ico")




#Заголовок

head = Label(text = "Ввод данных", font = "Helvetica 20 bold")
head.grid(row = 0, column = 0, pady = 10)


a1 = Label(text = "Введите количество точек", font = "consolas 8 ")
a1.grid(row = 1, column = 0, pady = 0, padx = 10, sticky = W)
table_name1 = Entry(root, width = 10)
table_name1.grid(row = 2, padx = 15, column = 0, pady = 0, sticky = W)
table_name1.focus_set()


a2 = Label(text = "Введите координаты точек для множества",font = "consolas 8 ")
a2.grid(row = 1, column = 1, pady = 5, padx = 10, sticky = W)
table_name2 = Entry(root, width = 38)
table_name2.grid(row = 2, padx = 15, column = 1, pady = 10, sticky = W)
##table_name2.config(state = "readonly")

#Menu




mainmenu = Menu(root)
root.config(menu = mainmenu)

usermenu = Menu(mainmenu, tearoff = 0)

mainmenu.add_cascade(label = "Действия")
mainmenu.add_command(label = "Справка")

def check_size(n):
    if n.isdigit() == False:
        if n == "":
            return 0
        else:
            return -1

def check_point(points, n):
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"}
    count = 0
    for i in points:
        a = set(i)
        if i.isalpha() == True or a.issubset(numbers) == False:
            return -1
        else:
            count += 1
    if count / 2 != n:
        return -2
    return 0

def compare(num1, num2):
    eps = 1e-7
    if abs(num1 - num2) < eps:
        return 1
    else:
        return 0


def exist(x1, y1, x2, y2, x3, y3):
    if ((compare(x1, x2) and compare(y1, y2)) or
            (compare(x1, x3) and compare(y1, y3)) or
            (compare(x2, x3) and compare(y2, y3)) or
            (compare(x1, y1) and compare(x2, y2) and compare(x3, y3)) or
            (compare(((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)), 0))):
        return 0
    else:
        return 1

def calculate_lenght(x1, y1, x2, y2, x3, y3):
    a = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    b = sqrt(pow((x3 - x2), 2) + pow((y3 - y2), 2))
    c = sqrt(pow((x1 - x3), 2) + pow((y1 - y3), 2))
    return a, b, c

def find_triangle(arrx, arry):
    coordinates = []
    area = []
    for i in range(0, len(arrx)):
        q = (str(arrx[i]), str(arry[i]))
        coordinates.append(q)
    combo = [x for x in combinations(coordinates, 3)]
    i = 0
    while i < len(combo):
        current = list(combo[i])
        point1 = list(current[0])
        point2 = list(current[1])
        point3 = list(current[2])

        x1 = float(point1[0])
        y1 = float(point1[1])
        x2 = float(point2[0])
        y2 = float(point2[1])
        x3 = float(point3[0])
        y3 = float(point3[1])

        if exist(x1, y1, x2, y2, x3, y3):
            a, b, c = calculate_lenght(x1, y1, x2, y2, x3, y3)
            p = (a + b + c) / 2
            r = sqrt((p - a) * (p - b) * (p - c) / p)
            R = (a * b * c) / (4 * sqrt(p * (p - a) * (p - b) * (p - c))) 
            s = pi * pow(r, 2)
            S = pi * pow(R, 2)
            area.append(S - s)
            area.append(i)
            area.append(R)
            area.append(r)
            i += 1
        else:
            del combo[i]
    if len(area) != 0:
         max_area = max(area)
         for i in range(0, len(area), 4):
             if compare(area[i], max_area) != 0:
                 return 0, area[i + 1], max_area, combo, area[i + 2], area[i + 3] 
         
    else:
        return -1, -1, -1, []


def circle_center(x1, y1, x2, y2, x3, y3):
##    a_x = (x1 + x2) / 2
##    a_y = (y1 + y2) / 2
##    b_x = (x2 + x3) / 2
##    b_y = (y2 + y3) / 2
##    c_x = (x1 + x3) / 2
##    c_y = (y1 + y3) / 2
##
##    if x2 - x1 != 0:
##        a_angle = (y2 - y1) / (x2 - x1)
##        if a_angle != 0:
##            a_alpha = -1 / a_angle
##            if a_angle == 0:
##                M1 = numpy.array([[1, -1 * b_alpha], [1, -1 * c_alpha]])
##                V1 = numpy.array([b_y - b_alpha * b_x, c_y - c_alpha * c_x])
##                return numpy.linalg.solve(M1, V1)
##    if x3 - x2 != 0:
##        b_angle = (y3 - y2) / (x3 - x2)
##        if b_angle != 0:
##             b_alpha = -1 / b_angle
##             if b_angle == 0:
##                M1 = numpy.array([[1, -1 * a_alpha], [1, -1 * c_alpha]])
##                V1 = numpy.array([a_y - a_alpha * a_x, c_y - c_alpha * c_x])
##                return numpy.linalg.solve(M1, V1)
##    if x1 - x3 != 0:
##        c_angle = (y1 - y3) / (x1 - x3)
##        if c_angle != 0:
##            c_alpha = -1 / c_angle
##            if c_angle == 0:
##                M1 = numpy.array([[1, -1 * a_alpha], [1, -1 * b_alpha]])
##                V1 = numpy.array([a_y - a_alpha * a_x, b_y - b_alpha * b_x])
##                return numpy.linalg.solve(M1, V1)
    
    c, a, b = calculate_lenght(x1, y1, x2, y2, x3, y3)

    x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    y = (a * y1 + b * y2 + c * y3) / (a + b + c)
    return x, y
    
    
    

def center_opis_okr(x1, y1, x2, y2, x3, y3):
    M1 = numpy.array([[2 * (x2 - x1), 2 * (y2 - y1)], [2 * (x2 - x3), 2 * (y2 - y3)]])
    V1 = numpy.array([pow(x2, 2) - pow(x1, 2) + pow(y2, 2) - pow(y1, 2), pow(x2, 2) - pow(x3, 2) + pow(y2, 2) - pow(y3, 2)])
    return numpy.linalg.solve(M1, V1)



def add_p(key, table_name3, window):
    if key == "Добавить":
        point = (table_name3.get()).split()
        if check_point(point, 1) == -1:
            messagebox.showerror("Ошибка!"
                , "Введены недопустимые символы.\nКоординаты должны принадлежать множеству вещественных чисел")
            table_name3.delete(0, END)
            table_name3.focus_set()
            return -1
        if check_point(point, 1) == -2:
            messagebox.showerror("Ошибка!"
                , "Надо ввести координаты одной точки")
            return -1
        else:
            table_name2.insert(END, " ")
            table_name2.insert(END, point[0])
            table_name2.insert(END, " ")
            table_name2.insert(END, point[1])
            n = table_name1.get()
            if n == "":
                n = 1
            else:
                n = int(table_name1.get())
                n += 1
            table_name1.delete(0, END)
            table_name1.insert(END, n)
            
        window.destroy()

def del_p(key, table_name4, window):
    n = table_name1.get()
    coordinates = (table_name2.get()).split()
    if n == "" or len(coordinates) == 0:
        messagebox.showerror("Ошибка!"
            , "Одно из полей пустое.\nПроверьте на правельность ввода")
        return -1
    if key == "Удалить":
        point = (table_name4.get()).split()
        if check_point(point, 1) == -1:
            messagebox.showerror("Ошибка!"
                , "Введены недопустимые символы.\nКоординаты должны принадлежать множеству вещественных чисел")
            table_name4.delete(0, END)
            table_name4.focus_set()
            window.destroy()
            return -1
        if check_point(point, 1) == -2:
            messagebox.showerror("Ошибка!"
                , "Надо ввести координаты одной точки")
            window.destroy()
            return -1
        else:
            if check_point(coordinates, int(n)) == -1:
                messagebox.showerror("Ошибка!"
                    , "Введены недопустимые символы.\nКоординаты должны принадлежать множеству вещественных чисел")
                table_name2.delete(0, END)
                table_name2.focus_set()
                window.destroy()
                return -1
            if check_point(coordinates, int(n)) == -2:
                messagebox.showerror("Ошибка!"
                   , "Число пар координат не соответствует введенному количеству")
                window.destroy()
                return -1
            else:
                if n == "" or len(coordinates) == 0:
                    messagebox.showerror("Ошибка!"
                    , "Вы пытаетесь удалить несуществующую точку")
                    window.destroy()
                    return -1
                if int(n) * 2 == len(coordinates):
                    for i in range(0, len(coordinates) - 1):
                        if float(point[0]) == float(coordinates[i]):
                            if float(point[1]) == float(coordinates[i + 1]) and i % 2 == 0:
                                del coordinates[i]
                                del coordinates[i]
                                table_name2.delete(0, END)
                                n = int(n) - 1
                                for i in range(0, len(coordinates)):
                                    table_name2.insert(END, coordinates[i])
                                    table_name2.insert(END, " ")
                                table_name1.delete(0, END)
                                table_name1.insert(END, n)
                                window.destroy()
                                return 0
                    messagebox.showerror("Ошибка!"
                    , "Вы пытаетесь удалить несуществующую точку")
                    window.destroy()
                    return -1
                else:
                    messagebox.showerror("Ошибка!"
                    , "Пары координат не соответствует количеству точек")
                    window.destroy()
                    return -1

def get_data():
        arrx = []
        arry = []
        n = table_name1.get()
        if check_size(n) == -1:
            messagebox.showerror("Ошибка!"
                , "Введены недопустимые символы.\nКоличество должно целым положительным числом")
            table_name1.delete(0, END)
            table_name1.focus_set()
            return -1, arrx, arry
        else:
            if n == "":
                n = 0
            else:
                n = int(n)
        points = (table_name2.get()).split()
        if check_point(points, n) == -1:
            messagebox.showerror("Ошибка!"
                , "Введены недопустимые символы.\nКоординаты должны принадлежать множеству вещественных чисел")
            table_name2.delete(0, END)
            table_name2.focus_set()
            return -1, arrx, arry
        if check_point(points, n) == -2:
            messagebox.showerror("Ошибка!"
                , "Число пар координат не соответствует введенному количеству")
            return -1, arrx, arry
        else:
            
            for i in range(0, n * 2):
                if i % 2 == 0:
                    arrx.append(float(points[i]))
                else:
                    arry.append(float(points[i]))
            return 0, arrx, arry

def options(key):
    arrx = []
    arry = []
    code, arrx, arry = get_data()
    if key == "Вычислить" and code == 0:
        code, pos, max_area, combo, R, r = find_triangle(arrx, arry)
        if code == 0:
            current = list(combo[pos])
            point1 = list(current[0])
            point2 = list(current[1])
            point3 = list(current[2])

            x1 = point1[0]
            y1 = point1[1]
            x2 = point2[0]
            y2 = point2[1]
            x3 = point3[0]
            y3 = point3[1]
            root = Tk()
            root.title("Результаты")
            root.geometry("400x200")
            text = Text(root, state = NORMAL)
            text.insert(1.0, str(max_area))
            text.insert(1.0, ")\nимеет наибольшую разность площадей окружности,\nвписанной и описанной около треугольника.\nМаксимальная площадь равна = ")
            text.insert(1.0, str(y3))
            text.insert(1.0, " ")
            text.insert(1.0, str(x3))
            text.insert(1.0, ")\nC = (")
            text.insert(1.0, str(y2))
            text.insert(1.0, " ")
            text.insert(1.0, str(x2))
            text.insert(1.0, ")\nB = (")
            text.insert(1.0, str(y1))
            text.insert(1.0, " ")
            text.insert(1.0, str(x1))
            text.insert(0.0, "Треугольник с точками:\nA = (")
            text.pack()
            root.mainloop()
            return -1
        else:
            messagebox.showinfo("Внимание!"
                , "Что то пошло не так.\nВведенные координаты не составляют какой либо треугольник.\nПроверьте на правельность ввода")
            return -1
            
    if key == "Удалить все точки" and code == 0:
        if len(arrx) == 0:
            messagebox.showinfo("Предукреждение!"
                , "Одно из полей пустое.\nПроверьте на правельность ввода")
            return -1
        messagebox.showinfo("Справка!", "Координаты все точек были удалены!")
        table_name2.delete(0, END)
        table_name1.delete(0, END)
        table_name2.focus_set()
    if key == "Добавить точку" and code == 0:
        window = Tk()
        window.geometry("200x100+450+10")
        window.resizable(False, False)
        window.iconbitmap("triangle.ico")
        a3 = Label(window, text = "Введите координаты точки", font = "consolas 8 ")
        a3.grid(row = 0, column = 0, pady = 5, padx = 15, sticky = W)
        table_name3 = Entry(window, width = 10)
        table_name3.grid(row = 1, padx = 15, column = 0, pady = 5, sticky = W)
        table_name3.focus_set()
        add1 = lambda x = "Добавить": add_p(x, table_name3, window)
        button5 = Button(window, text = "Добавить", width = 10, height = 1, font = "consolas 10 bold", bg="white",fg="#000080", command = add1)
        button5.grid(row = 2, column = 0, pady = 5, padx = 15, sticky = W)
    if key == "Удалить точку" and code == 0:
        if len(arrx) == 0:
            messagebox.showerror("Ошибка!"
                , "Одно из полей пустое.\nПроверьте на правельность ввода")
            return -1
        window = Tk()
        window.geometry("200x110+450+10")
        window.resizable(False, False)
        window.iconbitmap("triangle.ico")
        a4 = Label(window, text = "Введите координаты удаляемой \nточки", font = "consolas 8 ")
        a4.grid(row = 0, column = 0, pady = 5, padx = 0, sticky = W)
        table_name4 = Entry(window, width = 10)
        table_name4.grid(row = 1, padx = 15, column = 0, pady = 5, sticky = W)
        table_name4.focus_set()
        del_1 = lambda x = "Удалить": del_p(x, table_name4, window)
        button5 = Button(window, text = "Удалить", width = 10, height = 1, font = "consolas 10 bold", bg="white",fg="#000080", command = del_1)
        button5.grid(row = 2, column = 0, pady = 5, padx = 15, sticky = W)
    if key == "Показать точки" and code == 0:
        draw = Tk()
        draw.resizable(False, False)
        draw.geometry("+300+10")
        canv = Canvas(draw, width=1000, height=600, bg="lightblue", cursor="pencil")
        canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
        canv.create_line(0, 300, 1000, 300, width=2, arrow=LAST)
        start = -500
        m = -24
        p = 25
        for i in range(40000):
            if i % 800 == 0:
                n = start + (1 / 40) * i
                canv.create_line(n + 500, -3 + 300, n + 500, 3 + 300
                                 , width=0.5, fill='black')
                canv.create_text(n + 515, -10 + 300, text=str(m)
                                 , fill="purple", font=("Helvectica", "5"))
                m += 1
                if (n != 0):
                    canv.create_line(-3 + 500, n + 300, 3 + 500, n + 300
                                     , width=0.5, fill='black')
                    if p == 0:
                        p = -1
                    canv.create_text(20 + 500, n + 300, text=str(p)
                                    , fill="purple", font=("Helvectica", "5"))
                    p -= 1
                    
        for i in range(len(arrx)):
            canv.create_oval(arrx[i] * 20 + 500, 300 - arry[i] * 20
                             , arrx[i] * 20 + 501, 301 - arry[i] * 20
                             , width=5, outline="red")
        canv.pack()
        draw.mainloop()
    if key == "Показать рисунок" and code == 0:
        code, pos, max_area, combo, R, r = find_triangle(arrx, arry)
        if code == 0:
            current = list(combo[pos])
            point1 = list(current[0])
            point2 = list(current[1])
            point3 = list(current[2])

            x1 = float(point1[0])
            y1 = float(point1[1])
            x2 = float(point2[0])
            y2 = float(point2[1])
            x3 = float(point3[0])
            y3 = float(point3[1])
            draw = Tk()
            draw.resizable(False, False)
            draw.geometry("+300+10")
            canv = Canvas(draw, width=1000, height=600, bg="lightblue", cursor="pencil")
            canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
            canv.create_line(0, 300, 1000, 300, width=2, arrow=LAST)
            canv.create_polygon(((x1 * 20) + 500, 300 - (y1 * 20))
                            , ((x2 * 20) + 500, 300 - (y2 * 20)),
                            ((x3 * 20) + 500, 300 - (y3 * 20))
                            , fill="lightgreen", outline="black", width=2)
            start = -500
            m = -24
            p = 25
            for i in range(40000):
                if i % 800 == 0:
                    n = start + (1 / 40) * i
                    canv.create_line(n + 500, -3 + 300, n + 500, 3 + 300
                                 , width=0.5, fill='black')
                    canv.create_text(n + 515, -10 + 300, text=str(m)
                                 , fill="purple", font=("Helvectica", "5"))
                    m += 1
                    if (n != 0):
                        canv.create_line(-3 + 500, n + 300, 3 + 500, n + 300
                                     , width=0.5, fill='black')
                        if p == 0:
                            p = -1
                        canv.create_text(20 + 500, n + 300, text=str(p)
                                    , fill="purple", font=("Helvectica", "5"))
                        p -= 1
                       

            x_m, y_m = circle_center(x1, y1, x2, y2, x3, y3)
            canv.create_oval(x_m * 20 - r * 20 + 500, 300 - y_m * 20 - r * 20, x_m * 20 + r * 20 + 500
                             , 300 - y_m * 20 + r * 20
                             , width = 2, outline = "orange")
            opis = center_opis_okr(x1, y1, x2, y2, x3, y3)
            canv.create_oval(float(opis[0]) * 20 - R * 20 + 500, 300 - float(opis[1]) * 20 - R * 20, float(opis[0]) * 20 + R * 20 + 500
                        , 300 - float(opis[1]) * 20 + R * 20
                        , width = 2, outline = "red")

            canv.pack()
            draw.mainloop()
            
        else:
            messagebox.showinfo("Внимание!"
                , "Что то пошло не так.\nВведенные координаты не составляют какой либо треугольник.\nПроверьте на правельность ввода")
            return -1   

            
        

show_points = lambda x = "Показать точки": options(x)
del_all_points = lambda x = "Удалить все точки": options(x)
del_one_point = lambda x = "Удалить точку": options(x)
add_point = lambda x = "Добавить точку": options(x)
check_n = lambda x = "Вычислить": options(x)
show_pic = lambda x = "Показать рисунок": options(x)




button1 = Button(text = "Показать точки", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = show_points)
button1.grid(row = 5, column = 0, pady = 20, padx = 10, sticky = W)

button2 = Button(text = "Удалить все точки", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = del_all_points)
button2.grid(row = 5, column = 1, pady = 20, padx = 0, sticky = W)

button3 = Button(text = "Удалить точку", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = del_one_point)
button3.grid(row = 6, column = 0, pady = 20, padx = 10, sticky = W)

button4 = Button(text = "Добавить точку", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = add_point)
button4.grid(row = 6, column = 1, pady = 20, padx = 0, sticky = W)

button3 = Button(text = "Вычислить", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = check_n)
button3.grid(row = 7, column = 0, pady = 20, padx = 10, sticky = W)

button4 = Button(text = "Показать рисунок", width = 20, height = 2, font = "consolas 10 bold", bg="white",fg="#000080", command = show_pic)
button4.grid(row = 7, column = 1, pady = 20, padx = 0, sticky = W)

    
        


