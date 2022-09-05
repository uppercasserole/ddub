import argparse
import random

from ddub.restrictions.restrictions import generate_restrictions
from ddub.skills.skills import generate_skill_levels
from ddub.spells.spells import generate_spells
from ddub.splits.split import Split, SplitData
from ddub.weapons.weapons import generate_weapon

parser = argparse.ArgumentParser(description="Death's Door Ultimate Bravery")
parser.add_argument(
    "--seed",
    default=None,
    help="The seed to use for reproducible challenges (default: random)",
)
parser.add_argument(
    "--soul",
    default=5300,
    type=int,
    help="How much soul should be available for upgrades (default: 5300)",
)
parser.add_argument("--difficulty", default=3, type=int, help="How cursed do you want it? (default: 3)")


args = parser.parse_args()
random.seed(args.seed)


def blurb(split: SplitData):
    print(f"# {split.name}")
    print(f"Weapon: {generate_weapon(split.available_weapons).value}")
    print(f"Spells: {' and '.join(spell.value for spell in generate_spells(split.available_spells))}")
    restrictions = ", ".join(
        f"{restriction.name} ({restriction.description})"
        for restriction in generate_restrictions(difficulty=args.difficulty)
    )

    if not restrictions:
        restrictions = "None"

    print(f"Restrictions: {restrictions}")
    print()


skill_levels = generate_skill_levels(soul=args.soul)

print("# Skills")
for skill, level in skill_levels.items():
    print(f"{skill.value}: {level}")

print()
print("If you disobey a restriction, you must immediately Save & Quit")
print()

for split in Split:
    blurb(split.value)
