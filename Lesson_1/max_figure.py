# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = -1
while user_number <= 0:
    user_number = int(input("Введите целое положительное число:"))

n = int(1)
max_figure = int(0)

while n <= int(len(str(user_number))):

    a = int((user_number % (10 ** n)) // (10 ** (n - 1)))
    if a >= max_figure:
        max_figure = a
        n = n + 1
    # print(user_number, max_figure, n-1)
    else:
        n = n + 1
    # print(user_number, max_figure, n - 1)

print(f"Максимальная цифра в числе: {max_figure}")
