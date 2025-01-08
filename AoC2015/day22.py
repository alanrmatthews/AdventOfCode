"""Day 22: Wizard Simulator 20XX"""

import sys
from copy import deepcopy
from AoC2015.rpg_helpers import Character, Usables, parse_input, Spell
from Utilities.aoc_day import AdventOfCodeDay


class Day22(AdventOfCodeDay):
    """Day 22: Wizard Simulator 20XX"""

    def __init__(self, input_file: str):
        super().__init__(input_file)
        self.min_mana = sys.maxsize

    def part1(self):
        self.min_mana = sys.maxsize
        boss = parse_input(self.input_file)
        character = Character("Player", 50, 0, 0, 500)
        return min(self.battle(deepcopy(character), deepcopy(boss), spell, False) for spell in Usables.spells)

    def part2(self):
        self.min_mana = sys.maxsize
        boss = parse_input(self.input_file)
        character = Character("Player", 50, 0, 0, 500)
        return min(self.battle(deepcopy(character), deepcopy(boss), spell, True) for spell in Usables.spells)

    def battle(self, player: Character, boss: Character, spell: Spell, hard_mode: bool) -> int:
        """Returns minimum mana to win"""
        # Check for Hard mode debuff
        if hard_mode:
            player.hit_points -= 1
            if player.hit_points <= 0:
                return sys.maxsize

        # Execute Turn
        # Player Turn
        self.spell_effects(player, boss)

        player.mana -= spell.mana_cost
        player.mana_spent += spell.mana_cost

        if player.mana_spent >= self.min_mana:
            return sys.maxsize

        # Execute spell
        if spell.name == "Magic Missile":
            boss.hit_points -= spell.damage
        elif spell.name == "Drain":
            boss.hit_points -= spell.damage
            player.hit_points += spell.healing
        elif spell.name == "Shield":
            player.armor += spell.armor
            player.shield_turns = spell.duration
        elif spell.name == "Poison":
            player.poison_turns = spell.duration
        elif spell.name == "Recharge":
            player.recharge_turns = spell.duration

        # Boss's turn
        self.spell_effects(player, boss)
        player.hit_points -= max(1, boss.damage - player.armor)

        # Post-turn checks
        if boss.hit_points <= 0:
            self.min_mana = min(self.min_mana, player.mana_spent)
            return player.mana_spent

        if player.hit_points <= 0:
            return sys.maxsize

        next_turn_mana = player.mana if player.recharge_turns == 0 else player.mana + 101
        castable_spells = [spell for spell in Usables.spells if spell.mana_cost <= next_turn_mana]

        if player.shield_turns > 1 and Usables.spells[2] in castable_spells:
            castable_spells.remove(Usables.spells[2])

        if player.poison_turns > 1 and Usables.spells[3] in castable_spells:
            castable_spells.remove(Usables.spells[3])

        if player.recharge_turns > 1 and Usables.spells[4] in castable_spells:
            castable_spells.remove(Usables.spells[4])

        if len(castable_spells) == 0:
            return sys.maxsize

        return min(self.battle(deepcopy(player), deepcopy(boss), s, hard_mode) for s in castable_spells)

    def spell_effects(self, player, boss):
        """Execute spell effects"""
        if player.shield_turns > 0:
            player.shield_turns -= 1
            if player.shield_turns == 0:
                player.armor -= 7

        if player.recharge_turns > 0:
            player.mana += 101
            player.recharge_turns -= 1

        if player.poison_turns > 0:
            boss.hit_points -= 3
            player.poison_turns -= 1


# 900 too low
# 1242 too high
