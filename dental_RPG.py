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


def user_attack():
    """ Asks user to select type of attack """
    end = False
    # Valid attack inputs, making sure it doesn't error out
    attack_types = ['1', '2', '3', '4', '5']
    while end == False:
        attack_u_num = ''
        while not (attack_u_num in attack_types):
            attack_u_num = str(input('''What type of attack do you want to do:
1: Tooth Brush 
2: Mouth Wash
3: Dental Floss
4: Fillings
5: Whitener
(see image for flow chart)
: ''')).strip()

        # Assigns the attack
        if attack_u_num == '1':
            attack_u = 'Tooth Brush'
            end = True
            
        elif attack_u_num == '2':
            attack_u = 'Mouth Wash'
            end = True
            
        elif attack_u_num == '3':
            attack_u = 'Dental Floss'
            end = True

        elif attack_u_num == '4':
            attack_u = 'Fillings'
            end = True

        elif attack_u_num == '5':
            attack_u = 'Whitener'
            end = True
            
        else:
            end = False
    print('You have picked {}'.format(attack_u))

    return attack_u


def enemy_attack():
    """ Enemy randomly selects between R P or S """
    attack_e_move = ''
    
    attack_e_num = random.randint(1, 5)
    if attack_e_num == 1:
        attack_e_move = 'Yellow Teeth'
            
    elif attack_e_num == 2:
        attack_e_move = 'Plaque'
            
    elif attack_e_num == 3:
        attack_e_move = 'Bad Breath'

    elif attack_e_num == 4:
        attack_e_move = 'Gum Disease'

    elif attack_e_num == 5:
        attack_e_move = 'Cavities'

    return attack_e_move
    


def turns():
    win = 0
    loss = 0
    for i in range(0, 5):
        print('-----------------------------------')
        print('Round {} of 5\n'.format(i + 1))
        attack_u = user_attack()
        attack_e = enemy_attack()

        # Assigning if you win 
        if ((attack_u == 'Tooth Brush' and attack_e == 'Plaque')
        or (attack_u == 'Tooth Brush' and attack_e == 'Bad Breath')
        or (attack_u == 'Mouth Wash' and attack_e == 'Bad Breath')
        or (attack_u == 'Mouth Wash' and attack_e == 'Gum Disease')
        or (attack_u == 'Dental Floss' and attack_e == 'Gum Disease')
        or (attack_u == 'Dental Floss' and attack_e == 'Cavities')
        or (attack_u == 'Fillings' and attack_e == 'Cavities')
        or (attack_u == 'Fillings' and attack_e == 'Yellow Teeth')
        or (attack_u == 'Whitener' and attack_e == 'Yellow Teeth')
        or (attack_u == 'Whitener' and attack_e == 'Plaque')):
            print('\nYou used {} and beat {}. Good Job!'.format(attack_u, attack_e))
            win += 1

        # Assigning if you lose
        elif (attack_u == 'Tooth Brush' and attack_e == 'Gum Disease'):
            print('\nUh Oh. You have got {}. You need to use Mouth Wash '
                  'or Dental Floss if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Tooth Brush' and attack_e == 'Cavities'):
            print('\nUh Oh. You have got {}. You need to use Fillings '
                  'or Dental Floss if you have {}.'.format(attack_e, attack_e))
            loss += 1
            
        elif (attack_u == 'Mouth Wash' and attack_e == 'Cavities'):
            print('\nUh Oh. You have got {}. You need to use Fillings '
                  'or Dental Floss if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Mouth Wash' and attack_e == 'Yellow Teeth'):
            print('\nUh Oh. You have got {}. You need to use Whitener '
                  'or Fillings if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Dental Floss' and attack_e == 'Yellow Teeth'):
            print('\nUh Oh. You have got {}. You need to use Fillings '
                  'or Whitener if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Dental Floss' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush '
                  'or Whitener if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Fillings' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush '
                  'or Whitener if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Fillings' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Mouth Wash '
                  'or Tooth Brush if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Whitener' and attack_e == 'Gum Disease'):
            print('\nUh Oh. You have got {}. You need to use Dental Floss '
                  'or Mouth Wash if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Whitener' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush '
                  'or Mouth Wash if you have {}.'.format(attack_e, attack_e))
            loss += 1

        # Assign if you draw
        else:
            print('\n{} doesn\'t effect {}.'.format(attack_u, attack_e))
        
            
    return win, loss
    

def win_loss(win, loss, username):
    """ Totals wins and loss and tells if the user won """
    # Using CPU and User win/loss count to find winner 
    if win > loss:
        print('Good Job {}, you won {} out of 5 rounds and beat Bad Dental Hygiene!'.format(username, win))
    elif win == loss:
        print('{}, you drew with bad dental hygiene, both winning {} rounds each'.format(username, win))
    else:
        print('{}, you have lost to bad dental hygiene. You only beat it {} times'.format(username, win))

def main():
    username = characters()
    win, loss = turns()
    win_loss(win, loss, username)
