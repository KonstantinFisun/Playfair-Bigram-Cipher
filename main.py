
def matrix(x, y, initial): # Заполнение матрицы
    return [[initial for i in range(x)] for j in range(y)]


def locindex(c, my_matrix): # Позиция буквы
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix): # i - номер строчки, j - сама строчка
        for k, l in enumerate(j): # k - номер цифры в строчке, l - сама буква
            if c == l: # Если это наша буква добавляем в списко номер строки и номер столбца и выходим
                loc.append(i)
                loc.append(k)
                return loc


# Шифрование
def encrypt(my_matrix):
    msg = str(input("Введите сообщение, которое хотите зашифровать : ")).upper().replace(" ", "")

    # Добавляем 'X' между одинаковыми буквами
    for s in range(0, len(msg) + 1, 2): # Шаг 2
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]

    # Добавляем в конец 'X', если не хватает
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'

    i = 0
    print("Зашифрованное сообщение : ", end=' ')
    while i < len(msg):
        loc_first = locindex(msg[i], my_matrix) # позиция первой буквы
        loc_second = locindex(msg[i + 1], my_matrix) # позиция второй буквы
        if loc_first[1] == loc_second[1]: # Если столбцы совпадают, заменяем на находящиеся под ними
            print("{}{}".format(my_matrix[(loc_first[0] + 1) % 5][loc_first[1]],
                                my_matrix[(loc_second[0] + 1) % 5][loc_second[1]]), end=' ')
        elif loc_first[0] == loc_second[0]: # Если столбцы совпадают, заменяем на находящиеся справа от них
            print("{}{}".format(my_matrix[loc_first[0]][(loc_first[1] + 1) % 5],
                                my_matrix[loc_second[0]][(loc_second[1] + 1) % 5]), end=' ')
        else: # заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам
            print("{}{}".format(my_matrix[loc_first[0]][loc_second[1]],
                                my_matrix[loc_second[0]][loc_first[1]]), end=' ')
        i = i + 2 # Рассматривается след пара


def decrypt(my_matrix):  # Расшифровка
    msg = str(input("Введите зашифрованный текст : ")).upper().replace(" ", "")

    print("Исходный текст : ", end=' ')
    i = 0
    while i < len(msg):
        loc_first = locindex(msg[i], my_matrix) # позиция первой буквы
        loc_second = locindex(msg[i + 1], my_matrix) # позиция второй буквы
        if loc_first[1] == loc_second[1]: # Если столбцы совпадают, заменяем на находящиеся сверху
            print("{}{}".format(my_matrix[(loc_first[0] - 1) % 5][loc_first[1]],
                                my_matrix[(loc_second[0] - 1) % 5][loc_second[1]]), end=' ')
        elif loc_first[0] == loc_second[0]: # Если столбцы совпадают, заменяем на находящиеся слева от них
            print("{}{}".format(my_matrix[loc_first[0]][(loc_first[1] - 1) % 5],
                                my_matrix[loc_second[0]][(loc_second[1] - 1) % 5]), end=' ')
        else: # заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам
            print("{}{}".format(my_matrix[loc_first[0]][loc_second[1]],
                                my_matrix[loc_second[0]][loc_first[1]]), end=' ')
        i = i + 2 # Рассматривается след пара


def main():
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
            if i == 73 and chr(74) not in result:  #
                result.append("I")
            elif i == 74:
                pass  # Ничего не выполняем
            else:
                result.append(chr(i))

    k = 0  # Счетчик идущий по result
    my_matrix = matrix(5, 5, 0)  # Матрица 5 на 5

    for i in range(0, 5):  # making matrix
        for j in range(0, 5):
            my_matrix[i][j] = result[k]
            k += 1

    while True:
        choice = int(input("\n 1.Шифрование \n 2.Расшифровка \n 3.Выход \n"))
        if choice == 1:
            encrypt(my_matrix)
        elif choice == 2:
            decrypt(my_matrix)
        elif choice == 3:
            exit()
        else:
            print("Выберите корректную цифру")


if __name__ == '__main__':
    main()
