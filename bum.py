import os
from time import sleep
from termcolor import colored
import webbrowser
import random
km = 'КАМЕНЬ'
no = 'НОЖНИЦЫ'
bu = 'БУМАГА'
bot = 0
people = 0
words = [ km, no, bu]
rand = (random.choice(words))

t = True
while t:
    os.system('cls')

    
    print('∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎')
    print(colored('КАМЕНЬ', 'grey', attrs=['bold']),colored('НОЖНИЦЫ', 'yellow', attrs=['bold']),colored('БУМАГА', 'white', attrs=['bold']))
    print('∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎')
    
    print('')
    
    print('∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎')
    print(colored('Счёт игрока:', 'grey', attrs=['bold']),colored(people, 'yellow', attrs=['bold']))
    print(colored('Счёт бота:', 'grey', attrs=['bold']),colored(bot, 'yellow', attrs=['bold']))
    print('∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎')
    
    print('')


    print('∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎')
    print('Выбери предмет:')
    print(colored('КАМЕНЬ - 1', 'grey', attrs=['bold']))
    print(colored('НОЖНИЦЫ - 2', 'yellow', attrs=['bold']))
    print(colored('БУМАГА - 3', 'white', attrs=['bold']))
    print('∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎')
    print('')
    vod = int(input())
    sleep(1)
        #Камень
    if vod == 1:
        print(colored('Твой ход:', 'grey', attrs=['bold']))
        print(colored(km, 'grey', attrs=['bold']))
        sleep(1)
        print('')
        print('Бот:')
        sleep(1)
        odn = (random.choice(words))
        print(odn)
        sleep(1)
        if odn == bu:
            print('')
            print(colored('BOT WIN', 'yellow', attrs=['bold']))
            bot += 1
        elif odn == km:
            print('')
            print(colored('FAIL', 'yellow', attrs=['bold']))
        else:
            print('')
            print(colored('USER WIN', 'yellow', attrs=['bold']))
            people += 1
        #Ножницы
    if vod == 2:
        print(colored('Твой ход:', 'grey', attrs=['bold']))
        print(colored(no, 'grey', attrs=['bold']))
        sleep(1)
        print('')
        print('Бот:')
        sleep(1)
        odn = (random.choice(words))
        print(odn)
        sleep(1)
        if odn == km:
            print('')
            print(colored('BOT WIN', 'yellow', attrs=['bold']))
            bot += 1
        elif odn == no:
            print('')
            print(colored('FAIL', 'yellow', attrs=['bold']))
        else:
            print('')
            print(colored('USER WIN', 'yellow', attrs=['bold']))
            people += 1
        #Бумага
    if vod == 3:
        print(colored('Твой ход:', 'grey', attrs=['bold']))
        print(colored(bu, 'grey', attrs=['bold']))
        sleep(1)
        print('')
        print('Бот:')
        sleep(1)
        odn = (random.choice(words))
        print(odn)
        sleep(1)
        if odn == no:
            print('')
            print(colored('BOT WIN', 'yellow', attrs=['bold']))
            bot += 1
        elif odn == bu:
            print('')
            print(colored('FAIL', 'yellow', attrs=['bold']))
        else:
            print('')
            print(colored('USER WIN', 'yellow', attrs=['bold']))
            people += 1
    if vod == 13:
        print('⠄⠄⠄⠄⡠⣿⢷⣻⣿⣾⣳⡇⢺⠟⠒⠒⠶⢤⣈⠃⢠⡀')
        print('⠄⠄⠄⢀⣼⡿⠋⢉⣉⣙⠿⠁⢁⣤⣤⣄⡀⠄⠈⠳⢾⣿⣄')
        print('⠄⠄⠄⢞⡞⠄⣴⣿⡿⠛⠓⠄⠉⠉⠉⠉⠹⣷⣄⠄⠄⠙⢿⣦')
        print('⠄⢀⣾⡟⠄⣸⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⡀⠄⠰⣿⣆')
        print('⠄⢸⣿⠁⢸⣿⠄⠄⢸⢸⠄⠄⠄⢸⣆⢠⣀⡀⣧⣨⣻⡀⠄⢻⣿⣦⣀')
        print('⠄⢸⡇⡀⠘⣿⢰⣐⢾⢿⡀⠄⡀⢨⣎⣻⣷⣶⣿⣿⣿⣇⢀⢸⣿⣿⣿⣷')
        print('⠄⢸⣣⡇⣧⣿⣿⣿⣿⡎⢳⣟⠿⣿⣿⣏⣉⣿⣿⣿⢻⣿⣿⣾⣿⣿⣿⣿⣦')
        print('⠄⠄⢼⡇⢹⣿⡏⢠⣿⣿⠄⠉⠄⠄⠈⠄⢹⣿⠟⠼⢻⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⠄⠄⠈⢿⢈⣿⡛⠘⣿⡇⠄⠄⡀⠄⠄⠄⠈⠉⠁⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⠄⠄⢀⣿⣼⡿⣿⣀⠄⠄⠄⠄⠃⠄⠄⠄⠄⠄⠄⠘⣻⡏⣿⣿⢻⣿⣿⣿⣿')
        print('⠄⠄⠾⢻⡇⣿⣸⣦⣀⠄⠄⠐⢟⠙⢻⠃⠄⠄⠄⣾⡏⣷⢻⡹⡟⣿⣿⡟⢿')
        print('⠄⢀⡴⢻⣇⢿⣷⢻⡟⠻⣶⣤⣀⠉⠄⣀⣴⡿⢣⡟⠄⣿⢸⡇⣰⡟⠻⠃⢸')
        print('⢠⡏⠄⠄⠈⠻⣿⣏⣷⠄⠈⠻⠉⠛⠛⠉⠄⠄⢛⠄⠄⠻⢠⠁⢛⠁⠄⠄⢸')
        print('⣼⠄⠄⠄⠄⠄⠈⢿⡘⠃⠄⠄⠄⠄⠄⠄⠠⠈⠄⠄⠄⢠⣸⣠⡞⠄⠄⠄⣿')
        print('⣤⠄⠄⠄⠄⠄⠄⢸⣇⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⠟⠄⠄⠄⣸⣿')
        sleep(4)
    if vod == 5:
        url = "https://youtu.be/KmtzQCSh6xk"
        webbrowser.open(url)
    if vod == 4:
        break
    sleep(2)