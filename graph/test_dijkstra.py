import unittest
from graph.dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    """Test implementation of Dijkstra's algorithm."""

    def setUp(self) -> None:
        # Input
        self.graph = {
            'start': {
                'a': 5,
                'c': 2,
            },
            'a': {
                'b': 4,
                'd': 2,
            },
            'b': {
                'd': 6,
                'finish': 3,
            },
            'c': {
                'a': 8,
                'd': 7,
            },
            'd': {
                'finish': 1,
            },
            'finish': {},
        }
        # Initial calculations
        infinity = float('inf')
        self.initial_costs = {
            'a': 5,
            'b': infinity,
            'c': 2,
            'd': infinity,
            'finish': infinity,
        }
        self.initial_parents = {
            'a': 'start',
            'b': None,
            'c': 'start',
            'd': None,
            'finish': None,
        }
        # Results
        self.cheapest_path = 8
        self.final_costs = {
            'a': 5,
            'b': 9,
            'c': 2,
            'd': 7,
            'finish': 8,
        }
        self.final_parents = {
            'a': 'start',
            'b': 'a',
            'c': 'start',
            'd': 'a',
            'finish': 'd',
        }

    def test_init(self):
        """Test init functionality."""
        dijkstra = Dijkstra(self.graph)
        self.assertEqual(dijkstra.graph, self.graph)
        self.assertEqual(dijkstra.costs, self.initial_costs)
        self.assertEqual(dijkstra.parents, self.initial_parents)
        self.assertIsNone(dijkstra.cheapest_path)

    def test_calc_cheapest(self):
        """Test calculation of the cheapest path."""
        dijkstra = Dijkstra(self.graph)
        self.assertEqual(dijkstra.calc_cheapest_path(), self.cheapest_path)
        self.assertEqual(dijkstra.cheapest_path, self.cheapest_path)
        self.assertEqual(dijkstra.costs, self.final_costs)
        self.assertEqual(dijkstra.parents, self.final_parents)

    def test_graph_with_loop(self):
        """Test graph with loop."""
        graph = {
            'start': {
                'a': 10,
            },
            'a': {
                'b': 20,
            },
            'b': {
                'c': 1,
                'finish': 30,
            },
            'c': {
                'a': 1,
            },
            'finish': {},
        }
        dijkstra = Dijkstra(graph)
        dijkstra.calc_cheapest_path()
        self.assertEqual(dijkstra.cheapest_path, 60)

    def test_graph_with_negative_edge(self):
        """Test graph with negative edge."""
        graph = {
            'start': {
                'a': 2,
                'b': 2,
            },
            'a': {
                'c': 2,
                'finish': 2,
            },
            'b': {
                'a': 2,
            },
            'c': {
                'b': -1,
                'finish': 2,
            },
            'finish': {},
        }
        dijkstra = Dijkstra(graph)
        with self.assertRaises(ValueError):
            dijkstra.calc_cheapest_path()

    def test_bfs_shortest_path(self):
        """Test search of the shortest path."""
        graph = {
            'cab': {
                'cat': 1,
                'car': 1,
            },
            'car': {
                'bar': 1,
            },
            'cat': {
                'mat': 1,
                'bat': 1,
            },
            'bar': {
                'bat': 1,
            },
            'mat': {
                'bat': 1,
            },
            'bat': {},
        }
        dijkstra = Dijkstra(graph, 'cab', 'bat')
        shortest_path = dijkstra.calc_cheapest_path()
        self.assertEqual(shortest_path, 2)


if __name__ == '__main__':
    unittest.main()
