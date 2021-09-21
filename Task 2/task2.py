import sys
from string import digits, ascii_lowercase

def number_from_dec(decimal_number: int, number_system_indicator: int) -> str:
    if decimal_number is None:
        raise ValueError("Decimal number is None.")

    if number_system_indicator is None:
        raise ValueError("Number system indicator is None.")

    if number_system_indicator < 1 or number_system_indicator > 36:
        raise ValueError("Number system indicator must be in range [1, 36].")

    ALPHABET = digits + ascii_lowercase

    was_negative = decimal_number < 0
    decimal_number = abs(decimal_number)
    
    result_digits = []
    while decimal_number != 0:
        result_digits.append(ALPHABET[decimal_number % number_system_indicator])
        decimal_number //= number_system_indicator
    
    if len(result_digits) < 1:
        result_digits.append(ALPHABET[0])
    
    if was_negative:
        result_digits.append('-')

    result_digits.reverse()

    return ''.join(result_digits)

def number_to_dec(number: str, number_system_indicator: int) -> int:
    if number_system_indicator < 1 or number_system_indicator > 36:
        raise ValueError("Number system indicator must be in range [1, 36].")

    number = number.lower()

    ALPHABET = (digits + ascii_lowercase)[:number_system_indicator]
    was_negative = number.startswith("-")
    
    if was_negative:
        number = number[1:]

    result = 0
    for digit in number:
        result *= number_system_indicator
        if digit not in ALPHABET:
            raise ValueError("Number has incorrect format.")
        result += ALPHABET.index(digit)

    if was_negative:
        result *= -1

    return result

def main(argv):
    cast_8_result = False
    cast_16_result = False

    while not cast_8_result and not cast_16_result:
        print("Введите число в шестнадцатеричной или восьмеричной системе счисления: ")
        raw_number = input()

        try:
            n16 = number_to_dec(raw_number, 16)
            cast_16_result = True
        except ValueError:
            pass

        try:
            n8 = number_to_dec(raw_number, 8)
            cast_8_result = True
        except ValueError:
            pass

        if not cast_8_result and not cast_16_result:
            print("Некорректный ввод, повторите попытку.")
        else:
            if cast_8_result:
                print(f"Перевод из восьмеричной системы: {n8}")
            if cast_16_result:
                print(f"Перевод из шестнадцатеричной системы: {n16}")
    
    return 0

if __name__ == "__main__":
    main(sys.argv)
