from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str, description: str, weight=10) -> None:
        self.name = name
        self.description = description
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
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        if len(description) < 1:
            raise ValueError("Description cannot be left empty!")
        self._description = description

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
