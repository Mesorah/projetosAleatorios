from random import randint

def main():
    print('\033[1;33m1v1 fight against Mega Blaster of the World')
    print('You have 10 life and deal 3 damage against him with 25 life and deal 4 damage')
    print('You have 3 healing potions that heal 4 health points\033[m')

def attributes():
    health_player = 10
    health_boss = 15

    return health_player, health_boss

def cure_potion(health_player, potion, cure_potion_player, took_potion):

    try:
        cure_potion_player = int(cure_potion_player)
    except ValueError:
        print('enter only valid numbers')
    except Exception:
        print('unknown error')

    if cure_potion_player == 2:
        potion -= 1
        health_player += 4
        took_potion = True

    return health_player, potion, cure_potion_player, took_potion

def player_attack( health_boss):
    chance_of_damage_player = randint(1, 5)

    if chance_of_damage_player != 5:
        health_boss -= 3
        print(f'boss health {health_boss}')

    elif chance_of_damage_player == 5:
        print('you missed')
    
    return health_boss

def boss_attack(health_player ):
    chance_of_damage_boss = randint(1,5)

    if chance_of_damage_boss != 5:
        health_player -= 4
        print(f'you health {health_player}')

    elif chance_of_damage_boss == 5 :
        print('he missed')

    return health_player

def match():
    main()
    health_player, health_boss = attributes()
    potion = 3
    tot = 0
    
    match_player = 0

    while health_player > 1 and health_boss > 1:
        took_potion = False
        tot += 1

        rounds = randint(1,2)
        

        if health_player > 6:
            print()
            match_player = input('press 1 to attack: ')
            try:
                match_player = int(match_player)
            except ValueError:
                print('enter only valid numbers')
            except Exception:
                print('unknown error')
        
        if match_player == 1:
            if rounds == 1:
                health_boss = player_attack(health_boss)
            elif rounds == 2:
                health_player = boss_attack(health_player)

            if health_player <= 6 and potion > 0:
                cure_potion_player = input('press 1 to attack or 2 to drink a healing potion: ')
                health_player, potion, cure_potion_player, took_potion = cure_potion(health_player, potion, cure_potion_player, took_potion)

                if took_potion:
                    print(f'you recovered 4 life: {health_player}')
                    print(f'do you have {potion} potions')

            elif potion < 1 and tot != 1:
                cure_potion_player = input('press 1 to attack: ')
                

        if health_player <= 0:
            print('you lose')
            break

        if health_boss <= 0:
            print('you win')
            break

match()