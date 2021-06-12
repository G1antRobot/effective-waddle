#!/usr/bin/env python
from sys import version
from abc import ABCMeta
from typing import Iterator


class ABCProgression(metaclass=ABCMeta):
    def __init__(self, start :int, stepsize :int =1):
        self._current = start
        self._step = stepsize

    # Implement default iterator Interfaces
    def __next__(self) -> int:
        pass

    def __iter__(self) -> Iterator:
        pass

    # implement logic to update the progression

    def _advance():
        pass


class Progression(ABCProgression):
    """An basic step progression. default stepsize of 1. Implementated as Iterator class.
    """
    def __init__(self, start: int = 0) -> None:
        super().__init__(start=start)

    def _advance(self) -> None:
        self._current += 1

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration()
        else:
            ans = self._current # record as we need to return curent value at end
            self._advance()
            return ans  # start with first value

if __name__ == "__main__":
    p = Progression(start=10)
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))