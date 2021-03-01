from Counter import Counter


class CounterImpl(Counter):
    __curentwheels: list[int]
    __maxwheels: list[int]

    def __init__(self) -> None:
        self.__currentwheels = [0]
        self.__maxwheels = [0]

    def init(self, liste: list[int]):
        self.__currentwheels = []
        for _ in liste:
            self.__currentwheels.append(0)
        self.__maxwheels = liste

    def current(self) -> list[int]:
        return self.__currentwheels

    def next(self):
        if self.__currentwheels != self.__maxwheels:
            if len(self.__currentwheels) == 1:
                self.__currentwheels[0] = self.__currentwheels[0] + 1
            if len(self.__currentwheels) == 2:
                self.__currentwheels[1] = self.__currentwheels[1] + 1

    def hasnext(self) -> bool:
        return self.__currentwheels != self.__maxwheels

    def nbpossiblevalues(self) -> int:
        return self.__maxwheels[0] + 1

    def nbremainingvalues(self) -> int:
        return self.__maxwheels[0] - self.__currentwheels[0]
