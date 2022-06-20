#rock paper scissor
import random

#defining Global variables
hands = ['r','p','s']

print('ROCK PAPER SCISSORS \n Enjoy!!!')
print(' \n \n player : rock paper scirros go')

# collecting player input
def player():
    player_hand = ''
    while player_hand not in ['r','p','s']:
        player_hand = str(input('play your hand :_').lower())
    return player_hand

def cpu():
    cpu_hand = random.choice(hands)
    return cpu_hand
    
def tiecheck():
    if player() == cpu():
        print('Tie Game!')
        return True
    else:
        print('Game continues!')
        return False


def wincheck():
    if player()=='r' and cpu()== 's' or player()=='p' and cpu()== 'r' or player()=='s' and cpu()== 'p':
        print('Player wins!')
        return True
    else:
        print('Player Lost this round!')
        return False


def play_again():
    choice = str(input('do you want to play again?: Y OR N :_').lower())
    if choice =='y':
        return True
    else: return False


while True:
    player()
    cpu()
    if tiecheck() == False:
        wincheck()
        if wincheck == True:
            print('PLAYER WINS')
            break
    else:
        play_again()
        if play_again() == False:
            break
        else:
            print('RUN THE GAME AGAIN')
