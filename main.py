import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) #to initialize colorama module

'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL.

'''

#print('\033[31m' + 'some red text')
#print(Fore.RED + 'some red text')
#print("Hello World! in red")
#print('\033[39m') # to clear text color, to avoid this: colorama.init(autoreset=True)
#print('Hello World! in normal text color')

print(Fore.RED + 'some red fore color')
print(Back.GREEN + 'some green back color')
print(Style.DIM + 'some dim style')
print(Style.NORMAL + 'some normal style')
print(Style.BRIGHT + 'some bright style')
