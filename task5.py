max = -999 #делаем максимально маленькой
n = int(input())
count = 0 #вводим счетчик, который равен 0
while n != 0: #пока н не равно 0
    # если макс меньше н, то мы передаем значение числа, которое больше нового максимума
    if max < n:
        max = n
        # каунт равен 1, потому что у нас появляется новое значение максимума
        count = 1
    elif n == max: # иначе если значение н равно максу, то увеличеваем на 1
        count += 1
    n = int(input())
print(count)
