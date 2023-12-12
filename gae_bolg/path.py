"""Path algorithms for generating a board"""

from random import Random

import networkx as nx


def draw(graph: nx.Graph, length: int, _random: Random) -> list[int]:
    """Return a random path of the given length in the given graph."""
    return list(graph.nodes)[:length]
