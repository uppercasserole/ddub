import random
from enum import Enum
from typing import Dict, Final, List


class Skills(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    HAS = "Haste"
    MAG = "Magic"


# Cummulative prices. Sum of (0, 400, 600, 800, 1000, 1500)
SKILL_PRICES: Final[List[int]] = [0, 400, 1000, 1800, 2800, 4300]


def generate_skill_levels(soul: int) -> Dict[Skills, int]:
    skill_levels = {Skills.STR: 0, Skills.DEX: 0, Skills.HAS: 0, Skills.MAG: 0}

    while True:
        available_skills = [skill for skill, level in skill_levels.items() if level == 0]
        available_levels = {level: price for level, price in enumerate(SKILL_PRICES) if 0 < price <= soul}

        if not available_skills or not available_levels:
            break

        skill = random.choice(available_skills)
        level = random.choice(list(available_levels.keys()))

        skill_levels[skill] = level
        soul -= SKILL_PRICES[level]

    while True:
        upgradable_skills = [
            skill
            for skill, level in skill_levels.items()
            if level < 5 and soul >= (SKILL_PRICES[level + 1] - SKILL_PRICES[level])
        ]

        if not upgradable_skills:
            break

        skill = random.choice(upgradable_skills)

        soul = soul - SKILL_PRICES[skill_levels[skill] + 1] + SKILL_PRICES[skill_levels[skill]]
        skill_levels[skill] += 1

    return skill_levels
