# python 3.8

def table(values=range(1, 10)):
    '''Простейшая таблица умножения
    Результаты выводит в столбик'''
    for num1 in values:
        for num2 in values:
            print(num1, 'x', num2, '=', num1 * num2)


if __name__ == '__main__':
    table()
