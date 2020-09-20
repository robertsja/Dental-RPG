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
1: Play out of 5 (pai rawa atu rima)
2: Play endless (mure ore)
3: Highscores (kaute teitei)
4: End Program (mutunga)
: ''')).strip()
            print('----------------------------------')
        # Runs the assigned choice
        if user_choice == '1':
            game_mode = game_type()

            # If user picks normal
            if game_mode == '1':
                repeat = 'Y'
                while repeat == 'Y':
                    print('Out of 5 - Normal:')
                    win, loss, draw = normal_turns()
                    win_loss(win, loss, draw, username)
                    repeat = again()
                    if repeat == 'N':
                        # Shows that it returns to menu
                        end = False
                    else:
                        continue

            # If user picks complex
            else:
                repeat = 'Y'
                while repeat == 'Y':
                    print('Out of 5 - Comlex:')
                    win, loss, draw = complex_turns()
                    win_loss(win, loss, draw, username)
                    repeat = again()
                    if repeat == 'N':
                        # Shows that it returns to menu
                        end = False
                    else:
                        continue

        elif user_choice == '2':
            game_mode = game_type()

            # If user picks normal
            if game_mode == '1':
                print('Endless - Normal:')
                win, loss, draw = endless_normal_turns()
                win_loss(win, loss, draw, username)
                end = False

            # If user picks complex
            else:
                print('Endless - Complex:')
                win, loss, draw = endless_complex_turns()
                win_loss(win, loss, draw, username)
                end = False
                
            
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
        character = input('What is your name:\n'
                          '(Ko wai tou ingoa): ').strip().title()
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
1: Normal (noa)
2: Complex (matatini)
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
1: Tooth Brush (paraihe niho)
2: Mouth Wash (horoi horoi mangai)
3: Dental Floss (miro niho)
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
    draw = 0
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
            print('\nUh Oh. You have got {}. You need to use Mouth Wash (horoi horoi mangai).'.format(attack_e))
            loss += 1
            
        elif (attack_u == 'Mouth Wash' and attack_e == 'Gum Disease'):
            print('\nUh Oh. You have got {}. You need to use Dental Floss (miro niho).'.format(attack_e))
            loss += 1
            
        elif (attack_u == 'Dental Floss' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho).'.format(attack_e))
            loss += 1
        else:
            print('\n{} doesn\'t effect {}.'.format(attack_u, attack_e))
            draw += 1
            
    return win, loss, draw


def complex_user_attack():
    """ Asks user to select type of attack """
    end = False
    # Valid attack inputs, making sure it doesn't error out
    attack_types = ['1', '2', '3', '4', '5']
    while end == False:
        attack_u_num = ''
        while not (attack_u_num in attack_types):
            attack_u_num = str(input('''What type of attack do you want to do:
1: Tooth Brush (paraihe niho)
2: Mouth Wash (horoi horoi mangai)
3: Dental Floss (miro niho)
4: Fillings (whakakii)
5: Whitener (ma)
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
    draw = 0
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
            print('\nUh Oh. You have got {}. You need to use Mouth Wash (horoi horoi mangai) '
                  'or Dental Floss (miro niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Tooth Brush' and attack_e == 'Cavities'):
            print('\nUh Oh. You have got {}. You need to use Fillings (whakakii) '
                  'or Dental Floss (miro niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1
            
        elif (attack_u == 'Mouth Wash' and attack_e == 'Cavities'):
            print('\nUh Oh. You have got {}. You need to use Fillings (whakakii) '
                  'or Dental Floss (miro niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Mouth Wash' and attack_e == 'Yellow Teeth'):
            print('\nUh Oh. You have got {}. You need to use Whitener (ma) '
                  'or Fillings (whakakii) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Dental Floss' and attack_e == 'Yellow Teeth'):
            print('\nUh Oh. You have got {}. You need to use Fillings (whakakii) '
                  'or Whitener (ma) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Dental Floss' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho) '
                  'or Whitener (ma) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Fillings' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho) '
                  'or Whitener (ma) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Fillings' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Mouth Wash (horoi horoi mangai)'
                  'or Tooth Brush (paraihe niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Whitener' and attack_e == 'Gum Disease'):
            print('\nUh Oh. You have got {}. You need to use Dental Floss (miro niho) '
                  'or Mouth Wash (horoi horoi mangai) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Whitener' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho) '
                  'or Mouth Wash (horoi horoi mangai) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        # Assign if you draw
        else:
            print('\n{} doesn\'t effect {}.'.format(attack_u, attack_e))
            draw += 1
        
            
    return win, loss, draw
    

