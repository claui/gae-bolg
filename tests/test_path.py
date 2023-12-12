# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use, too-many-public-methods

from random import Random

from hypothesis import given, note, strategies as st
import hypothesis_networkx  # type: ignore
import networkx as nx
from networkx.readwrite.text import generate_network_text  # type: ignore

from gae_bolg import path

board_builder = hypothesis_networkx.graph_builder(
    graph_type=nx.Graph,
    node_keys=st.integers(),
    node_data=st.builds(dict),
    edge_data=st.builds(dict),
    min_nodes=2,
    max_nodes=16,
    min_edges=1,
    max_edges=None,
    self_loops=False,
    connected=True,
)


@st.composite
def draw_path_strategy(
    draw: st.DrawFn, random: st.SearchStrategy[Random]=st.randoms()
) -> tuple[nx.Graph, int, st.SearchStrategy[Random]]:
    graph = draw(board_builder)
    length: int = draw(st.integers(min_value=1, max_value=len(graph.nodes)))
    return graph, length, random


@given(draw_path_strategy())
def test_draw(draw_path_args: tuple[nx.Graph, int, Random]) -> None:
    graph: nx.Graph
    length: int
    random: Random
    graph, length, random = draw_path_args

    note("\n".join(["Called with graph:"] + list(generate_network_text(graph))))
    actual: list[int] = path.draw(graph, length, random)
    note(f"Returned path: {actual}")
    assert isinstance(actual, list)
    assert len(actual) == length
    assert nx.is_simple_path(graph, actual)  # type: ignore
