from ddub.skills.skills import Skills, generate_skill_levels


def test_generate_skill_levels():
    for _ in range(1, 1000):
        assert 5 <= sum(generate_skill_levels(5300).values()) <= 9


def test_generate_skill_levels_min():
    for _ in range(1, 1000):
        assert sum(generate_skill_levels(400).values()) == 1


def test_generate_skill_levels_max():
    for _ in range(1, 1000):
        assert generate_skill_levels(4300 * 4) == {
            Skills.STR: 5,
            Skills.DEX: 5,
            Skills.HAS: 5,
            Skills.MAG: 5,
        }
