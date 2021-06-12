from progresssion import Progression

class GeoProgression(Progression):
    def __init__(self, start: int , base :int = 2):
        """Creates Geometric progression

        start   (int) Start value for progression
        base    (int) fixed value for multiplying each term (default = 2)
        """
        super().__init__(start=start)
        self._base = base

    def _advance(self):
        "Updates current value by multiplying with base"
        ans = self._current
        self._current *= self._base
        return ans


if __name__ == "__main__":
    p = GeoProgression(start=20,base=15)
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))