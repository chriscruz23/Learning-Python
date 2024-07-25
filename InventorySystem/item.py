from abc import ABC, abstractmethod
from functools import cached_property


class EmptyArgumentError(TypeError):
    """Argument not supplied."""

    pass


class ReadOnlyPropertyError(AttributeError):
    """Property is read only."""

    pass


class Item(ABC):
    def __init__(self, name: str, desc: str, weight: int = 10) -> None:
        for arg, value in {name: "name", desc: "description", weight: "weight"}.items():
            self.validate_argument(arg, value)
        if not isinstance(weight, int):
            raise ValueError("Must be an integer type!")

        self._name = name
        self._desc = desc
        self._weight = weight

    @property
    def name(self) -> str:
        return self._name

    @property
    def desc(self) -> str:
        return self._desc

    @property
    def weight(self) -> str:
        return self._weight

    @name.setter
    def name(self, n: str) -> None:
        raise ReadOnlyPropertyError(f'Cannot change the "name" value.')

    @desc.setter
    def desc(self, d: str) -> None:
        raise ReadOnlyPropertyError(f'Cannot change the "description" value.')

    @weight.setter
    def weight(self, w: int) -> None:
        raise ReadOnlyPropertyError(f'Cannot change the "weight" value.')

    @abstractmethod
    @cached_property
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
    @cached_property
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
