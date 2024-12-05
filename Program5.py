def turple_stats(tpl):
    Sum = sum(tpl)
    Avg = sum(tpl) / len(tpl)
    Unq = tuple(set(tpl))

    result = {
        "Сумма" : Sum,
        "Среднее" : Avg,
        "Уникальные значения" : Unq 
    }
    print(result)

try:
    tpl = [int(x) for x in input("Введите кортеж чисел разделённых пробелами: ").split()]
    if len(tpl) == 0:
        raise ZeroDivisionError
    else:
        turple_stats(tpl)
except ZeroDivisionError:
    print("Числа не были введены")
except ValueError:
    print("Неккоректная информация")
