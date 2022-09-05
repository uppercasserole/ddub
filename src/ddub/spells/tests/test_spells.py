from ddub.spells.spells import Spell, generate_spells


def test_main_spells():
    for _ in range(1, 100):
        assert generate_spells([Spell.BOW]) == [Spell.BOW]

    for _ in range(1, 100):
        assert generate_spells([Spell.FIREBALL]) == [Spell.FIREBALL]

    for _ in range(1, 100):
        assert generate_spells([Spell.BOMB]) == [Spell.BOMB]


def test_hookshot():
    empty = 0
    non_empty = 0

    for _ in range(1, 1000):
        result = generate_spells([Spell.HOOKSHOT])

        if not result:
            empty += 1
        elif result == [Spell.HOOKSHOT]:
            non_empty += 1
        else:
            raise AssertionError("Invalid response from generate_spells for HOOKSHOT")

    assert empty >= 333
    assert non_empty >= 333


def test_combo():
    one_spell = 0
    two_spells = 0

    for _ in range(1, 1000):
        result = generate_spells([Spell.BOW, Spell.HOOKSHOT])

        if result == [Spell.BOW]:
            one_spell += 1
        elif result == [Spell.BOW, Spell.HOOKSHOT]:
            two_spells += 1
        else:
            raise AssertionError("Invalid response from generate_spells for HOOKSHOT")

    assert one_spell >= 333
    assert two_spells >= 333


def test_spell_pick():
    bow = 0
    fireball = 0
    bomb = 0

    for _ in range(1, 1000):
        result = generate_spells([Spell.BOW, Spell.BOMB, Spell.FIREBALL])

        if result == [Spell.BOW]:
            bow += 1
        elif result == [Spell.BOMB]:
            bomb += 1
        elif result == [Spell.FIREBALL]:
            fireball += 1
        else:
            raise AssertionError("Invalid response from generate_spells for HOOKSHOT")

    assert bow >= 150
    assert bomb >= 150
    assert fireball >= 150
