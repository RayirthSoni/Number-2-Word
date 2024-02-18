import ast

def dealing_zero_in_str(user_num_str):
    # This function removes leading zeros from the input string
    for x in user_num_str:
        if user_num_str[0] == '0':
            user_num_str = user_num_str[1:]
    return user_num_str

def get_word_for_digit(digit):
    # This function returns the word for a single digit
    return num2word[digit]

def get_word_for_tens(num):
    # This function returns the word for a number in the tens place
    if num < 20:
        return num2word[num]
    else:
        tens = num // 10 * 10
        units = num % 10
        if units:
            return num2word[tens] + '-' + num2word[units]
        else:
            return num2word[tens]

def get_word_for_hundreds(num):
    # This function returns the word for a number in the hundreds place
    hundred = num // 100
    remainder = num % 100
    if remainder:
        return num2word[hundred] + ' hundred ' + get_word_expansion(remainder)
    else:
        return num2word[hundred] + ' hundred'

def get_word_expansion(user_num, user_num_str=None):
    # This function generates the word expansion for a given number
    if user_num_str is None:
        user_num_str = str(user_num)
    
    word_expansion = ''
    
    if user_num == 0:
        return num2word[user_num]

    if user_num_str.startswith('0'):
        user_num_str = user_num_str.lstrip('0')

    # Handling billions
    if user_num >= 1000000000:
        billions = user_num // 1000000000
        remainder = user_num % 1000000000
        word_expansion += get_word_expansion(billions, str(billions)) + ' billion '
        user_num = remainder
        user_num_str = str(user_num)

    # Handling millions
    if user_num >= 1000000:
        millions = user_num // 1000000
        remainder = user_num % 1000000
        word_expansion += get_word_expansion(millions, str(millions)) + ' million '
        user_num = remainder
        user_num_str = str(user_num)

    # Handling thousands
    if user_num >= 1000:
        thousands = user_num // 1000
        remainder = user_num % 1000
        word_expansion += get_word_expansion(thousands, str(thousands)) + ' thousand '
        user_num = remainder
        user_num_str = str(user_num)

    # Handling hundreds, tens, and ones
    if user_num >= 100:
        word_expansion += get_word_for_hundreds(user_num) + ' '
    elif user_num >= 20:
        word_expansion += get_word_for_tens(user_num) + ' '
    elif user_num > 0:
        word_expansion += get_word_for_digit(user_num) + ' '

    return word_expansion.strip()

num2word = {
    # Dictionary mapping numbers to their word representations
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
}

def main():
    # Main function to get input from the user and print the word expansion
    user_num_str = input('Enter number : ')
    user_num = int(user_num_str) if isinstance(ast.literal_eval(user_num_str), int) else float(user_num_str)
    user_num = int(user_num) if user_num % 1 == 0 else float(user_num)
    user_num_str = str(user_num)
    word_expansion = get_word_expansion(user_num)
    print(f'Word Expansion = {word_expansion.capitalize()}')

if __name__ == '__main__':
    main()
