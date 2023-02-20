import numpy as np# Импортируем необходимые библиотеки

def guess_the_number(num:int=1) -> int:
    """Возвращает число попыток, которые требуются для угадывания заданного в параметре 'num' числа.
    
    Args:
        num (int, optional): Число в формате INT, в диапазоне [1:101].

    Returns:
        int: Корректное колл-во попыток в формате INT затраченное на угадывание программой числа.
    """
    if (num in [i for i in range(1,101)]) and (type(num) == int):#   Инициируем проверку передаваеммых аргументов.
        count = 0 #                 Создаём счётчик.
        bot_num = 1#                Инициируем изначальную нижнюю границу для  генерации рандомного числа.
        top_num = 101#              Инициируем изначальную верхнюю границу для  генерации рандомного числа. На 1 еденицу больше для корректной отработки.
        while True:
            count += 1#             В начале цикла перебора увеличиваем колл-во попыток на 1.
            tryig_num = np.random.randint(bot_num,top_num)# Генерируем рандомное число.
            if tryig_num == num:#   Проверяем угадала ли программа. 
                return count#       Если да, возвращем значение счётчика и закрываем действия функции, если нет продолжаем.
            if tryig_num > num:#    Если рандомное число точно больше искомого, заменяем верхнюю границу диапазона для рандомного числа на него.
                top_num = tryig_num
            if tryig_num < num:#    #Если рандомное число точно меньше искомого, заменяем нижнюю границу диапазона для рандомного числа на него.
                bot_num = tryig_num + 1        
    else:
        raise ValueError('В качестве аргумента допустимы только ЧИСЛА от 1 до 100')#Вызываем ошибку, если аргументы в функцию переданы неверно.


def midle_guess_the_number(guess_the_number):
    """Расчитывает среднее колл-во попыток для угадывания числа алгоритмом.

    Args:
        guess_the_number (_type_): Передаётся функция guess_the_number

    Returns:
        Возвращает среднее число, в формате int.
    """
    result_array = []#  Создаем пустой массив типа list, куда в процессе выполения кода, будут помещатся результаты каждого из выполнений скрипта.
    
    np.random.seed(1)#              Фиксируем сид для воспроизводимости
    nums_array = np.random.randint(1,101,size=1000)#    Создаём массив случайных чисел, которые будут передаваться в функцию guess_the_number) размером в 1000 значений.
    
    for num_iter in nums_array:#    Перебираем массив, заполняем result_array
        result_array.append(guess_the_number(int(num_iter)))
    res = int(np.mean(result_array))#   По факту заполнения массива, находим среднее значение колл-ва попыток и приводим его к типу INT для корректной итоговой выдачи.
    
    return res


if __name__ == '__main__':#Если скрипт запущен отдельным файлом, а не импортирован , выводим на экран результат функции "Измеритель мощности угадывателя."
    print(midle_guess_the_number(guess_the_number))

