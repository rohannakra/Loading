from time import sleep
from random import randint
from os import system

parts = ['/', '-', '\\']

def sim(index, bar, start=False):
    if index % 2 == 1 or index == 0:
        if start == True:
            bar = bar.replace('.', '=', 1)
            bar = bar.replace('.', '>', 1)
        else:
            bar = bar.replace('>', '=', 1)
            bar = bar.replace('.', '>', 1)
    
    print(f'{parts[index]} {bar}')
    

    sleep(int(randint(0, 1)))
    system('CLS')

    if '>' not in bar:
        return

    sim(index+1, bar) if index != 2 else sim(0, bar)

system('CLS')
sim(0, '[..............................]', start=True)
system('CLS')
