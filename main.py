import random

# Обучающая выборка (идеальное изображение цифр от О до 9)
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')


# Список всех цифр от О до 9 в едином массиве
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

lesson_topic = 5                                # какой цифре обучаем
n_sensors = 15                                  # количество сенсоров
weights = [1 for i in range(n_sensors)]         # обнуление весов

# Функция определяет, является ли полученное изображение числом 5
# Возвращает Да, если признано, что это 5. Возвращает Нет, если отвергнуто, что это 5

def perceptron(Sensor):
    b = 7                                       # Порог функции активации
    s = 0                                       # Начальное значение суммы

    for i in range(n_sensors):                  # цикл суммирования сигналов от сенсоров
        s += int(Sensor[i]) * weights[i]

    if s >= b:
        return True                             # Сумма превысила порог
    else:
        return False                            # Сумма меньше порога


# Уменьшение значений весов. Если сеть ошиблась и выдала Да при входной цифре, отличной от пятерки
def decrease(number):
    for i in range(n_sensors):
        if int(number[i]) == 1:                 # Возбужденный ли вход
            weights[i] -= 1                     # Уменьшаем связанный с входом вес на единицу


# Увеличение значений весов. Если сеть не ошиблась и выдала Да при поданной на вход цифре 5
def increase(number):
    for i in range(n_sensors):
        if int(number[i]) == 1:                 # Возбужденный ли вход
            weights[i] += 1                     # Увеличиваем связанный с входом вес на единицу


# Тренировка сети
n = 1000                                        # Количество уроков


for i in range(100):                            # Приучаем сеть!
    j = lesson_topic
    r = perceptron(nums[j])                     # Результат обращения к сумматору (ответ - Да или Нет)

    if j == lesson_topic:                       # Если генератор выдал случайное число j, равное 5
        if r:                                   # Если сумматор сказал Да (это пятерка), j пятерка. Поощряем!
            increase(nums[j])
    else:                                       # Если генератор выдал случайное число j, равное не 5
        if r:                                   # Если сумматор сказал Да (это пятерка), j не пятерка. Наказывем!
            decrease(nums[j])



for i in range(n):
    j = random.randint(0, 9)              # Генерируем случайное число j от О до 9
    r = perceptron(nums[j])                     # Результат обращения к сумматору (ответ - Да или Нет)

    if j == lesson_topic:                       # Если генератор выдал случайное число j, равное 5
        if r:                                   # Если сумматор сказал Да (это пятерка), j пятерка. Поощряем!
            increase(nums[j])
    else:                                       # Если генератор выдал случайное число j, равное не 5
        if r:                                   # Если сумматор сказал Да (это пятерка), j не пятерка. Наказывем!
            decrease(nums[j])



# под капотом:
    # print('Lesson count = ', i)
    # print('Random value = ', j)
    # print('Weights value = ', weights)


print('===============')
print('Lesson topic: ', lesson_topic)           # тема урока (число, которое мы учимся определять)
print('Result weights:', weights)               # Вывод значений весов
print('Etalon: ', 111100111001111)
print('===============')


# ====================================================================

# проверка работы программы на обучающей выборке
print('O это 5?', perceptron(num0))
print('1 это 5?', perceptron(num1))
print('2 это 5?', perceptron(num2))
print('З это 5?', perceptron(num3))
print('4 это 5?', perceptron(num4))
print('5 это 5?', perceptron(num5))
print('б это 5?', perceptron(num6))
print('7 это 5?', perceptron(num7))
print('8 это 5?', perceptron(num8))
print('9 это 5?', perceptron(num9))