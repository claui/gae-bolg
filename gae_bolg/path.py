"""Path algorithms for generating a board"""

from collections.abc import Iterator
from random import Random

import networkx as nx


def draw(graph: nx.Graph, length: int, _random: Random = Random()) -> list[int]:
    """Return a random path of the given length in the given graph."""

    def random_paths() -> Iterator[list[int]]:
        for start_node in _random.sample(graph.nodes, k=len(graph.nodes)):
            yield from _random_paths_starting_at(graph, start_node, length, _random)

    if (path := next(random_paths(), None)) is None:
        raise ValueError("No path found")
    return path


def _random_paths_starting_at(
    graph: nx.Graph, source: int, length: int, random: Random
) -> Iterator[list[int]]:
    if length < 1:
        raise ValueError(length)
    if length == 1:
        yield [source]
    tail: nx.Graph = graph.copy()
    tail.remove_node(source)
    neighbors: list[int] = list(graph.neighbors(source))  # type: ignore
    next_node: int
    for next_node in random.sample(neighbors, k=len(neighbors)):
        yield from (
            [source] + p
            for p in _random_paths_starting_at(tail, next_node, length - 1, random)
        )
