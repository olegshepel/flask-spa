from typing import Any
from typing import List, Set, Dict, Tuple, Optional
from typing import Callable, Iterator, Union, cast


def f() -> Tuple[int, str, float]:
    return 1, 'foo', 1.5

def g() -> Tuple[int, ...]:
    x: List[int] = [1, 2, 3, 4]
    return tuple(x)

# Could be Any instead of Union
def x() -> Tuple[Union[int, str], ...]:
    x: List[Any] = [1, 2, 3, '8']
    y: List[Union[int, float]] = [0, 1, 2, 3.0]
    return tuple(x)

def y() -> Tuple[int, ...]:
    x: List[int] = [1]
    return tuple(x)

# Variables
# Built-in
a: int  # without assignment
l1: list[int] = [9]
l2: set[str] = {'q'}
l3: Set[int] = {89}
res: Dict[str, int] = {'x': 0}
res2: dict[int, Optional[float]] = {1: 2.0, 2: None}

# Functions
def func(x: int, y: str, z: float = 7.89, xx=0) -> None:
    pass

def func_call(x: float, y: float) -> str:
    return ''

# This is how you annotate a callable (function) value
ppp: Callable[[int, float], str] = func_call

def func_new(*args: Any, **kwargs: str) -> None:
    pass

func_new(1, ggg='u')

aaa = [7]
b = cast(list[int], aaa)  # Passes fine
c = cast(list[str], aaa)  # Passes fine (no runtime check)

bb = cast(int, a)  # Passes fine
