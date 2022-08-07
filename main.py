'''
Задача 1.
Напишите программу, удаляющую из текста все слова содержащие "абв",
которое регистронезависимо.
'''

from functools import reduce
import numbers
from turtle import update


def del_words_with_chars(text: list[str]) -> list:
    return list(filter(lambda x: x.lower().find('абв')==-1, text))

original_text=['абвгдеж', 'рабав', 'копыто', 'фабв', 'Абкн', 'абрыволк', 'аБволк']
print(del_words_with_chars(original_text))

'''
Задача 2.
Вы когда-нибудь играли в игру "Крестики-нолики"?
Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.
'''
# Глобальные переменные:
CROSS_SYMBOL='X'
ZERO_SYMBOL='0'
SIZE_OF_BOARD=9
MOVES=' '
FRIENDSHIP='Ничья'
# Приветствие игрока
def instruction():
    print('''
Игра "Крестики-нолики".
Чтобы сделать ход, введи номер клетки,
куда хочешь поставить свой символ:

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8


''')
# Обработка ответа игрока на вопрос с выбором символа
def start(quest):
    answ=None
    while answ not in ('да','нет'):
        answ=input(quest).lower()
    return answ

# Даём игроку возможность выбрать свой символ. 
def choose_of_symbol():
    first_move=start("Вы хотите быть первым, кто сделает ход \
(играть крестиками)?  ")
    if first_move=='да':
        print('Окей, ты играешь крестиками!')
        human=CROSS_SYMBOL
        comp=ZERO_SYMBOL
    else:
        print('ОК, я делаю первый ход крестиками')
        human=ZERO_SYMBOL
        comp=CROSS_SYMBOL
    return comp, human
# Запрашиваем у игрока номер ячейки, где он хочет поставить свой символ.
def move_number(low,high):
    answ=None
    while answ not in range(low,high):
        answ=int(input("Делай свой ход - напиши номер поля (0-8): "))
    return answ

# Перерисовка поля.
def new_board():
    board=[]
    for i in range(SIZE_OF_BOARD):
        board.append(MOVES)
    return board
# Вывод поля в консоль
def show_of_board(board):
    print('\n', board[0], '|', board[1], '|', board[2])
    print('---------')
    print('\n'
          , board[3], '|', board[4], '|', board[5])
    print('---------')
    print('\n', board[6], '|', board[7], '|', board[8], '\n')

# Проверяем, куда можно пойти.
def aviable_moves(board):
    aviable_moves=[]
    for i in range(SIZE_OF_BOARD):
        if board[i]==MOVES:
            aviable_moves.append(i)
    return aviable_moves

# Определяем победителя.
def winner(board):
    variants_of_win=((0,1,2),
                    (3,4,5),
                    (6,7,8),
                    (0,3,6),
                    (1,4,7),
                    (2,5,8),
                    (0,4,8),
                    (2,4,6))
    for i in variants_of_win:
        if board[i[0]]==board[i[1]]==board[i[2]]!=MOVES:
            winner=board[i[0]]
            return winner
        if MOVES not in board:
            return FRIENDSHIP
    return None

# Обработка хода игрока
def human_move(board,human):
    aviable=aviable_moves(board)
    move=None
    while move not in aviable:
        move=move_number(0,SIZE_OF_BOARD)
        if move not in aviable:
            print('Поле занято. Напиши другой номер: ')
    print('Супер!')
    return move

# Ход Компьютера
def comp_move(board,comp,human):
    board=board[:]
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print('Мой ход: ')
    for i in aviable_moves(board):
        board[i]=comp
        if winner(board)==comp:
            print(i)
            return i
        board[i]=MOVES
    for j in aviable_moves(board):
        board[j]=human
        if winner(board)==human:
            print(j)
            return j
        board[j]=MOVES
    for k in aviable_moves(board):
        print(k)
        return k

# Переключение хода.
def who_is_next_move(move):
    if move==CROSS_SYMBOL:
        return ZERO_SYMBOL
    else:
        return CROSS_SYMBOL

# Поздравление победителя.
def congratulation(winner,comp,human):
    if winner!=FRIENDSHIP:
        print('Собрана линия ', winner)
    else:
        print(FRIENDSHIP)
    if winner==comp:
        print('Компьютер выиграл!')
    elif winner==human:
        print('Ты победил!')
    elif winner==FRIENDSHIP:
        print(FRIENDSHIP)

def main():
    instruction()
    comp,human=choose_of_symbol()
    whose_move=CROSS_SYMBOL
    board=new_board()
    show_of_board(board)
    while not winner(board):
        if whose_move==human:
            move=human_move(board,human)
            board[move]=human
        else:
            move=comp_move(board,comp,human)
            board[move]=comp
        show_of_board(board)
        whose_move=who_is_next_move(whose_move)
    winr=winner(board)
    congratulation(winr,comp,human)
main()
input('\n Нажми "Enter", чтобы выйти')
'''
Задача 3.
"Отфильтруйте текст, чтобы его можно было нормально прочесть.
Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых."
'''
incoming_text="Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин.\
Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, \
по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. \
Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. \
Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из \
подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в \
магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в \
общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил."

def filter_text(txt):
    def delete_words (text, word):
        find = text.lower().find(word)
        while find!=-1:
            repl_str=text[find:find+len(word)]
            text=text.replace(repl_str, '')
            find=text.lower().find(word)
        return text
    def clean_text (text: str):
        if text.startswith(', '):
            text=text.replace(', ', '', 1)
        text=text.replace('.,','.').replace(', .', '.').replace('  ', ' ')
        text=text[0].upper()+text[1:]
        find_index=0
        while find_index<len(text):
            find=text.find('.', find_index)+2
            if find<find_index:
                break
            text=text[:find]+text[find:find+2].capitalize()+text[find+2:]
            find_index=find
        return text

    parasites_list=["короче говоря", "короче", "эээээ", "ээээ", "эээ", "ну", "ясен пень", "в общем", "кажется", "как бы", "….", "…", "...", "кстати", " ,"]
    for filter_word in parasites_list:
        txt=delete_words(txt, filter_word)
    txt=clean_text(txt)
    return txt


cleaned_text=filter_text(incoming_text)
# Так как в тексте отались запятые, то и их снесём.
cleaned_text = cleaned_text.replace(',', '')
cleaned_text = cleaned_text.replace('.,', '')

print(cleaned_text)

'''
Задача №4:
Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. 
Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом:
если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается,
его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С 
помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.
''' 
from functools import reduce

languages=['Assembler', 'Basic', 'C Sharp', 'C++', 'Go', 'Java', 'JavaScript', 'Kotlin', 'Objective-C', 'Pascal', 'PHP', 'Python', 'QBasic', 'SQL', 'Swift', 'VBA']
numbers=[i for i in range(1, len(languages)+1)]

def tuple_list():
    return tuple(zip(numbers, [language.upper() for language in languages]))

def filter_list(in_tuple):
    out_list=[]
    for index, name in in_tuple:
        sum_of_points=reduce(lambda x, y: x + ord(y)-ord('A')+1, name, 0)
        div_list=[i for i in range(1, sum_of_points // 2 + 1) if not sum_of_points % i]
        if index in div_list:
            out_list.append((sum_of_points, name))
    return tuple(out_list)

languages_tuple=tuple_list()
print(languages_tuple)
filtered_languages_tuple=filter_list(languages_tuple)
print(filtered_languages_tuple)