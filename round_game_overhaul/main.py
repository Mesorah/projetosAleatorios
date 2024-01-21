from random import randint

def main():
    print('\033[1;33m1v1 fight against Mega Blaster of the World')
    print('You have 10 life and deal 3 damage against him with 25 life and deal 4 damage')
    print('You have 3 healing potions that heal 4 health points\033[m')

def attributes():
    health_player = 10
    health_boss = 25

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

def player_attack(health_boss):
    global player_situation
    chance_of_damage_player = randint(1, 5)

    if chance_of_damage_player != 5:
        health_boss -= 3
        print(f'boss health {health_boss}')
        player_situation = True

    elif chance_of_damage_player == 5:
        print('you missed')
        player_situation = False

    return health_boss

def boss_attack(health_player):
    global boss_situation
    chance_of_damage_boss = randint(1,5)

    if chance_of_damage_boss != 5:
        health_player -= 4
        print(f'you health {health_player}')
        boss_situation = True

    elif chance_of_damage_boss == 5 :
        print('he missed')
        boss_situation = False

    return health_player

def critical_player(health_boss):
    health_boss -= 6
    print(f'you critted and dealt 6 damage he life {health_boss}')

    return health_boss

def critical_boss(health_player):
    health_player -= 8
    print(f'he did a critical and did 8 damage you life {health_player}')

    return health_player

def super_player(health_boss):
    
    if player_situation:
        super_list.append(1)
    elif not player_situation:
        super_list.clear()
    elif boss_situation:
        super_list.clear()

    if super_list.count(1) == 3:
        health_boss -= 7
        super_list.clear()
        print(f'did you use super | life boss: {health_boss}')

    print(f'{super_list.count(1)} / 3 to use super')

    return health_boss

def dodge_player():
        print('he was wrong')

def dodge_boss():
        print('you was wrong')

def match():
    main()

    global super_list
    super_list = []

    health_player, health_boss = attributes()
    potion = 3
    tot = 0
    
    match_player = 0

    while health_player > 1 and health_boss > 1:
        took_potion = False
        tot += 1

        rounds = randint(1,2)  
        dodge_chance = randint(1,5)

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
                if dodge_chance != 1 and dodge_chance != 2:
                    critical_chance_player = randint(1, 10)
                    if critical_chance_player == 1:
                        health_boss = critical_player(health_boss)
                    else:
                        health_boss = player_attack(health_boss)
                        health_boss = super_player(health_boss)
                else:
                    dodge_player()

            elif rounds == 2:
                if dodge_chance != 1 and dodge_chance != 2:
                    critical_chance_boss = randint(1, 10)
                    if critical_chance_boss == 1:
                        health_player = critical_boss(health_player)
                    else:
                        health_player  = boss_attack(health_player)
                else:
                    dodge_boss()
                    

            if health_player <= 6 and potion > 0:
                cure_potion_player = input('press 1 to attack or 2 to drink a healing potion: ')
                health_player, potion, cure_potion_player, took_potion = cure_potion(health_player, potion, cure_potion_player, took_potion)
                print()

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