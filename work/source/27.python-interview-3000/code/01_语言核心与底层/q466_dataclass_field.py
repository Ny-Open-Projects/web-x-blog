from dataclasses import dataclass, field, InitVar

@dataclass
class Inventory:
    name: str
    tags: list = field(default_factory=list)          # 可变默认值的正确姿势
    qty: int = 0
    initial_qty: InitVar[int] = 0                     # 只参与初始化
    _cache: dict = field(init=False, default_factory=dict,
                         repr=False, compare=False)   # 内部缓存不参与比较

    def __post_init__(self, initial_qty):
        if initial_qty:
            self.qty = initial_qty

    @property
    def label(self):
        if "l" not in self._cache:
            self._cache["l"] = f"{self.name}:{self.qty}"
        return self._cache["l"]

if __name__ == "__main__":
    a = Inventory("apple", initial_qty=5)
    b = Inventory("banana", tags=["fresh"])
    print(a)
    print(b, b.label)
    print("eq:", a == Inventory("apple", initial_qty=5))
    print("initial_qty is a real field:", "initial_qty" in Inventory.__dataclass_fields__)
