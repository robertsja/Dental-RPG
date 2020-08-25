##
# dental_RPG.py
# By: Jarrod Roberts
# Created on: 18/08/20
# Create an You are going to develop an RPG
# simulator that will be designed to teach
# young people about dental hygiene. 


import random


def characters():
    """ Gives user a character name """
    character = input('What is your name: ')
    return character


def user_attack():
    """ Asks user to select type of attack """
    end = False
    attack_types = ['1', '2', '3']
    while end == False:
        attack_u_num = ''
        while not (attack_u_num in attack_types):
            attack_u_num = str(input('''What type of attack do you want to do:
1: Tooth Brush (Beats Plaque, loses to Bad Breath, Draws against Gum Disease)
2: Mouth Wash (Beats Bad Breath, Loses to Gum disease, Draws Plaque)
3: Dental Floss (Beats Gum Disease, Loses to Plaque, Draws against Bad Breath)

: ''')).strip()

        if attack_u_num == '1':
            attack_u = 'Tooth Brush'
            end = True
            
        elif attack_u_num == '2':
            attack_u = 'Mouth Wash'
            end = True
            
        elif attack_u_num == '3':
            attack_u = 'Dental Floss'
            end = True
            
        else:
            end = False
    print('You have picked {}'.format(attack_u))

    return attack_u


def enemy_attack():
    """ Enemy randomly selects between R P or S """
    attack_e_num = random.randint(1, 3)
    if attack_e_num == 1:
        attack_e = 'Plaque'
            
    elif attack_e_num == 2:
        attack_e = 'Bad Breath'
            
    elif attack_e_num == 3:
        attack_e = 'Gum Disease'

    return attack_e
    


def turns():
    print()
    attack_u = user_attack()
    attack_e = enemy_attack()
    if ((attack_u == 'Tooth Brush' and attack_e == 'Plaque')
    or (attack_u == 'Mouth Wash' and attack_e == 'Bad Breath')
    or (attack_u == 'Dental Floss' and attack_e == 'Gum Disease')):
        print('\nYou used {} and beat {}. Good Job!'.format(attack_u, attack_e))


    elif (attack_u == 'Tooth Brush' and attack_e == 'Bad Breath'):
        print('\nUh Oh. You have got {}. You need to use Mouth Wash.'.format(attack_e))


    elif (attack_u == 'Mouth Wash' and attack_e == 'Gum Disease'):
        print('\nUh Oh. You have got {}. You need to use Dental Floss.'.format(attack_e))


    elif (attack_u == 'Dental Floss' and attack_e == 'Plaque'):
        print('\nUh Oh. You have got {}. You need to use Tooth Brush.'.format(attack_e))

    else:
        print('\n{} doesn\'t effect {}.'.format(attack_u, attack_e))
            
    

def win_loss(win, loss, username):
    """ Totals wins and loss and tells if the user won """
    if win > loss:
        print('Good Job {}, you won {} out of 5 rounds and won!'.format(username, win))
    elif win == loss:
        print('{}, you drew with bad dental hygiene, both winning {} rounds each'.format(username, win))
    else:
        print('{}, you have lost to bad dental hygiene. You only beat it {} times'.format(username, win))

def main():
    username = characters()
    turns()
    

        
        

        
        
    
    
    
    

