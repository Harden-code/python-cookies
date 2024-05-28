from typing import Callable
from typing import TypeVar, Protocol, Any
from collections.abc import Iterable
from pytest import mark


# def show_count(count: int, word: str) -> str:
#    if count == 1:
#        return f'1 {word}'
#    count_str = str(count) if count else 'no'
#    return f'{count} {word}'


# @mark.parametrize('qty,expected', [(1, '1 part'), (2, '2 part')])
# def test_show(qty, expected):
# got = show_count(qty, 'part')
# assert got == expected

# pytest *.py


def type_dic(key: str, value: int) -> dict[str, int]:
    mydic = {}
    mydic[key] = value
    return mydic


class Must_Lt(Protocol):
    def __lt__(self, other: Any) -> bool: ...


LT = TypeVar('LT', bound=Must_Lt)


def sort_helper(arr: Iterable[LT]) -> None:
    order = sorted(arr)
    for _ in order:
        print(_)


strs = ['1']
sort_helper(strs)


def func() -> None:
    print('func')


def re() -> Callable[..., None]:
    return func
