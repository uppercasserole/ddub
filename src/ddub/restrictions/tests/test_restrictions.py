from ddub.restrictions.restrictions import generate_restrictions


def test_generate_restrictions_groups_are_distinct():
    for _ in range(1, 1000):
        restrictions = generate_restrictions(difficulty=10)

        groups = [restriction.groups for restriction in restrictions]
        groups_size = sum([len(group) for group in groups])

        assert groups_size == len(set.union(*groups))


def test_generate_empty():
    for _ in range(1, 1000):
        assert not generate_restrictions(difficulty=-1)
