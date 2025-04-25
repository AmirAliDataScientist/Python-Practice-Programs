import random

print('--Welcome to the password generator--')
letter = int(input('How many letter do you want in your password : '))
symbol = int(input('How mant symbols do you want in your password : '))
num =  int(input('How many numbers you want in your code : '))

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
    '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>',
    ',', '.', '?', '/', '~', '`'
]

numbers = [0,1,2,3,4,5,6,7,8,9]

#Problem need to solve
# Generate a password in a sequence, letter, symbole, numbers, as per the user requirement.
# For ex- 4 letter, 2 symboles, 3 numbers
# x_alpha = int(input("How many letters you want in your password")
pass_letter = random.sample(alphabets, letter)
pass_symbol = random.sample(special_chars, symbol)
pass_num = [random.choice(numbers) for x in range(num)]
# pass_num = random.sample(numbers,num)

pass_word = pass_letter + pass_symbol + pass_num
random.shuffle(pass_word)


result = ''.join(map(str,(pass_word)))
print(f"Your suggested password with combination of character, symbols and number is : {result}")

