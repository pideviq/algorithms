from __future__ import annotations


class Dijkstra:
    """Dijkstra's algorithm implementation."""

    def __init__(self, graph: dict, start: str = 'start',
                 finish: str = 'finish') -> None:
        self.graph = graph
        self.start = start
        self.finish = finish
        self.costs = {}
        self.parents = {}
        self.processed = []
        self.cheapest_path = None
        infinity = float('inf')
        # Set initial costs of edges of a graph and parents of nodes
        for node in self.graph:
            if node == start:
                # Skip start node
                continue
            self.costs[node] = infinity
            self.parents[node] = None
        # Set cost and parent of start neighbors
        for node, weight in self.graph[start].items():
            self.costs[node] = weight
            self.parents[node] = start

    def calc_cheapest_path(self) -> int:
        """Calculate the cheapest path from start to finish."""
        if self.cheapest_path is None:
            while (node := self._get_cheapest_node()) is not None:
                for neighbor, neighbor_cost in self.graph[node].items():
                    # Catch negative-weight edge
                    if neighbor_cost < 0:
                        raise ValueError('negative-weight edge detected.'
                                         'Use Bellman-Ford algorithm instead')
                    new_cost = self.costs[node] + neighbor_cost
                    if new_cost < self.costs[neighbor]:
                        self.costs[neighbor] = new_cost
                        self.parents[neighbor] = node
                self.processed.append(node)
            self.cheapest_path = self.costs[self.finish]
        return self.cheapest_path

    def _get_cheapest_node(self) -> str | None:
        """Get unprocessed node with the lowest cost.

        Return None if no node found.
        """
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node, cost in self.costs.items():
            if node not in self.processed and cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
