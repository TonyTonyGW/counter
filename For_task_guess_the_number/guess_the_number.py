import numpy as np# Импортируем необходимые библиотеки

def guess_the_number(num:int=1) -> int:
    """Возвращает число попыток, которые требуются для угадывания заданного в параметре 'num' числа.
    
    Args:
        num (int, optional): Число в формате INT, в диапазоне [1:101].

    Returns:
        int: Корректное колл-во попыток в формате INT затраченное на угадывание программой числа.
    """
    if (type(num) == int) and (num >= 1 and num <= 100):#   Инициируем проверку передаваеммых аргументов.
        count = 0
        while True:
            count += 1
            tryig_num = np.random.randint(1,101)
            if tryig_num == num:
                return count
    else:
        raise ValueError('В качестве аргумента допустимы только ЧИСЛА от 1 до 100')#    Вызываем ошибку, если аргументы в функцию переданы неверно.



def midle_guess_the_number(guess_the_number):
    """Расчитывает среднее колл-во попыток для угадывания числа алгоритмом.

    Args:
        guess_the_number (_type_): Передаётся функция guess_the_number

    Returns:
        Возвращает среднее число, в формате int.
    """
    result_array = []#  Создаем пустой массив типа list, куда в процессе выполения кода, будут помещатся результаты каждого из выполнений скрипта.
    
    nums_array = np.random.randint(1,101,size=1000)#    Создаём массив случайных чисел, которые будут передаваться в функцию guess_the_number) размером в 1000 значений.
    
    for num_iter in nums_array:#    Перебираем массив, заполняем result_array
        result_array.append(guess_the_number(int(num_iter)))
    res = int(np.mean(result_array))#   По факту заполнения массива, находим среднее значение колл-ва попыток и приводим его к типу INT для корректной итоговой выдачи.
    
    return res


print(midle_guess_the_number(guess_the_number))