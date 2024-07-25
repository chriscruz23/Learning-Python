from item import Item


class OverEncumbered(Exception):
    """Carrying capacity has been exceeded."""


class Inventory:
    def __init__(self, capacity: int, items: list[Item] = None) -> None:
        self.stock = {}
        if items:
            for item in items:
                self.stock[item] = self.stock.get(item, 0) + 1
        self.capacity = capacity

    def __str__(self) -> str:
        return str([f"{value}x {item.name}" for item, value in self.stock.items()])
