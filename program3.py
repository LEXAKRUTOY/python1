def average_grade(student_grades):
    return sum(student_grades) / len(student_grades)        
try:
    student_name = input("Введите имя студента: ")
    student_age = int(input("Введите возраст студента: "))
    student_grades = [int(x) for x in input("Введите список оценок через пробел: ").split()]
    
    average = average_grade(student_grades)  
    
    student = {
    "Имя студента" : student_name,
    "Возраст студента" : student_age,
    "Оценки" : student_grades,
    "Средняя оценка" : average
    }
    print(student)
    if len(student_grades) == 0:
            raise ZeroDivisionError  
except ValueError:
        print("Введены некорректные данные.")
except ZeroDivisionError:
        print("Студент отчислен")