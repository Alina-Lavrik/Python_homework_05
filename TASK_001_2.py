# # 1.a. Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 117 конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

from os import system
system("cls")

from random import randint

def input_player(name):
    sweets = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while sweets < 1 or sweets > 28:
        sweets = int(input(f"{name}, введите корректное количество конфет: "))
    return sweets


def information(name, x, counter, value):
    print(f"{name} взял(a) {x} конф, всего у нее(него) {counter} конф, на столе {value} конф.")

player1 = input("Введите имя игрока 1: ")
player2 = 'Bot'
value = int(input("Введите количество конфет на столе: "))
first_player = randint(0,2) 
if first_player:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if first_player:
        x = input_player(player1)
        counter1 += x
        value -= x
        first_player = False
        information(player1, x, counter1, value)
    else:
        x = randint(1,28)
        counter2 += x
        value -= x
        first_player = True
        information(player2, x, counter2, value)

if first_player:
    print(f"Выиграл(а) {player1}")
else:
    print(f"Выиграл(а) {player2}")
