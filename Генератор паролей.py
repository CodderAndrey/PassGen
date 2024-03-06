from random import *

while 1 > 0:
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_?'
    exc = 'il1Lo0O'
    chars = ''
    cntPw = input('Укажите количество паролей для генерации:')

    while not cntPw.isdigit():
        cntPw = input('Укажите ЧИСЛО! равное количеству паролей для генерации:')
    if int(cntPw) == 0:
        print('Вот ваш пароль состоящий из пустоты :)')
        break

    lenPw = input('Укажите длину одного ахуенного пароля:')
    while lenPw.isdigit() != True or int(lenPw) == 0:
        lenPw = input('Укажите ЧИСЛО! оличное от 0 и равное длинне паролей для генерации :')

    digOn = input('Включать ли цифры 0123456789?')
    while digOn.lower() != 'да' and digOn.lower() != 'нет':
        digOn = input('Скажите "ДА" или "НЕТ')

    ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
    while ABCon.lower() != 'да' and ABCon.lower() != 'нет':
        ABCon = input('Скажите "ДА" или "НЕТ')

    abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
    while abcOn.lower() != 'да' and abcOn.lower() != 'нет':
        abcOn = input('Скажите "ДА" или "НЕТ')

    chOn = input('Включать ли символы !#$%&*+-=?@^_? ')
    while chOn.lower() != 'да' and chOn.lower() != 'нет':
        chOn = input('Скажите "ДА" или "НЕТ')

    excOn = input('Исключать ли неоднозначные символы il1Lo0O? ')
    while excOn.lower() != 'да' and excOn.lower() != 'нет':
        excOn = input('Скажите "ДА" или "НЕТ')

    if digOn.lower() == 'да':
        chars += digits
    if ABCon.lower() == 'да':
        chars += uppercase_letters
    if abcOn.lower() == 'да':
        chars += lowercase_letters
    if chOn.lower() == 'да':
        chars += punctuation
    if excOn.lower() == 'да':
        for i in 'il1Lo0O':
            chars.replace(i, '')

    if int(cntPw) > 1:
        print('Вот пароли подходящие под ваши запросы:')
    elif int(cntPw) == 1:
        print('Вот пароль подходящий под ваши запросы:')


    def generate_password(lenPw, chars):
        password = ''
        for _ in range(int(lenPw)):
            password += choice(chars)
        return password


    for _ in range(int(cntPw)):
        print(generate_password(lenPw, chars))
