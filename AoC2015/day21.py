"""Day 21: RPG Simulator 20XX"""

from AoC2015.rpg_helpers import Character, Usables, parse_input
from Utilities.aoc_day import AdventOfCodeDay


class Day21(AdventOfCodeDay):
    """Day 21: RPG Simulator 20XX"""

    def part1(self):
        # This part should be easy, as long as attack-defense is greater for me than the
        # boss, I win. Find cheapest equipment that does this.
        boss = parse_input(self.input_file)
        return self.find_costs(boss)[0]

    def part2(self):
        boss = parse_input(self.input_file)
        return self.find_costs(boss)[1]

    def find_costs(self, boss: Character) -> tuple:
        """Returns (min_cost_to_win, max_cost_to_lose)"""
        # There's faster ways to do this, for example if a weapon by itself is sufficient, we don't
        # need to keep checking for the minimum cost. But this is simple, fast enough and works.
        min_cost = float("inf")
        max_cost = 0
        for weapon in Usables.weapons:
            for armor in Usables.armor:
                for ring1 in Usables.rings:
                    for ring2 in Usables.rings:
                        if ring1 == ring2 and ring1.name != "None":
                            continue
                        player = Character("Player", 100, 0, 0)
                        player.add_equipment(weapon)
                        player.add_equipment(armor)
                        player.add_equipment(ring1)
                        player.add_equipment(ring2)
                        if player.net_damage(boss) >= 0:
                            min_cost = min(min_cost, player.equipment_cost)
                        else:
                            max_cost = max(max_cost, player.equipment_cost)
        return (min_cost, max_cost)
