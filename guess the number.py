import numpy as np

def guess_the_number(num:int=1) -> int:
    """Возвращает число попыток, которые требуются для угадывания заданного в параметре 'num' числа.
    
    Args:
        num (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    if num >= 1 and num <= 100:
        count = 0
        while True:
            count += 1
            tryig_num = np.random.randint(1,101)
            if tryig_num == num:
                return count
    else:
        raise ValueError('Допустипый диапазон значение от 1 до 100')



def midle_guess_the_number(guess_the_number):
    """Расчитывает среднее колл-во попыток для угадывания числа

    Args:
        guess_the_number (_type_): Передаётся функция guess_the_number

    Returns:
        Возвращает среднее число, в формате int.
    """
    result_array = []
    
    nums_array = np.random.randint(1,101,size=1000)
    
    for num_iter in nums_array:
        result_array.append(guess_the_number(num_iter))
    res = int(np.mean(result_array))
    
    return res
