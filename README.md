# ddub

## Death's Door Ultimate Bravery

This is a simple python project that generates settings for a Death's Door Ultimate Bravery challenge. What is that, you ask? A demonstration is in order!

Simply run the command like so:
```shell
python generate.py
```

And it will produce output like so:
```markdown
# Skills
Strength: 3
Dexterity: 2
Haste: 3
Magic: 1

# Start
Weapon: Discarded Umbrella
Spells: Bow
Restrictions: Dancer (You may only move by rolling)

# Manor Entry
Weapon: Reaper's Sword
Spells: Bow
Restrictions: No Deflect (You may not deflect projectiles), Running on empty (You may not swing your weapon if you have any mana)

# Post Avarice 1
Weapon: Rogue Daggers
Spells: Fireball
Restrictions: Carnivore (You may not consume soul fruit), Feeble (You may only use light attacks with your weapon)

# Post Avarice 2
Weapon: Discarded Umbrella
Spells: Fireball
Restrictions: Manahoarder (You may only cast spells when you have full mana), No Deflect (You may not deflect projectiles)

# Post Avarice 3
Weapon: Reaper's Sword
Spells: Fireball
Restrictions: Running on empty (You may not swing your weapon if you have any mana)

# Post Giant Souls
Weapon: Reaper's Greatsword
Spells: Bow
Restrictions: Muggle (You may not cast spells), Feeble (You may only use light attacks with your weapon)
```

Essentially, it creates a set of restrictions and requirements for various parts of your Death's Door Any% "speedrun". 

### The rules

1) If you accidentally break a restriction, you must immediately save and quit.
2) If the "Post Avarice 3" split requires the Reaper's Greatsword, you must go get it immediately. Use your current weapon and new spells/restrictions until then.
3) You are not required to pick up all weapons if you don't need to.
4) Have fun!

### Installation

In order to run it yourself:

1) Download the git repository
2) Navigate to the root of the project and do a `pip install .`
3) Now you can run the script with `python generate.py` and suffer the joys of randomly generated things
4) `python generate.py --help` will show you how to enter advanced options for modifying the difficulty

### Development

In order to set up this project for development:

1) Clone the git repository
2) Navigate to the root of the project and do a `pip install --editable .[dev]`
3) You should now have all the development dependencies installed and be able to run the tests

### 
