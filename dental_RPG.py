##
# dental_RPG.py
# By: Jarrod Roberts
# Created on: 18/08/20
# Create an You are going to develop an RPG
# simulator that will be designed to teach
# young people about dental hygiene. 


def characters():
    """ Gives user a character name """
    character = input('What is your name: ')
    enemy = 'Plaque'
    return character, enemy


def player_attack():
    attack_verify = input("Press Enter to attack ").strip()
    return True


def enemy_attack():
    attack_verify = True
    return attack_verify


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


main()
        
        

        
        
    
    
    
    

