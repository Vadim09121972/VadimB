n = int(input('Введите число от 3 до 20: '))
def my_parol(number):
    parol = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                parol += str(i) + str(j)
    return parol
result = my_parol(n)
print('пароль:', result)
