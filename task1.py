# задаем 2 переменные, одна из которых будет равна 30000
x = int(input())
f = 30000
for i in range(2, x + 1):  #переменную х вводим в диапозон, которые начинает с 2 и потом это число х становится больше на 1
    if x % i == 0 and x // i < f: # и если х делится с остатком на i и х делится целочисленно на i и это меньше 30000
        print(i) # выводим переменную i
        break # завершаем работу цикла