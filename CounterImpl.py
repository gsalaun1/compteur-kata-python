from Counter import Counter


class CounterImpl(Counter):
    wheels = list

    def init(self, liste: list[int]):
        self.wheels = liste

    def current(self) -> list[int]:
        return self.wheels

    def next(self):
        pass

    def hasnext(self) -> bool:
        return False

    def nbpossiblevalues(self) -> int:
        return 1

    def nbremainingvalues(self) -> int:
        return 0
