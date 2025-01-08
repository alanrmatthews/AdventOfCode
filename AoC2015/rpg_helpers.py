"""Helpers for Day 21 and Day 22 solutions."""

from dataclasses import dataclass, field


@dataclass
class Equipment:
    """Equipment class"""

    name: str
    cost: int
    damage: int = 0
    armor: int = 0


@dataclass
class Spell:
    """Spell class"""

    name: str
    mana_cost: int
    duration: int = 0
    damage: int = 0
    healing: int = 0
    armor: int = 0
    mana_regen: int = 0


@dataclass
class Character:
    """Character class"""

    name: str
    hit_points: int
    damage: int
    armor: int
    mana: int = 0
    mana_spent: int = 0
    equipment_cost: int = 0
    shield_turns: int = 0
    poison_turns: int = 0
    recharge_turns: int = 0

    def add_equipment(self, equipment: Equipment):
        """Add equipment to character"""
        self.damage += equipment.damage
        self.armor += equipment.armor
        self.equipment_cost += equipment.cost

    def net_damage(self, other: "Character") -> int:
        """Returns net damage (our total damage - their total damage)"""
        our_damage = max(1, self.damage - other.armor)
        their_damage = max(1, other.damage - self.armor)
        return our_damage - their_damage


class Usables:
    """Class to hold usable items"""

    weapons: list = [
        Equipment("Dagger", 8, 4),
        Equipment("Shortsword", 10, 5),
        Equipment("Warhammer", 25, 6),
        Equipment("Longsword", 40, 7),
        Equipment("Greataxe", 74, 8),
    ]

    armor = [
        Equipment("None", 0, 0, 0),
        Equipment("Leather", 13, 0, 1),
        Equipment("Chainmail", 31, 0, 2),
        Equipment("Splintmail", 53, 0, 3),
        Equipment("Bandedmail", 75, 0, 4),
        Equipment("Platemail", 102, 0, 5),
    ]

    rings = [
        Equipment("None", 0, 0, 0),
        Equipment("Damage +1", 25, 1, 0),
        Equipment("Damage +2", 50, 2, 0),
        Equipment("Damage +3", 100, 3, 0),
        Equipment("Defense +1", 20, 0, 1),
        Equipment("Defense +2", 40, 0, 2),
        Equipment("Defense +3", 80, 0, 3),
    ]

    spells = (
        Spell("Magic Missile", 53, damage=4),
        Spell("Drain", 73, damage=2, healing=2),
        Spell("Shield", 113, duration=6, armor=7),
        Spell("Poison", 173, duration=6, damage=3),
        Spell("Recharge", 229, duration=5, mana_regen=101),
    )


def parse_input(input_file: str) -> Character:
    """Parse input file and return boss character"""
    with open(input_file, encoding="utf-8") as f:
        data = f.read().splitlines()
        boss = Character(
            "Boss",
            int(data[0].split(": ")[1]),
            int(data[1].split(": ")[1]),
            int(data[2].split(": ")[1] if len(data) > 2 else 0),
        )
    return boss
