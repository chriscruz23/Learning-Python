from inventory import Inventory
from weapon import Weapon, WeaponType

weapons = [
    Weapon("Mithril Sword", "A pretty decent sword.", 80, WeaponType.blade),
    Weapon("Dragonite Spear", "An intimidating spear!", 110, WeaponType.spear),
    Weapon("Tarkov's Mallet", "Will definitely leave a bruise.", 150, WeaponType.mace),
    Weapon("Tarkov's Mallet", "Will definitely leave a bruise.", 150, WeaponType.mace),
    Weapon("Tarkov's Mallet", "Will definitely leave a bruise.", 150, WeaponType.mace),
    Weapon("Yule Shortbow", "In experienced hands, quite deadly.", 40, WeaponType.bow),
    Weapon("Rune dagger", "", 50, WeaponType.blade),
]

inv = Inventory(1000, weapons)
print(inv)
