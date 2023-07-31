from enum import Enum, auto

from item import Item


class WeaponType(Enum):
    SWORD = "Sword"
    MACE = "Mace"
    SPEAR = "Spear"
    BOW = "Bow"


class Weapon(Item):
    def __init__(self, name: str, desc: str, weight: int, w_type: WeaponType) -> None:
        super().__init__(name, desc, weight)
        self.w_type = w_type

    @property
    def w_type(self) -> WeaponType:
        return self._w_type

    @w_type.setter
    def w_type(self, w_type: WeaponType) -> None:
        if not w_type:
            raise ValueError("Weapon type cannot be left empty!")
        elif not isinstance(w_type, WeaponType):
            raise TypeError("Must be a weapon type!")
        self._w_type = w_type

    def examine(self) -> str:
        return f"{self.name} ---- {self.desc}\n \
            A {self.w_type.name} that {self.w_type.value.value} to cause its damage!"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Weapon):
            return sorted(self.__dict__) == sorted(other.__dict__)

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self) -> str:
        return f"{self.name} | Weight {self.weight} | Type {self.w_type.value}"

    def __repr__(self) -> str:
        return f"Weapon(name='{self.name}', desc='{self.desc}', weight={self.weight}, w_type={self.w_type})"
