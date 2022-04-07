def matrix(x, y, initial):  # Заполнение матрицы
    return [[initial for i in range(x)] for j in range(y)]


def locindex(c, my_matrix):  # Позиция буквы
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):  # i - номер строчки, j - сама строчка
        for k, l in enumerate(j):  # k - номер цифры в строчке, l - сама буква
            if c == l:  # Если это наша буква добавляем в списко номер строки и номер столбца и выходим
                loc.append(i)
                loc.append(k)
                return loc


# Шифрование на латиницу
def encrypt_english(my_matrix):
    msg = str(input("Введите сообщение, которое хотите зашифровать : ")).upper().replace(" ", "")

    # Добавляем 'X' между одинаковыми буквами
    for s in range(0, len(msg) + 1, 2):  # Шаг 2
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]

    # Добавляем в конец 'X', если не хватает
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'

    i = 0
    print("Зашифрованное сообщение : ", end=' ')
    while i < len(msg):
        loc_first = locindex(msg[i], my_matrix)  # позиция первой буквы
        loc_second = locindex(msg[i + 1], my_matrix)  # позиция второй буквы
        if loc_first[1] == loc_second[1]:  # Если столбцы совпадают, заменяем на находящиеся под ними
            print("{}{}".format(my_matrix[(loc_first[0] + 1) % 5][loc_first[1]],
                                my_matrix[(loc_second[0] + 1) % 5][loc_second[1]]), end='')
        elif loc_first[0] == loc_second[0]:  # Если столбцы совпадают, заменяем на находящиеся справа от них
            print("{}{}".format(my_matrix[loc_first[0]][(loc_first[1] + 1) % 5],
                                my_matrix[loc_second[0]][(loc_second[1] + 1) % 5]), end='')
        else:  # заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам
            print("{}{}".format(my_matrix[loc_first[0]][loc_second[1]],
                                my_matrix[loc_second[0]][loc_first[1]]), end='')
        i = i + 2  # Рассматривается след пара


def decrypt_english(my_matrix):  # Расшифровка латиницы
    msg = str(input("Введите зашифрованный текст : ")).upper().replace(" ", "")

    print("Исходный текст : ", end=' ')
    i = 0
    while i < len(msg):
        loc_first = locindex(msg[i], my_matrix)  # позиция первой буквы
        loc_second = locindex(msg[i + 1], my_matrix)  # позиция второй буквы
        if loc_first[1] == loc_second[1]:  # Если столбцы совпадают, заменяем на находящиеся сверху
            print("{}{}".format(my_matrix[(loc_first[0] - 1) % 5][loc_first[1]],
                                my_matrix[(loc_second[0] - 1) % 5][loc_second[1]]), end='')
        elif loc_first[0] == loc_second[0]:  # Если столбцы совпадают, заменяем на находящиеся слева от них
            print("{}{}".format(my_matrix[loc_first[0]][(loc_first[1] - 1) % 5],
                                my_matrix[loc_second[0]][(loc_second[1] - 1) % 5]), end='')
        else:  # заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам
            print("{}{}".format(my_matrix[loc_first[0]][loc_second[1]],
                                my_matrix[loc_second[0]][loc_first[1]]), end='')
        i = i + 2  # Рассматривается след пара


# Шифрование на кириллицу
def encrypt_russian(my_matrix):
    msg = str(input("Введите сообщение, которое хотите зашифровать : ")).upper().replace(" ", "")

    # Добавляем 'Ь' между одинаковыми буквами
    for s in range(0, len(msg) + 1, 2):  # Шаг 2
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'Ь' + msg[s + 1:]

    # Добавляем в конец 'Ь', если не хватает
    if len(msg) % 2 != 0:
        msg = msg[:] + 'Ь'

    i = 0
    print("Зашифрованное сообщение : ", end=' ')
    while i < len(msg):
        loc_first = locindex(msg[i], my_matrix)  # позиция первой буквы
        loc_second = locindex(msg[i + 1], my_matrix)  # позиция второй буквы
        if loc_first[1] == loc_second[1]:  # Если столбцы совпадают, заменяем на находящиеся под ними
            print("{}{}".format(my_matrix[(loc_first[0] + 1) % 8][loc_first[1]],
                                my_matrix[(loc_second[0] + 1) % 8][loc_second[1]]), end=' ')
        elif loc_first[0] == loc_second[0]:  # Если столбцы совпадают, заменяем на находящиеся справа от них
            print("{}{}".format(my_matrix[loc_first[0]][(loc_first[1] + 1) % 4],
                                my_matrix[loc_second[0]][(loc_second[1] + 1) % 4]), end=' ')
        else:  # заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам
            print("{}{}".format(my_matrix[loc_first[0]][loc_second[1]],
                                my_matrix[loc_second[0]][loc_first[1]]), end=' ')
        i = i + 2  # Рассматривается след пара


