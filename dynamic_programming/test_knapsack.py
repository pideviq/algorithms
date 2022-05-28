import unittest
from dynamic_programming.knapsack import Knapsack


class TestKnapsack(unittest.TestCase):
    """Test solution to knapsack problem."""

    def setUp(self) -> None:
        self.capacity = 4
        self.granularity = 1
        self.inventory = {
            'stereo': {
                'capacity': 4,
                'value': 3_000,
            },
            'laptop': {
                'capacity': 3,
                'value': 2_000,
            },
            'guitar': {
                'capacity': 1,
                'value': 1_500,
            },
        }
        self.best_choice = {'laptop', 'guitar'}

    def test_knapsack_init(self):
        """Test creation of a new knapsack."""
        knapsack = Knapsack(self.capacity)
        self.assertEqual(self.capacity, knapsack.capacity)

    def test_pick_items(self):
        """Test picking algorithm."""
        knapsack = Knapsack(capacity=self.capacity)

        with self.subTest(msg='Strait order'):
            pick = knapsack.pick_items(self.inventory, self.granularity)
            self.assertEqual(self.best_choice, pick)

        with self.subTest(msg='Changed order'):
            inventory = {
                'guitar': self.inventory['guitar'],
                'laptop': self.inventory['laptop'],
                'stereo': self.inventory['stereo'],
            }
            pick = knapsack.pick_items(inventory, self.granularity)
            self.assertEqual(self.best_choice, pick)

        with self.subTest(msg='Expand inventory with iphone'):
            inventory = self.inventory.copy()
            new_item = {
                'iphone': {
                    'capacity': 1,
                    'value': 2_000,
                },
            }
            inventory.update(new_item)
            best_choice = {'iphone', 'laptop'}
            pick = knapsack.pick_items(inventory, self.granularity)
            self.assertEqual(best_choice, pick)

    def test_empty_inventory(self):
        """Test picking items from an empty inventory."""
        knapsack = Knapsack(capacity=self.capacity)
        inventory = {}
        pick = knapsack.pick_items(inventory, self.granularity)
        self.assertEqual(set(), pick)

    def test_fractional_granularity(self):
        """Test grid with fractional granularity."""
        places = {
            'Westminster Abbey': {
                'capacity': .5,
                'value': 7,
            },
            'Globe Theater': {
                'capacity': .5,
                'value': 6,
            },
            'National Gallery': {
                'capacity': 1,
                'value': 9,
            },
            'British Museum': {
                'capacity': 2,
                'value': 9,
            },
            "St Paul's Cathedral": {
                'capacity': .5,
                'value': 8,
            },
        }
        best_choice = {
            'Westminster Abbey',
            'National Gallery',
            "St Paul's Cathedral",
        }
        duration = 2
        vacation = Knapsack(capacity=duration)
        itinerary = vacation.pick_items(places, .5)
        self.assertEqual(best_choice, itinerary)

    def test_camping_problem(self):
        """Test solution to camping problem."""
        items = {
            'water': {
                'capacity': 3,
                'value': 10,
            },
            'book': {
                'capacity': 1,
                'value': 3,
            },
            'food': {
                'capacity': 2,
                'value': 9,
            },
            'jacket': {
                'capacity': 2,
                'value': 5,
            },
            'camera': {
                'capacity': 1,
                'value': 6,
            },
        }
        best_choice = {'water', 'food', 'camera'}
        granularity = 1
        knapsack_capacity = 6

        knapsack = Knapsack(knapsack_capacity)
        pick = knapsack.pick_items(items, granularity)
        self.assertEqual(best_choice, pick)


if __name__ == '__main__':
    unittest.main()
