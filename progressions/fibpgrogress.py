#!/usr/bin/env python

from progresssion import Progression

class FibonacciProgression(Progression):
    """ Iterator producing a generalized Fibonacci progression"""
    def __init__(self, first: int = 0 , second: int = 1) -> None:
        """ Creates a new Fibonacci preogression
        first   (int): first term of progression (default = 0)
        second  (int): Second term of progression (default = 1)
        """
        super().__init__(start=first)
        self._prev = second - first


    def _advance(self) -> None:
        self._prev , self._current = self._current , self._prev + self._current



if __name__ == "__main__":
    p = FibonacciProgression()
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