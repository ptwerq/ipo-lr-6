import random  # подключаем модуль для случайных чисел

# создаём список из 25 случайных чисел от -50 до 50
numbers = []
for i in range(25):
    numbers.append(random.randint(-50, 50))

# выводим сам список
print("Список чисел:", numbers)

# создаём счётчики
plus = 0
minus = 0
zero = 0

# считаем, сколько каких чисел
for n in numbers:
    if n > 0:
        plus += 1
    elif n < 0:
        minus += 1
    else:
        zero += 1

# общее количество
total = len(numbers)

# считаем проценты
p_plus = plus / total * 100
p_minus = minus / total * 100
p_zero = zero / total * 100

# выводим результаты
print("\nПоложительных чисел:", plus, f"({p_plus:.1f}%)")
print("Отрицательных чисел:", minus, f"({p_minus:.1f}%)")
print("Нулей:", zero, f"({p_zero:.1f}%)")

# выводим самое большое и самое маленькое число
print("\nМаксимальное число:", max(numbers))
print("Минимальное число:", min(numbers))