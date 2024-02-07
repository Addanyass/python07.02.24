
# zadanie 1

# def academiya(par):    #число
     

#     def number(loc):           #степень 
#         return par ** loc          # степень возводим
#     return number


# num =  int(input("введите число"))
# stepen = int(input("введите степень"))
# top = academiya(num)


# print(top(stepen))

# zadanie 2


# a = int(input("введите  число первое"))
# b = int(input("введите число второе"))

# def sum(a,b):
#     first_nim = a
#     second_num = b
#     def inner():
#         result = 0
#         for i in range(first_nim, second_num +1):
#             result += i
#         return result
#     return inner
# summa = sum(a,b)
# print(summa())




#zadanie 4

# # Создаем поле для игры
# pole_igry = [[' ']*3 for _ in range(3)]

# # Функция для отображения поля
# def otrisovka_pole(pole):
#     print('---------')
#     for i in range(3):
#         print('|', end='')
#         for j in range(3):
#             print(pole[i][j], end='|')
#         print('\n---------')

# # Функция для выбора хода игроком
# def hod_igroka(pole):
#     while True:
#         x, y = map(int, input('Введите координаты вашего хода через пробел: ').split())
#         if x < 1 or x > 3 or y < 1 or y > 3 or pole[x-1][y-1] != ' ':
#             print('Некорректный ход. Попробуйте еще раз.')
#         else:
#             pole[x-1][y-1] = 'X'
#             break

# # Функция для проверки выигрышной комбинации
# def proverka_pobedy(pole, simvol):
#     for i in range(3):
#         if pole[i][0] == pole[i][1] == pole[i][2] == simvol:
#             return True
#     for i in range(3):
#         if pole[0][i] == pole[1][i] == pole[2][i] == simvol:
#             return True
#     if pole[0][0] == pole[1][1] == pole[2][2] == simvol:
#         return True
#     if pole[0][2] == pole[1][1] == pole[2][0] == simvol:
#         return True
#     return False

# # Функция для хода компьютера
# def hod_kompyutera(pole):
#     for i in range(3):
#         for j in range(3):
#             if pole[i][j] == ' ':
#                 pole[i][j] = 'O'
#                 if proverka_pobedy(pole, 'O'):
#                     return
#                 pole[i][j] = ' '
#     for i in range(3):
#         for j in range(3):
#             if pole[i][j] == ' ':
#                 pole[i][j] = 'X'
#                 if proverka_pobedy(pole, 'X'):
#                     pole[i][j] = 'O'
#                     return
#                 pole[i][j] = ' '
#     for i in range(3):
#         for j in range(3):
#             if pole[i][j] == ' ':
#                 pole[i][j] = 'O'
#                 return

# # Основной игровой цикл
# while True:
#     otrisovka_pole(pole_igry)
#     hod_igroka(pole_igry)
#     if proverka_pobedy(pole_igry, 'X'):
#         otrisovka_pole(pole_igry)
#         print('Вы выиграли!')
#         break
#     hod_kompyutera(pole_igry)
#     if proverka_pobedy(pole_igry, 'O'):
#         otrisovka_pole(pole_igry)
#         print('Вы проиграли!')
#         break
#     if all(pole_igry[i][j] != ' ' for i in range(3) for j in range(3)):
#         otrisovka_pole(pole_igry)
#         print('Ничья!')
#         break
