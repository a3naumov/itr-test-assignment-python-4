class Table:
    def __init__(self):
        pass

    def print_table(self, args):
        from Rule import Rule
        len_of_args = len(args)
        for y in range(0, len_of_args):
            winners = []
            if y != 0:
                winners = Rule().get_winners(args, y)
            for x in range(0, len_of_args):
                if y == 0 and x == 0:
                    print('{:15}'.format(''), end='')
                else:
                    if y == 0 and x != 0:
                        print(f'{args[x]:15}', end='')
                    elif y != 0 and x == 0:
                        print(f'{args[y]:15}', end='')
                    else:
                        cell_x = args[x]
                        cell_y = args[y]
                        if cell_y == cell_x:
                            res = 'Draw'
                        else:
                            if cell_x in winners:
                                res = 'Lose'
                            else:
                                res = 'Win'
                        print(f'{res:15}', end='')
            print('\n')
