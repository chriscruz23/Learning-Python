from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str, desc: str, weight=10) -> None:
        self.name = name
        self.desc = desc
        self.weight = weight

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if len(name) < 1:
            raise ValueError("Name cannot be left empty!")
        self._name = name

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, desc: str) -> None:
        if not desc:
            raise ValueError("Description cannot be left empty!")
        self._desc = desc

    @property
    def weight(self) -> str:
        return self._weight

    @weight.setter
    def weight(self, weight: int) -> None:
        if not isinstance(weight, int):
            raise TypeError("Weight must be a whole number!")
        self._weight = weight

    @abstractmethod
    def examine(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
