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
    character = ''
    while character == '':
        character = input('What is your name: ').strip().title()
    print('Welcome {}\n'.format(character))
    return character


def weapon_pick():
    """ User picks weapon """
    end = False
    weapon_set = ['1', '2', '3']
    while end == False:
        weapon_set_num = ''
        while not (weapon_set_num in weapon_set):
            weapon_set_num = str(input('''What type of weapon do you want to use:
1: Tooth Brush:
    Moves          Damage
    30 sec brush    | 10 DMG
    hard bristle    | 15 DMG
    Circular motion | 20 DMG
    Perfect Brush   | 25 DMG
    
2: Mouth Wash
    Moves          Damage
    Swish swish     | 10 DMG
    Gargle          | 15 DMG
    Gargle rinse    | 20 DMG
    Perfect wash    | 25 DMG
    
3: Dental Floss
    Moves          Damage
    Bad Technique   | 10 DMG
    Cutting Gums    | 15 DMG
    Thorough Floss  | 20 DMG
    Perfect Floss   | 25 DMG

: ''')).strip()

        if weapon_set_num == '1':
            weapon_u = 'Tooth Brush'
            end = True
            
        elif weapon_set_num == '2':
            weapon_u = 'Mouth Wash'
            end = True
            
        elif weapon_set_num == '3':
            weapon_u = 'Dental Floss'
            end = True
            
        else:
            end = False
            
    return weapon_u


def moves_type(weapon):
    if weapon == 'Tooth Brush':
        moves = {'30 Sec Brush':10, 'Hard Bristle':15,
                 'Circular Motion':20, 'Perfect Brush':25}
    elif weapon == 'Mouth Wash':
        moves = {'Swish Swish':10, 'Gargle':15,
                 'Gargle Rinse':20, 'Perfect Wash':25}
    else:
        moves = {'Bad Technique':10, 'Cutting Gums':15,
                 'Thorough Floss':20, 'Perfect Floss':25}
    return moves
        

def user_attack():
    """ Asks user to select type of attack """
    end = False
    attack_types = ['1', '2', '3', '4']
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


def enemy_select():
    """ Enemy randomly selected """
    attack_e_num = random.randint(1, 3)
    if attack_e_num == 1:
        attack_e = 'Plaque'
            
    elif attack_e_num == 2:
        attack_e = 'Bad Breath'
            
    elif attack_e_num == 3:
        attack_e = 'Gum Disease'

    return attack_e
    


def turns(weapon, moves):
    enemy = enemy_select()
    enemy_hp = 100
    user_hp = 100
    
    

def win_loss(win, loss, username):
    """ Totals wins and loss and tells if the user won """
    if win > loss:
        print('Good Job {}, you won {} out of 5 rounds and beat Bad Dental Hygiene!'.format(username, win))
    elif win == loss:
        print('{}, you drew with bad dental hygiene, both winning {} rounds each'.format(username, win))
    else:
        print('{}, you have lost to bad dental hygiene. You only beat it {} times'.format(username, win))

def main():
    username = characters()
    weapon = weapon_pick()
    moves = moves_types(weapon)
    win, loss = turns()
    win_loss(win, loss, username)
    

        
        

        
        
    
    
    
    

