#2йэтап

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']  # список удвоили, чтобы при использовании букв в слове из конца алфавита, при большом шаге кода переключиться на начало алфавита

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text,
            shift_amount):  # Создаем функцию с необходимыми параметрами. будет приравнивать аргументы (inputs от юзера) к параметрам этой функции
    cipher_text = ""  # создаем переменную, пока пустой закодированный текст, который далее будем наполнять
    for letter in plain_text:  # для каждой буквы из выбранного слова
        position = alphabet.index(
            letter)  # определяем позицию при помощи функции index из выше указанного Алфавита. Позиция определяется для каждой буквы при помощи loop.
        new_position = position + shift_amount  # новая позиция назначается прибавлением шага от юзера, который он вводит через input shift. Новая позиция определяется для каждой буквы при помощи loop.
        new_letter = alphabet[new_position]  # создается новая буква с учетом новой позиции в алфавите
        cipher_text += new_letter  # формируем закодированное слово исходя из новых букв
    print(f"The encoded text is {cipher_text}")  # выводим новое слово


def decrypt(cipher_text, shift_amount):  # создаем декодирующую функцию
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount  # т.к. нам нужно отсчитать шаги обратно, используем вычитание
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


if direction == "encode":  # в зависимости от выбора юзера, вызывается определенная функция
    encrypt(plain_text=text, shift_amount=shift)

elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

#3йэтапОбъединяем2функции


def caesar(direction, text, shift):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            cipher_text += alphabet[new_position]
        print(f"The decoded text is {cipher_text}")


caesar(direction, text, shift)

#Или


def caesar(start_text, shift_amount,
           cipher_direction):  # будет объединять 2 функции и выбор юзера по кодированию или раскодированию.
    end_text = ""
    if cipher_direction == "decode":  # перенесли наверх, чтобы выполнялось действие только для decode
        shift_amount *= -1
    for letter in start_text:  # это будет выполняться для encode. А для decode это будет выполняться с показателем shift_amount *= -1
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#ФИНАЛ

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']  # список удвоили, чтобы при использовании букв в слове из конца алфавита, при большом шаге кода переключиться на начало алфавита


def caesar(start_text, shift_amount,
           cipher_direction):  # будет объединять 2 функции и выбор юзера по кодированию или раскодированию.
    end_text = ""
    if cipher_direction == "decode":  # перенесли наверх, чтобы выполнялось действие только для decode.
        shift_amount *= -1  # Shift amount преобретает отрицательное число и код смещается влево
    for char in start_text:
        if char in alphabet:  # если буквы в выбранном слове присутсвуют в алфавите, то дальше идут действия
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char  # если символов нет в алфавите, то финальный результат их берет из выбранного слова не изменяя
    print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo

print(logo)

should_end = False  # создаем переменную для while loop
while not should_end:  # пока should_end не является true, опрос юзера возобновляется каждый раз. всё нижнее помещается в эту while loop.

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # Если юзер ввел 45, то модуль будет 45 - 26(кол-во букв в алфавите) = 19. На столько шагов от первой буквы переместится зашифрованная буква

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")  # вводим новый опрос
    if restart == "no":  # если пользователь выбрал NO
        should_end = True  # should_and становится True и while loop прекращается.
        print("Goodbye")




