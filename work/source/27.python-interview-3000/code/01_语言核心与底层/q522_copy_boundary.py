from typing import Sequence

class Cart:
    def __init__(self, items: Sequence[str] = ()):
        self._items = list(items)             # 入参拷贝:与调用方脱钩

    def add(self, item: str) -> None:
        self._items.append(item)

    def items(self) -> tuple:
        return tuple(self._items)             # 出参只读化

if __name__ == "__main__":
    external = ["pen"]
    cart = Cart(external)
    external.append("eraser")
    print("caller list:", external)
    print("cart untouched:", cart.items())

    cart.add("book")
    snapshot = cart.items()
    cart.add("lamp")
    print("snapshot stays:", snapshot)
    print("current:", cart.items())
