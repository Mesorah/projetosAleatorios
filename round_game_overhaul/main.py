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


def match():
    from random import randint

    health_player, health_boss = attributes()
    potion = 3
    tot = 0

    while health_player > 0 and health_boss > 0:
        took_potion = False
        tot += 1

        rounds = randint(1,2)
        chanche_of_damage_player = randint(1,5)
        chanche_of_damage_boss = randint(1,5)

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
            
            if health_player <= 6:
                cure_potion_player = input('press 1 to attack or 2 to drink a healing potion: ')
                health_player, potion, cure_potion_player, took_potion = cure_potion(health_player, potion, cure_potion_player, took_potion)
                if took_potion:
                    print(f'you recovered 4 life: {health_player}')
                    print(f'do you have {potion} potions')

            if chanche_of_damage_player != 5 and rounds == 1 and took_potion == False:
                health_boss -= 3
                print(f'boss health {health_boss}')

            elif chanche_of_damage_player == 5:
                print('you missed')

            if chanche_of_damage_boss != 5 and rounds == 2 and took_potion == False:
                health_player -= 4
                print(f'you health {health_player}')

            elif chanche_of_damage_boss == 5:
                print('he missed')
        
        else:
            ...


main()
match()