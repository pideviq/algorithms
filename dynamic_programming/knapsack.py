from typing import Union, Dict, Optional


Capacity = Union[int, float]
Item = Dict[str, Capacity]
Inventory = Dict[str, Item]


class Knapsack:
    """Representation of knapsack problem."""

    def __init__(self, capacity: Capacity):
        """Create new knapsack.

        Arguments:
            capacity -- total capacity of knapsack (int or float number)
        """
        self.capacity = capacity

    def pick_items(self, inventory: Inventory, granularity: Capacity) -> set:
        """Return items that maximize fullness and value of a knapsack.

        Arguments:
            inventory -- dict of items and their specifications
            granularity -- the greatest common divisor of knapsack capacity and
                           items capacities
        """
        number_of_columns = int(self.capacity / granularity) + 1
        grid = [[item if column == 0 else {'total': 0, 'items': set()}
                 for column in range(number_of_columns)]
                for item in inventory]
        # The best choice by default (for empty inventory)
        cell = {'items': set()}

        # Iterate over items
        for i, row in enumerate(grid):
            item_name: Optional[str] = None
            # Iterate over sub-knapsacks
            for j, cell in enumerate(row):
                # The first cell always stores item name
                if not j:
                    item_name = cell
                    continue

                # The rest cells store total value and items of sub-knapsack
                value = inventory[item_name]['value']
                capacity = inventory[item_name]['capacity']
                cell_capacity = j * granularity
                old_max = grid[i - 1][j]['total'] if i > 0 else 0
                old_items = grid[i - 1][j]['items'] if i > 0 else set()

                if cell_capacity >= capacity:
                    # Enough space in sub-knapsack to put in an item
                    # Get a column number of the remaining space maximum value
                    remaining_col = int((cell_capacity - capacity)
                                        / granularity)
                    remaining_max = grid[i - 1][remaining_col]['total']\
                        if remaining_col > 0 else 0
                    remaining_items = grid[i - 1][remaining_col]['items']\
                        if remaining_col > 0 else set()
                    new_max = value + remaining_max
                    if new_max > old_max:
                        # Set new best value
                        cell['total'] = new_max
                        cell['items'] = remaining_items.copy()
                        cell['items'].add(item_name)
                        continue

                # Carry over the previous best value
                cell['total'] = old_max
                cell['items'] = old_items.copy()
        return cell['items']
