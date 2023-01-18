
import random 

def player_is_alive(rpg_data) -> bool:
    """Checks if the player's HP is > 0

    Returns:
        bool: True if player's HP >0, else return False
    """
    if rpg_data["player_hp"] > 0:
        return True# Player setup #
    return False

def enemy_is_alive(rpg_data) -> bool:
    """checks if the enemy's HP is > 0

    Returns:
        bool: True if enemy's HP >0 else return False
    """
    if rpg_data["enemy_hp"] > 0:
        return True
    return False
    

def afficher_status(rpg_data) ->None:
    
    return rpg_data


def player_attack(rpg_data) -> None:
    """if player choosed "attack", enemy_hp decrease randomly by 10-20 HP
    """
    rpg_data["enemy_hp"] -= (10 + randint(10))
    if rpg_data["enemy_hp"] < 0:
        rpg_data["enemy_hp"] = 0
    

def player_heals(rpg_data) -> None:
    """if player choosed "potion", player_hp increase randomly by 17-25 HP potion_number decrease by 1
    """
    if rpg_data["potion_number"] >= 1:
        rpg_data["potion_number"] -= 1
        rpg_data["player_hp"] += (17 + randint(8))
        if rpg_data["player_hp"] > 50:
            rpg_data["player_hp"] = 50
    else:
        print("You don't have enough potions !")

def enemy_turn(rpg_data) -> None:
    """plays enemy's turn
    player's health should decrease randomly by 5-20 hp
    """
    rpg_data["player_hp"] -= (5 + randint(15))
    if rpg_data["player_hp"] < 0:
        rpg_data["player_hp"]= 0