##
# dental_RPG.py
# By: Jarrod Roberts
# Created on: 18/08/20
# Create an You are going to develop an RPG
# simulator that will be designed to teach
# young people about dental hygiene. 


import random

def menu(username):
    """ Asks user what they want to do
        Play games, Highscores, quit etc """
    game_mode = ''
    end = False
    # Valid attack inputs, making sure it doesn't error out
    valid_inputs = ['1', '2', '3', '4', '5']
    while end == False:
        user_choice = ''
        while not (user_choice in valid_inputs):
            user_choice = str(input('''\n----------------------------------
What would you like to do:
1: Play out of 5
2: Play endless
3: Highscores
4: End Program
: ''')).strip()
            print('----------------------------------')
        # Runs the assigned choice
        if user_choice == '1':
            game_mode = game_type()

            # If user picks normal
            if game_mode == '1':
                repeat = 'Y'
                while repeat == 'Y':
                    win, loss = normal_turns()
                    win_loss(win, loss, username)
                    repeat = again()
                    if repeat == 'N':
                        menu(username)
                    else:
                        continue

            # If user picks complex
            else:
                repeat = 'Y'
                while repeat == 'Y':
                    win, loss = complex_turns()
                    win_loss(win, loss, username)
                    repeat = again()
                    if repeat == 'N':
                        menu(username)
                    else:
                        continue
            end = True

        elif user_choice == '2':
            continue 
            
        elif user_choice == '3':
            highscores()
            end = True
            
        elif user_choice == '4':
            goodbye(username)
            return False
            end = True
            
        else:
            end = False


def again():
    """ Takes input from user if they want to play again """
    again_values = ['Y', 'N']
    again = ''
    while not (again in again_values):
        again = input('\nWould you like to go again (Y/N): ').strip().upper()
    return again
    
def characters():
    """ Gives user a character name """
    character = ''
    # Doesn't allow blank space
    while character == '' or len(character) >= 24:
        character = input('What is your name: ').strip().title()
    print('Welcome {}\n'.format(character))
    return character


def game_type():
    """ Asks user if they want normal or complex R, P, S"""
    # Menu type of input
    valid_inputs = ['1', '2']
    end = False
    while end == False:
        choice = ''
        while not (choice in valid_inputs):
            choice = str(input('''\n----------------------------------
Would you like to play:
1: Normal
2: Complex
: ''')).strip()
            print('----------------------------------')
        end = True

    return choice


def normal_user_attack():
    """ Asks user to select type of attack """
    end = False
    attack_types = ['1', '2', '3']
    while end == False:
        attack_u_num = ''
        # Menu assigning the attacks that the user wants
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
    # Tells user what they picked 
    print('You have picked {}'.format(attack_u))

    return attack_u


def normal_enemy_attack():
    """ Enemy randomly selects between R P or S """
    attack_e_num = random.randint(1, 3)
    if attack_e_num == 1:
        attack_e = 'Plaque'
            
    elif attack_e_num == 2:
        attack_e = 'Bad Breath'
            
    elif attack_e_num == 3:
        attack_e = 'Gum Disease'

    return attack_e
    


def normal_turns():
    win = 0
    loss = 0
    for i in range(0, 5):
        print('Round {} of 5\n'.format(i + 1))
        attack_u = normal_user_attack()
        attack_e = normal_enemy_attack()
        # Assigns wins and losses 
        if ((attack_u == 'Tooth Brush' and attack_e == 'Plaque')
        or (attack_u == 'Mouth Wash' and attack_e == 'Bad Breath')
        or (attack_u == 'Dental Floss' and attack_e == 'Gum Disease')):
            print('\nYou used {} and beat {}. Good Job!'.format(attack_u, attack_e))
            win += 1

        elif (attack_u == 'Tooth Brush' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Mouth Wash.'.format(attack_e))
            loss += 1
            
        elif (attack_u == 'Mouth Wash' and attack_e == 'Gum Disease'):
            print('\nUh Oh. You have got {}. You need to use Dental Floss.'.format(attack_e))
            loss += 1
            
        elif (attack_u == 'Dental Floss' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush.'.format(attack_e))
            loss += 1
        else:
            print('\n{} doesn\'t effect {}.'.format(attack_u, attack_e))
            
    return win, loss


def complex_user_attack():
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


def complex_enemy_attack():
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
    


def complex_turns():
    win = 0
    loss = 0
    for i in range(0, 5):
        print('-----------------------------------')
        print('Round {} of 5\n'.format(i + 1))
        attack_u = complex_user_attack()
        attack_e = complex_enemy_attack()

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


def goodbye(username):
    """ Says goodbye to user """
    print('Goodbye {}'.format(username))
def main():
    username = characters()
    menu(username)
    
