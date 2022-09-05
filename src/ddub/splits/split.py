from enum import Enum
from typing import List

from pydantic import BaseModel

from ddub.spells.spells import Spell
from ddub.weapons.weapons import Weapon


class SplitData(BaseModel):
    name: str
    available_spells: List[Spell]
    available_weapons: List[Weapon]


class Split(Enum):
    START = SplitData(
        name="Start",
        available_spells=[Spell.BOW],
        available_weapons=[Weapon.SWORD, Weapon.UMBRELLA],
    )

    MANOR = SplitData(
        name="Manor Entry",
        available_spells=[Spell.BOW],
        available_weapons=[Weapon.SWORD, Weapon.UMBRELLA, Weapon.DAGGERS],
    )

    POSTAVA1 = SplitData(
        name="Post Avarice 1",
        available_spells=[Spell.BOW, Spell.FIREBALL],
        available_weapons=[
            Weapon.SWORD,
            Weapon.UMBRELLA,
            Weapon.DAGGERS,
            Weapon.HAMMER,
        ],
    )

    POSTAVA2 = SplitData(
        name="Post Avarice 2",
        available_spells=[Spell.BOW, Spell.FIREBALL, Spell.BOMB],
        available_weapons=[
            Weapon.SWORD,
            Weapon.UMBRELLA,
            Weapon.DAGGERS,
            Weapon.HAMMER,
        ],
    )

    POSTAVA3 = SplitData(
        name="Post Avarice 3",
        available_spells=[Spell.BOW, Spell.FIREBALL, Spell.HOOKSHOT],
        available_weapons=[
            Weapon.SWORD,
            Weapon.UMBRELLA,
            Weapon.DAGGERS,
            Weapon.HAMMER,
            Weapon.GREATSWORD,
        ],
    )

    POSTSOULS = SplitData(
        name="Post Giant Souls",
        available_spells=[Spell.BOW, Spell.FIREBALL, Spell.HOOKSHOT],
        available_weapons=[
            Weapon.SWORD,
            Weapon.UMBRELLA,
            Weapon.DAGGERS,
            Weapon.HAMMER,
            Weapon.GREATSWORD,
        ],
    )
