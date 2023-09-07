
str0 = '  0 1 2'
str1 = '0 ? ? ?'
str2 = '1 ? ? ?'
str3 = '2 ? ? ?'
print(str0)
print(str1)
print(str2)
print(str3, end = '\n\n')



i = 1

while True:

    if i % 2 != 0 or i == 1:
        hod = list(map(int, input('Ходит "крестик". Введите координаты через пробел: '). split( )))
        if  hod[0] < 0 or hod[0] > 2 or hod[1] < 0 or hod[1] > 2:
            hod = list(map(int, input('Вы вышли за пределы поля. Введите новые координаты через пробел: ').split()))
        if hod[0] == 0:
            if hod[1] == 0:
                if str1[2] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 1:
                if str1[4] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 2:
                if str1[6] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
        if hod[0] == 1:
            if hod[1] == 0:
                if str2[2] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 1:
                if str2[4] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 2:
                if str2[6] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
        if hod[0] == 2:
            if hod[1] == 0:
                if str3[2] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 1:
                if str3[4] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 2:
                if str3[6] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
        if len(hod) != 2:
            hod = list(map(int, input('Введите два числа. Введите новые координаты через пробел: ').split()))
        if type(hod[0]) != int or type(hod[1]) != int:
            hod = list(map(int, input('Введите целые значения. Введите новые координаты через пробел: ').split()))
    elif i % 2 == 0:
        hod = list(map(int, input('Ходит "нолик". Введите координаты через пробел: '). split( )))
        if  hod[0] < 0 or hod[0] > 2 or hod[1] < 0 or hod[1] > 2:
            hod = list(map(int, input('Вы вышли за пределы поля. Введите новые координаты через пробел: ').split()))
        if hod[0] == 0:
            if hod[1] == 0:
                if str1[2] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 1:
                if str1[4] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 2:
                if str1[6] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
        if hod[0] == 1:
            if hod[1] == 0:
                if str2[2] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 1:
                if str2[4] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 2:
                if str2[6] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
        if hod[0] == 2:
            if hod[1] == 0:
                if str3[2] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 1:
                if str3[4] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
            if hod[1] == 2:
                if str3[6] != '?':
                    hod = list(map(int, input('Клетка занята. Введите новые координаты через пробел: ').split()))
        if len(hod) != 2:
            hod = list(map(int, input('Введите два числа. Введите новые координаты через пробел: ').split()))
        if type(hod[0]) != int or type(hod[1]) != int:
            hod = list(map(int, input('Введите целые значения. Введите новые координаты через пробел: ').split()))


    if hod[0] == 0:
        if hod[1] == 0:
            if i % 2 != 0 or i == 1:
                str1 = str1[:2] + 'x' + str1[3:]
            elif i % 2 == 0:
                str1 = str1[:2] + 'o' + str1[3:]
        if hod[1] == 1:
            if i % 2 != 0 or i == 1:
                str1 = str1[:4] + 'x' + str1[5:]
            elif i % 2 == 0:
                str1 = str1[:4] + 'o' + str1[5:]
        if hod[1] == 2:
            if i % 2 != 0 or i == 1:
                str1 = str1[:6] + 'x'
            elif i % 2 == 0:
                str1 = str1[:6] + 'o'

    if hod[0] == 1:
        if hod[1] == 0:
            if i % 2 != 0 or i == 1:
                 str2 = str2[:2] + 'x' + str2[3:]
            elif i % 2 == 0:
                str2 = str2[:2] + 'o' + str2[3:]
        if hod[1] == 1:
            if i % 2 != 0 or i == 1:
                str2 = str2[:4] + 'x' + str2[5:]
            elif i % 2 == 0:
                str2 = str2[:4] + 'o' + str2[5:]
        if hod[1] == 2:
            if i % 2 != 0 or i == 1:
                str2 = str2[:6] + 'x'
            elif i % 2 == 0:
                str2 = str2[:6] + 'o'

    if hod[0] == 2:
        if hod[1] == 0:
            if i % 2 != 0 or i == 1:
                str3 = str3[:2] + 'x' + str3[3:]
            elif i % 2 == 0:
                str3 = str3[:2] + 'o' + str3[3:]
        if hod[1] == 1:
            if i % 2 != 0 or i == 1:
                str3 = str3[:4] + 'x' + str3[5:]
            elif i % 2 == 0:
                str3 = str3[:4] + 'o' + str3[5:]
        if hod[1] == 2:
            if i % 2 != 0 or i == 1:
                str3 = str3[:6] + 'x'
            elif i % 2 == 0:
                str3 = str3[:6] + 'o'
    print(str0)
    print(str1)
    print(str2)
    print(str3, end='\n\n')

    i += 1

    if i >= 5:
        if (str1[2] == str1[4] == str1[6] == 'x') or (str2[2] == str2[4] == str2[6] == 'x') or (str3[2] == str3[4] == str3[6] == 'x') or (str1[2] == str2[2] == str3[2] == 'x') or (str1[4] == str2[4] == str3[4] == 'x') or (str1[6] == str2[6] == str3[6] == 'x') or (str1[2] == str2[4] == str3[6] == 'x') or (str1[6] == str2[4] == str3[2] == 'x'):
            print ("Крестик выиграл")
            break
        elif (str1[2] == str1[4] == str1[6] == 'o') or (str2[2] == str2[4] == str2[6] == 'o') or (str3[2] == str3[4] == str3[6] == 'o') or (str1[2] == str2[2] == str3[2] == 'o') or (str1[4] == str2[4] == str3[4] == 'o') or (str1[6] == str2[6] == str3[6] == 'o') or (str1[2] == str2[4] == str3[6] == 'o') or (str1[6] == str2[4] == str3[2] == 'o'):
            print ("Нолик выиграл")
            break
        else:
            continue





