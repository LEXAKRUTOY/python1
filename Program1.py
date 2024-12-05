import statistics

def analyze_list(lst):
        maximum = max(lst)
        minimum = min(lst)
        average = sum(lst) / len(lst)
        medium = statistics.median(lst)

        result = {
            "max" : maximum,
            "min" : minimum,
            "avg" : average,
            "med" : medium
        }
        print(result)

try:
    lst = [int(x) for x in input("Введите список чисел через пробел: ").split()]

    if len(lst) == 0:
            raise ZeroDivisionError
    else:
        analyze_list(lst)
    
except ValueError:
        print("Введены некорректные данные.")

except ZeroDivisionError:
        print("Список не должен быть пустым.")