def decrypt_russian(my_matrix):  # Расшифровка на кириллицу
    msg = str(input("Введите зашифрованный текст : ")).upper().replace(" ", "")

    print("Исходный текст : ", end=' ')
    i = 0
    while i < len(msg):
        loc_first = locindex(msg[i], my_matrix)  # позиция первой буквы
        loc_second = locindex(msg[i + 1], my_matrix)  # позиция второй буквы
        if loc_first[1] == loc_second[1]:  # Если столбцы совпадают, заменяем на находящиеся сверху
            print("{}{}".format(my_matrix[(loc_first[0] - 1) % 8][loc_first[1]],
                                my_matrix[(loc_second[0] - 1) % 8][loc_second[1]]), end=' ')
        elif loc_first[0] == loc_second[0]:  # Если столбцы совпадают, заменяем на находящиеся слева от них
            print("{}{}".format(my_matrix[loc_first[0]][(loc_first[1] - 1) % 4],
                                my_matrix[loc_second[0]][(loc_second[1] - 1) % 4]), end=' ')
        else:  # заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам
            print("{}{}".format(my_matrix[loc_first[0]][loc_second[1]],
                                my_matrix[loc_second[0]][loc_first[1]]), end=' ')
        i = i + 2  # Рассматривается след пара


def matrix_english():
    # Убираем пробелы и в верхний регистр
    key = input("Введите ключ : ").replace(" ", "").upper()  # Ключевое слово

    result = list()  # Список из букв ключевого слова
    # Заменим букву J на I (Объединим в одну ячейку), попутно создадим список из key
    for c in key:
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)

    # Добавим в наш result остальные символы
    for i in range(65, 91):
        if chr(i) not in result:  # Если символа нет в нашем списке
            if i == 73 and chr(74) not in result:
                result.append("I")
            elif i == 74:
                pass  # Ничего не выполняем
            else:
                result.append(chr(i))

    k = 0  # Счетчик идущий по result
    my_matrix = matrix(5, 5, 0)  # Матрица 5 на 5

    for i in range(0, 5):
        for j in range(0, 5):
            my_matrix[i][j] = result[k]
            k += 1

    return my_matrix


def matrix_russian():
    # Убираем пробелы и в верхний регистр
    key = input("Введите ключ : ").replace(" ", "").upper()  # Ключевое слово

    result = list()  # Список из букв ключевого слова
    # Заменим букву J на I (Объединим в одну ячейку), попутно создадим список из key
    for c in key:
        if c not in result:
            if c == 'Ъ':
                result.append('Ь')
            else:
                result.append(c)

    # Добавим в наш result остальные символы
    for i in range(1040, 1073):
        if chr(i) not in result:  # Если символа нет в нашем списке
            if i == 1066 and chr(1068) not in result:
                result.append("Ь")
            elif i == 1066:
                pass  # Ничего не выполняем
            elif i == 1046:
                result.append('Ё')
                result.append(chr(i))
            else:
                result.append(chr(i))

    k = 0  # Счетчик идущий по result
    my_matrix = matrix(4, 8, 0)  # Матрица 8 на 4

    for i in range(0, 8):
        for j in range(0, 4):
            my_matrix[i][j] = result[k]
            k += 1
    return my_matrix


def main():
    while True:
        language = int(input("1. Русский \n2. Английский \n"))
        if language == 1:
            matrix_rus = matrix_russian()
            print(matrix_rus)
            while True:
                choice = int(input("\n1.Шифрование \n2.Расшифровка \n3.Выход \n"))
                if choice == 1:
                    encrypt_russian(matrix_rus)
                elif choice == 2:
                    decrypt_russian(matrix_rus)
                elif choice == 3:
                    exit()
                else:
                    print("Выберите корректную цифру")

        elif language == 2:
            matrix_eng = matrix_english()
            while True:
                choice = int(input("\n1.Шифрование \n2.Расшифровка \n3.Выход \n"))
                if choice == 1:
                    encrypt_english(matrix_eng)
                elif choice == 2:
                    decrypt_english(matrix_eng)
                elif choice == 3:
                    exit()
                else:
                    print("Выберите корректную цифру")

        else:
            print("Выберите корректную цифру")


if __name__ == '__main__':
    main()
