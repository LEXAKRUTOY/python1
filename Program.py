import random

A = int(input("Введите число: "))
B = []
C = range(10)

for _ in C:
    D = random.randint(1,10)
    B.append(D)

if A in B:
    print("Число есть в массиве")
else:
    print("Числа нет в массиве")
    
print(B)