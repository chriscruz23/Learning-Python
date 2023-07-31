from InventorySystem.weapon import Weapon, WeaponType

NAME = "Mithril Longsword"
DESC = "A sword made from mithril ore. A very capable weapon!"
WEIGHT = 100
W_TYPE = WeaponType.SWORD


def test_property_access() -> None:
    Weapon(NAME, DESC, WEIGHT, W_TYPE)
