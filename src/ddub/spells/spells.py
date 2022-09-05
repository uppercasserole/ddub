import random
from enum import Enum
from typing import List


class Spell(Enum):
    BOW = "Bow"
    FIREBALL = "Fireball"
    BOMB = "Bomb"
    HOOKSHOT = "Hookshot"


def generate_spells(candidates: List[Spell]) -> List[Spell]:
    spells = []

    if Spell.HOOKSHOT in candidates:
        candidates = candidates.copy()
        candidates.remove(Spell.HOOKSHOT)

        if random.choice([True, False]):
            spells = [Spell.HOOKSHOT]

    if candidates:
        spells.insert(0, random.choice(candidates))

    return spells
