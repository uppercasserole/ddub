import importlib.resources
import random
from typing import List, Set

import yaml
from pydantic import BaseModel, Extra, Field

import ddub.restrictions


class Restriction(BaseModel, extra=Extra.forbid):
    name: str = Field(..., description="The name of the restriction")
    description: str = Field(..., description="A description of what this restriction entails")
    groups: Set[str] = Field(
        ...,
        description="The list of string for determining which restrictions conflict",
    )
    difficulty: int = Field(
        ...,
        description="How difficult is this restriction. Higher=More difficult",
        ge=1,
        le=5,
    )


class RestrictionConfig(BaseModel, extra=Extra.forbid):
    restrictions: List[Restriction]


RESTRICTIONS = RestrictionConfig(
    **yaml.safe_load(importlib.resources.read_text(ddub.restrictions, "restrictions.yaml"))
).restrictions


def generate_restrictions(difficulty: int) -> List[Restriction]:
    chosen_restrictions: List[Restriction] = []
    difficulty += random.choice([-1, 0, 1])

    while difficulty > 0:
        available_restrictions = [
            potential_restriction
            for potential_restriction in RESTRICTIONS
            if potential_restriction.difficulty <= difficulty
            and (
                not chosen_restrictions
                or not potential_restriction.groups
                & Set.union(*[chosen_restriction.groups for chosen_restriction in chosen_restrictions])
            )
        ]

        if not available_restrictions:
            break

        restriction = random.choice(available_restrictions)
        chosen_restrictions.append(restriction)
        difficulty -= restriction.difficulty

    return chosen_restrictions
