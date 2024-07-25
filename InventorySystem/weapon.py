from enum import Enum, auto

from item import Item


class WeaponType(Enum):
    @classmethod
    def items(cls):
        return [f"WeaponType.{c.name}" for c in cls]

    blade = "slashes"
    mace = "crushes"
    spear = "gouges"
    bow = "pierces"


class Weapon(Item):
    def __init__(self, name: str, desc: str, weight: int, w_type: WeaponType) -> None:
        for arg, value in {w_type: "weapon type"}.items():
            self.validate_argument(arg, value)
        if not isinstance(w_type, WeaponType):
            raise TypeError(f"Must be a weapon type! {WeaponType.items()}")

        super().__init__(name, desc, weight)
        self._w_type = w_type

    @property
    def w_type(self) -> WeaponType:
        return self._w_type

    @w_type.setter
    def w_type(self, w_type: WeaponType) -> None:
        raise Item.ReadOnlyPropertyError(f'Cannot change the "name" value.')

    def examine(self) -> str:
        return f"{self.name} ---- {self.desc}\n \
            A {self.w_type.name} that {self.w_type.value} to cause its damage!"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Weapon):
            return sorted(self.__dict__) == sorted(other.__dict__)

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Item):
            return self.name < other.name

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Item):
            return self.name > other.name

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self) -> str:
        return f"{self.name} | Weight {self.weight} | Type {self.w_type.value}"

    def __repr__(self) -> str:
        return f"Weapon(name='{self.name}', desc='{self.desc}', weight={self.weight}, w_type={self.w_type})"
