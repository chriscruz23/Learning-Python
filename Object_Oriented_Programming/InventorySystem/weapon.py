from enum import Enum, auto

from item import Item


class WeaponType(Enum):
    SWORD = "Sword"
    MACE = "Mace"
    SPEAR = "Spear"
    BOW = "Bow"


class Weapon(Item):
    def __init__(
        self, name: str, description: str, weight: int, weapon_type: WeaponType
    ) -> None:
        super().__init__(name, description, weight)
        self.weapon_type = weapon_type

    @property
    def weapon_type(self) -> WeaponType:
        return self._weapon_type

    @weapon_type.setter
    def weapon_type(self, weapon_type: WeaponType) -> None:
        if not isinstance(weapon_type, WeaponType):
            raise TypeError("Must be a type of Weapon!")
        elif not type:
            raise ValueError("Weapon type cannot be left empty!")
        self._weapon_type = weapon_type

    def examine(self) -> str:
        return f"{self.name} ---- {self.description}\n \
            A {self.type.name} that {self.type.value.value} to cause its damage!"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Weapon):
            return sorted(self.__dict__) == sorted(other.__dict__)

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self) -> str:
        return f"{self.name} | Weight {self.weight} | Type {self.weapon_type.value}"

    def __repr__(self) -> str:
        return f"Weapon(name='{self.name}', description='{self.description}', weight={self.weight}, weapon_type={self.weapon_type})"
