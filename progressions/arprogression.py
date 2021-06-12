from progresssion import Progression


class ArithmaticProgression(Progression):
    def __init__(self, start: int =0,stepsize :int =2):
        """
        Creates new Arithmetic progression.
        start       (int) Start of Arithemtic progression (default = 0)
        stepsize    (int) Fixed constant to be  added to each term (default = 2)
        """
        super().__init__(start=start)
        self._stepsize = stepsize

    def _advance(self):
        "Update current value by added fixed increment"
        ans = self._current
        self._current += self._stepsize
        return ans


if __name__ == "__main__":
    p = ArithmaticProgression(start=10, stepsize=5)
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    