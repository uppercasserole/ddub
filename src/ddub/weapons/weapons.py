import random
from enum import Enum
from typing import List


class Weapon(Enum):
    SWORD = "Reaper's Sword"
    DAGGERS = "Rogue Daggers"
    GREATSWORD = "Reaper's Greatsword"
    HAMMER = "Thunder Hammer"
    UMBRELLA = "Discarded Umbrella"


def generate_weapon(candidates: List[Weapon]) -> Weapon:
    return random.choice(candidates)
