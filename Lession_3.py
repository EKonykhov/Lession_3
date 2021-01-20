#=====#1===== Пришлось поразмыслить как избавиться от None )))

def x(*args):

    try:
        x1 = int(input("Укажите первое значение: "))
        x2 = int(input("Укажите второе значение: "))
        x = round(x1 / x2, 2)

    except ZeroDivisionError:
        return ("Делить на ноль нельзя!")

    return (f'Ваш результат равен: {x}')

print(x())


#=====#2=====

def x(**kwargs):
    # y = (f"name: {name}," + " " + f"surname: {surname}," + " " + f"date_of_birth: {date_of_birth},"
    # + " " + f"place_of_residence: {place_of_residence}," + " " + f"email: {email},"
    # + " " + f"telephone: {telephone}")
    return print(list(kwargs.items()))

def y():
    x(name=input("Введите имя:"),
    surname=input("Введите фамилию:"),
    date_of_birth=input("Введите дату рождения:"),
    place_of_residence=input("Введите место проживания:"),
    email=input("Введите е-мейл:"),
    telephone= input("Введите телефон:"))

y()


#=====#3=====

def my_func(*args):

    x1 = int(input("Введите первое число: "))
    x2 = int(input("Введите второе число: "))
    x3 = int(input("Введите третее число: "))

    x = [x1, x2, x3]
    x.remove(min(x))
    return print(sum(x))

my_func()


#=====#4=====

def my_func(*args):

    print("Внимание! Формула составлена для расчета отрицательного возведения в степень,"
          "поэтому при вводе второго числа не обязательно ставить минус!")

    x1 = int(input("Введите первое число: "))
    x2 = int(input("Введите второе число: "))

    x = 1 / x1 ** abs(x2)

    return print(x)

my_func()


#=====#5=====

def x():
    y = 0
    while True:
        n = 0
        z = input('Введите число или <Q> для выхода: ').split()
        for i in z:
            try:
                if i.upper() == 'Q':
                    print(f'Итоговая сумма по выходу:[{y}]')
                    return
                else:
                    y += int(i)
                    n += int(i)
            except ValueError:
                print("ВВЕДИТЕ ЧИСЛО!!! ИЛИ СИМВОЛ <q> для выхода!!!")
                break
        print(f'сумма последний ряд:[{n}]')
        print(f'сумма:[{y}]')
x()


#=====#6=====

def x():

    while True:
        z = input("Введите любое предложение: ")
        for i in z:
            z = z.lower()
            z = z.title()
            print(f'Ваше предложение преобразовано:[{z}]')
            return

x()