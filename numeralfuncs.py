import dboperations

def get_roman(n):
    """
    Convert arabic numerals to roman
    Attention! No more than 3999 and not less than 1
    """

    if 1 > n or n > 3999:
        raise SyntaxError('The number is less than 1 or more than 3999')

    db_number = n  # входное значение для БД

    numbers_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                    50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = str()
    for arabic, roman in numbers_dict.items():
        result += n // arabic * roman  # данным алгоритмом мы опредяем сколько рим. чисел нужно внести в result
        n %= arabic  # не забываем вычитать из конвертируемого арабского числа

    dboperations.db_write(db_number, result)  # Запись данных в БД

    return result

#########

def get_arabic(n):
    """
    Convert roman numerals to arabic
    """

    n = n.upper()  # на случай, если пользователь введет числа в нижнем регистре
    invalid_format = ['MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII',  # список невалидных комбинаций чисел
                      'IM', 'VM', 'XM', 'LM', 'DM', 'CCM', 'CMC',
                      'ID', 'VD', 'XD', 'LD', 'CCD', 'CDC',
                      'IC', 'VC', 'XXC', 'LC', 'XCX',
                      'XXL', 'VL', 'IL', 'XLX', 'IXI',
                      'VX', 'IIX',
                      'IIV', 'IVI']

    check_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    # если встречаются посторонние символы или неправильный формат рим. чисел - бросаем ошибку
    if [True for num in n if all([num != check for check in check_list])] or any([inv in n for inv in invalid_format]):
        raise SyntaxError('Invalid roman numeral format!')

    db_number = n  # входное значение для БД

    numbers_dict = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4,
                    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    for roman, arabic in numbers_dict.items():  # перебираем элементы, вычитая их из строки и переводя в арабские числа
        for i in range(n.count(roman)):
            n = n.replace(roman, '', 1)
            result += arabic

    dboperations.db_write(db_number, result)  # Запись данных в БД

    return str(result)


