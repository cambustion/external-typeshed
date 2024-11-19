import random
from _typeshed import Incomplete
from types import ModuleType
from typing_extensions import TypeAlias

import numpy

__all__ = [
    "flatten",
    "make_list_of_ints",
    "dict_to_numpy_array",
    "arbitrary_element",
    "pairwise",
    "groups",
    "create_random_state",
    "create_py_random_state",
    "PythonRandomInterface",
    "PythonRandomViaNumpyBits",
    "nodes_equal",
    "edges_equal",
    "graphs_equal",
    "_clear_cache",
]

_RandomNumberGenerator: TypeAlias = (
    ModuleType | random.Random | numpy.random.RandomState | numpy.random.Generator | PythonRandomInterface
)
_RandomState: TypeAlias = int | _RandomNumberGenerator | None

def flatten(obj, result: Incomplete | None = None): ...
def make_list_of_ints(sequence): ...
def dict_to_numpy_array(d, mapping: Incomplete | None = None): ...
def arbitrary_element(iterable): ...
def pairwise(iterable, cyclic: bool = False): ...
def groups(many_to_one): ...
def create_random_state(random_state: Incomplete | None = None): ...

class PythonRandomViaNumpyBits(random.Random):
    def __init__(self, rng: numpy.random.Generator | None = None) -> None: ...
    def getrandbits(self, k: int) -> int: ...

class PythonRandomInterface:
    def __init__(self, rng: Incomplete | None = None) -> None: ...
    def random(self): ...
    def uniform(self, a, b): ...
    def randrange(self, a, b: Incomplete | None = None): ...
    def choice(self, seq): ...
    def gauss(self, mu, sigma): ...
    def shuffle(self, seq): ...
    def sample(self, seq, k): ...
    def randint(self, a, b): ...
    def expovariate(self, scale): ...
    def paretovariate(self, shape): ...

def create_py_random_state(random_state: _RandomState = None): ...
def nodes_equal(nodes1, nodes2): ...
def edges_equal(edges1, edges2): ...
def graphs_equal(graph1, graph2): ...
def _clear_cache(G) -> None: ...
