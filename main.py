import sys
import collections
from random import randint
from RandomKey import RandomKey
from HMAC import HmacGen
from Rule import Rule
from Table import Table

args = sys.argv
len_args = len(args) - 1
if len_args < 3:
    print('Count of args must be >= 3. Please give correct value.\n'
          'E.g. - python main.py rock paper scissors')
    sys.exit()
elif len_args % 2 == 0:
    print('Count of args must be an odd. Please give correct value.\n'
          'E.g. - python main.py rock paper scissors')
    sys.exit()
args_collections = collections.Counter(args)
cnt_repeat = len([i for i in args_collections if args_collections[i] > 1])
if cnt_repeat != 0:
    print('Args must be unique. Please give correct value.\n'
          'E.g. - python main.py rock paper scissors')
    sys.exit()
key = RandomKey().keygen()
computer_move_num = randint(1, len_args)
computer_move = args[computer_move_num]
hmac = HmacGen().hmac(key, computer_move)
print('HMAC:', hmac)


def show_moves():
    print('Available moves:')
    for i in range(1, len(args)):
        print(i, '-', args[i])
    print('0 - exit')
    print('? - help')


show_moves()
while True:
    try:
        move = input('Enter your move: ')
        if move == '?':
            Table().print_table(args)
            show_moves()
            continue
        else:
            move = int(move)
    except ValueError:
        show_moves()
    else:
        if move == 0:
            sys.exit()
        if move in [i for i in range(1, len_args + 1)]:
            break
        else:
            show_moves()
print('Your move:', args[move])
print('Computer move:', computer_move)
if args[move] == computer_move:
    result = 'Draw'
else:
    winners = Rule().get_winners(args, computer_move_num)
    if args[move] in winners:
        result = 'Win'
    else:
        result = 'Lose'
print('Result:', result)
print('HMAC key:', key)
