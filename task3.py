p = 0
u = 0
k = int(input())
while k != 0: #пока к не равно нулю, то прибавляя к мы получаем сумму чисел, т. е число п
    p += k
    u += 1 #прибавляя 1 мы получаем кол-во чисел
    k = int(input())
print(p / u) #находим среднее арифметическое 