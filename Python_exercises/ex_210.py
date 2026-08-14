n = int(input("Введіть число: "))

if 1 <= n <=100:
    summa=0

    for i in range(1, n+1):
        summa += i

    print(summa)
else: 
    print("Допустиме число <= 100")

#знов використала джерело, иноді не розумію як реалізувати в код
