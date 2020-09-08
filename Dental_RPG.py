 
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
    # Doesn't allow blank space
    while character == '':
        character = input('What is your name: ').strip().title()
    print('Welcome {}\n'.format(character))
    return character

def hp(username, user_hp, enemy, enemy_hp, user_damage, enemy_damage):
    """ Changes users and CPU's hit points"""

    user_hp -= enemy_damage
    enemy_hp -= user_damage

    # If hp goes below 0, it won't show negative numbers
    if user_hp < 0:
        print('''-------------------------------
{} HP: 0
{} HP: {}
-------------------------------
You lost to bad dental hygiene :(
          '''.format(username, enemy, enemy_hp))
    elif enemy_hp < 0:
        print('''-------------------------------
{} HP: {}
{} HP: 0
-------------------------------
You beat bad dental hygiene!
          '''.format(username, user_hp, enemy))
    elif user_hp < 0 and enemy_hp < 0:
        print('''-------------------------------
{} HP: 0
{} HP: 0
-------------------------------
You drew to bad dental hygiene :|
          '''.format(username, enemy))
    else:
        print('''-------------------------------
{} HP: {}
{} HP: {}
-------------------------------
              '''.format(username, user_hp, enemy, enemy_hp))

    return user_hp, enemy_hp


def weapon_pick():
    """ User picks weapon """

    # Menu type selection
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
    """ Assigns the moves to dict and list for later use """

    # Using damage first as key, makes it easier as they
    # are numerals rather than strings, easier to iterate with
    if weapon == 'Tooth Brush':
        moves_dict = {10:'30 Sec Brush', 15:'Hard Bristle',
                      20:'Circular Motion', 25:'Perfect Brush'}
        
    elif weapon == 'Mouth Wash':
        moves_dict = {10:'Swish Swish', 15:'Gargle',
                      20:'Gargle Rinse', 25:'Perfect Wash'}

    else:
        moves_dict = {10:'Bad Technique', 15:'Cutting Gums',
                 20:'Thorough Floss', 25:'Perfect Floss'}

    return moves_dict
        

def user_attack(weapon, moves, username):
    """ Asks user to select type of attack """

    # Count used to show which key to press 
    count = 0
    print('-------------------------------')
    print('Attacks:')
    for damage, move in sorted(moves.items()):
        count += 1
        print('{}: {}: {}DMG'.format(count, move, damage))

    valid_input = ['1', '2', '3', '4']
    attack = ''
    while not(attack in valid_input):
        attack = input('\nPick your attack: ')
        print('')

    # Tells user what they have done, makes it easier to test 
    for damage, move in moves.items():
        if (attack == '1') and (damage == 10):
            print('{} has used {} dealing {} DMG'.format(username, move, damage))
            return damage
        
        elif (attack == '2') and (damage == 15):
            print('{} has used {} dealing {} DMG'.format(username, move, damage))
            return damage
        
        elif (attack == '3') and (damage == 20):
            print('{} has used {} dealing {} DMG'.format(username, move, damage))
            return damage
        
        elif (attack == '4') and (damage == 25):
            print('{} has used {} dealing {} DMG'.format(username, move, damage))
            return damage


def enemy_attack():
    """ Randomly picks an attack for the enemy to pick """
    
    num = random.randint(1, 4)
    if num == 1:
        damage = 10
        attack = 'Plaque Buildup'
    elif num == 2:
        damage = 15
        attack = 'Chipped Tooth'
    elif num == 3:
        damage = 20
        attack = 'Cavity'
    else:
        damage = 25
        attack = 'Oral Cancer'
        
    return damage, attack
    
    

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
    


def turns(weapon, moves, username):
    """ Swaps between user attacking and CPU attacking """
    # Preset values
    enemy_hp = 100
    user_hp = 100
    user_damage = 0
    enemy_damage = 0
    enemy = enemy_select()
    enemy_hp, user_hp = hp(username, user_hp, enemy, enemy_hp, user_damage, enemy_damage)
    
    # Calls functions while both characters HP is above 0
    while (enemy_hp > 0) and (user_hp > 0):
        user_damage = user_attack(weapon, moves, username)
        enemy_damage, enemy_move = enemy_attack()
        print('{} used {} dealing {} DMG'.format(enemy, enemy_move, enemy_damage))
        print('-------------------------------')
        user_hp, enemy_hp = hp(username, user_hp, enemy, enemy_hp, user_damage, enemy_damage)
        

def main():
    username = characters()
    weapon = weapon_pick()
    moves = moves_type(weapon)
    turns(weapon, moves, username)
