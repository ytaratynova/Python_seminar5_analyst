# Домашнее задание к семинару 5 по дисциплине Python.
## Задачи:
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

    **Реализовано task01.py**


2. Создайте программу для игры с конфетами человек против человека.

    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

     **Реализовано task02_players.py**

    a) Добавьте игру против бота

    **Реализовано task02_bot.py**

    b) Подумайте как наделить бота ""интеллектом""
    
    **Реализовано task02_clever_bot.py**

3. Создайте программу для игры в ""Крестики-нолики"".
   
    **Реализовано task03.py**

    *Игра между двумя игроками. Право первого хода определяется случайным образом.*

4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
    Входные и выходные данные хранятся в отдельных текстовых файлах.

    **Реализовано task04.py**

    *Данные для кодировки берутся из файла "for_encoding.txt". Закодированные данные записываются в файл "RLE_txt.txt". Текст после "расшифровки" rle данных записываются в файл "after_decoding". Если алгоритмы работают верно, то первый и последний файлы совпадают.*