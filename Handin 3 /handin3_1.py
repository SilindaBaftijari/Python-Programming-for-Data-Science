monster_level1 = 9
monster_level2 = 4
monster_level3 = 3

import random

def roll_dice(sides):
    """Simulate a dice roll with the given number of sides."""
    return random.randint(1, sides)

def game_play():
    """Simulate a battle between a hero and a monster using dice rolls."""
    
    hero_levels = [roll_dice(18), roll_dice(6), roll_dice(9)]
    
    print(f"Monster Levels: {monster_level1}, {monster_level2}, {monster_level3}")
    print(f"Hero Levels: {', '.join(map(str, hero_levels))}")
    
    if all(hero_level > monster_level for hero_level, monster_level in zip(hero_levels, [monster_level1, monster_level2, monster_level3])):
        print("Hero wins")
    else:
        print("Monster wins")

game_play()