def endless_normal_user_attack():
    """ Asks user to select type of attack """
    end = False
    attack_types = ['1', '2', '3', '4', '0']
    while end == False:
        attack_u_num = ''
        # Menu assigning the attacks that the user wants
        while not (attack_u_num in attack_types):
            attack_u_num = str(input('''What type of attack do you want to do:
1: Tooth Brush (paraihe niho) 
2: Mouth Wash (horoi horoi mangai)
3: Dental Floss (miro niho) 

0: Stop Endless
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

        elif attack_u_num == '0':
            attack_u = '0'
            end = True
            
        else:
            attack_u = 'End'
            end = True
    # Tells user what they picked 
    print('You have picked {}'.format(attack_u))

    return attack_u    


def endless_normal_turns():
    win = 0
    draw = 0
    loss = 0
    count = 0
    attack_u = ''
    while attack_u != '0':
        count += 1
        print('-------------------------')
        print('Round {}\n'.format(count))
        attack_u = endless_normal_user_attack()
        attack_e = normal_enemy_attack()
        # Assigns wins and losses 
        if ((attack_u == 'Tooth Brush' and attack_e == 'Plaque')
        or (attack_u == 'Mouth Wash' and attack_e == 'Bad Breath')
        or (attack_u == 'Dental Floss' and attack_e == 'Gum Disease')):
            print('\nYou used {} and beat {}. Good Job!'.format(attack_u, attack_e))
            win += 1

        elif (attack_u == 'Tooth Brush' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Mouth Wash (horoi horoi mangai).'.format(attack_e))
            loss += 1
            
        elif (attack_u == 'Mouth Wash' and attack_e == 'Gum Disease'):
            print('\nUh Oh. You have got {}. You need to use Dental Floss (miro niho).'.format(attack_e))
            loss += 1
            
        elif (attack_u == 'Dental Floss' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho).'.format(attack_e))
            loss += 1

        # If user selects 0 it wont do anything 
        elif attack_u == '0':
            continue

        else:
            print('\n{} doesn\'t effect {}.'.format(attack_u, attack_e))
            draw += 1

        # Print wins/draws/loss
        print('Wins - {}, Draws - {}, Loss - {}'.format(win, draw, loss))

        
            
    return win, loss, draw


def endless_complex_user_attack():
    """ Asks user to select type of attack """
    end = False
    # Valid attack inputs, making sure it doesn't error out
    attack_types = ['1', '2', '3', '4', '5', '0']
    while end == False:
        attack_u_num = ''
        while not (attack_u_num in attack_types):
            attack_u_num = str(input('''What type of attack do you want to do:
1: Tooth Brush (paraihe niho)
2: Mouth Wash (horoi horoi mangai)
3: Dental Floss (miro niho)
4: Fillings (whakakii)
5: Whitener (ma)
(see image for flow chart)

0: To Quit Endless
: ''')).strip().upper()

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

        elif attack_u_num == '0':
            attack_u = '0'
            end = True
            
        else:
            end = False
    print('You have picked {}'.format(attack_u))

    return attack_u


def endless_complex_turns():
    win = 0
    loss = 0
    draw = 0
    count = 0
    attack_u = ''
    while attack_u != '0':
        count += 1
        print('-----------------------------------')
        print('Round {}\n'.format(count))
        attack_u = endless_complex_user_attack()
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
            print('\nUh Oh. You have got {}. You need to use Mouth Wash (horoi horoi mangai)'
                  'or Dental Floss (miro niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Tooth Brush' and attack_e == 'Cavities'):
            print('\nUh Oh. You have got {}. You need to use Fillings (whakakii) '
                  'or Dental Floss (miro niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1
            
        elif (attack_u == 'Mouth Wash' and attack_e == 'Cavities'):
            print('\nUh Oh. You have got {}. You need to use Fillings (whakakii) '
                  'or Dental Floss (miro niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Mouth Wash' and attack_e == 'Yellow Teeth'):
            print('\nUh Oh. You have got {}. You need to use Whitener (ma) '
                  'or Fillings (whakakii) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Dental Floss' and attack_e == 'Yellow Teeth'):
            print('\nUh Oh. You have got {}. You need to use Fillings (whakakii) '
                  'or Whitener (ma) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Dental Floss' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho) '
                  'or Whitener (ma) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Fillings' and attack_e == 'Plaque'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho) '
                  'or Whitener (ma) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Fillings' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Mouth Wash (horoi horoi mangai) '
                  'or Tooth Brush (paraihe niho) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Whitener' and attack_e == 'Gum Disease'):
            print('\nUh Oh. You have got {}. You need to use Dental Floss (miro niho) '
                  'or Mouth Wash (horoi horoi mangai) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        elif (attack_u == 'Whitener' and attack_e == 'Bad Breath'):
            print('\nUh Oh. You have got {}. You need to use Tooth Brush (paraihe niho) '
                  'or Mouth Wash (horoi horoi mangai) if you have {}.'.format(attack_e, attack_e))
            loss += 1

        # If user uses 0, it doesnt do anything
        elif attack_u == '0':
            continue

        # Assign if you draw
        else:
            print('\n{} doesn\'t effect {}.'.format(attack_u, attack_e))
            draw += 1

        # Print wins/draws/loss
        print('Wins - {}, Draws - {}, Loss - {}'.format(win, draw, loss))        
            
    return win, loss, draw


def win_loss(win, loss, draw, username):
    """ Totals wins and loss and tells if the user won """
    # Using CPU and User win/loss count to find winner 
    if win > loss:
        print('Good Job {}, you won {} times, drew {} times, lost {} times,'
              'and beat Bad Dental Hygiene!'.format(username, win, draw, loss))
    elif win == loss:
        print('{}, you drew with bad dental hygiene. You won {} times, drew {} times, '
              'and lost {} times'.format(username, win, draw, loss))
    else:
        print('{}, you have lost to bad dental hygiene. You won {} times, drew {} times, '
              'and lost {} times'.format(username, win, draw, loss))


def goodbye(username):
    """ Says goodbye to user """
    print('Goodbye (tēnā koe) {}'.format(username))
def main():
    username = characters()
    menu(username)
