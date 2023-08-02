from abc import ABC, abstractmethod


class EmptyArgumentError(Exception):
    """Argument not supplied."""

    pass


class Item(ABC):
    def __init__(self, name: str, desc: str, weight=10) -> None:
        self.name = name
        self.desc = desc
        self.weight = weight

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, n: str) -> None:
        self.validate_argument(n, "name")
        self._name = n

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, d: str) -> None:
        self.validate_argument(d, "description")
        self._desc = d

    @property
    def weight(self) -> str:
        return self._weight

    @weight.setter
    def weight(self, w: int) -> None:
        self.validate_argument(w, "weight")
        if not isinstance(w, int):
            raise TypeError("Weight must be a whole number!")
        self._weight = w

    @abstractmethod
    def examine(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @staticmethod
    def validate_argument(arg: str, method_name: str):
        if not arg:
            raise EmptyArgumentError(
                f"{method_name.capitalize()} cannot be left empty!"
            )
