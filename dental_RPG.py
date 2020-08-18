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
    enemy = 'plaque'
    return character, enemy


def player_attack():
    attack_verify = input("Press Enter to attack ").strip()
    return True 



def turns():
    for i in range(0, 100):
        attack = player_attack()
        if attack == True:
            print("You have attacked")
        

        
        
    
    
    
    

