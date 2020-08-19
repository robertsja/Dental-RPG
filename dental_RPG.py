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
    enemy = 'Plaque'
    return character, enemy


def player_attack():
    """ Asks user to select type of attack """
    end = False
    attack_types = ['1', '2', '3']
    while end == False:
        attack_u = ''
        while not (attack_u_num in attack_types):
            attack_u_num = str(input('''What type of attack do you want to do:
1: Rock
2: Paper
3: Scissors

: '''))

    if attack_u_num == '1':
        attack_u = 'Rock'
        end = True
        
    elif attack_u_num == '2':
        attack_u = 'Paper'
        end = True
        
    elif attack_u_num == '3':
        attack_u = 'Scissors'
        end = True
        
    else:
        end = False
    print('You have picked {}'.format(attack_u))
    return attack_u


def enemy_attack():
    """ Enemy randomly selects between R P or S """
    attack_e_num = random.randint(1, 3)
    print(attack_e_num)
    


def turns(e_name):
    for i in range(0, 100):
        attack_p = player_attack()
        if attack_p == True:
            print("You have attacked\n")
        else:
            continue
        attack_e = enemy_attack()
        if attack_e == True:
            print('{} has attacked\n'.format(e_name))
        else:
            continue

def main():
    username, e_name = characters()
    turns(e_name)
    
    

        
        

        
        
    
    
    
    

