"""frozen dataclass 的冻结与转换:from_dict、to_dict 与 replace 组合。"""
import dataclasses
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    @classmethod
    def from_dict(cls, raw):
        """外部输入到冻结对象:入口处完成归一化。"""
        return cls(x=float(raw["x"]), y=float(raw["y"]))

    def to_dict(self):
        return dataclasses.asdict(self)

    def moved(self, dx=0.0, dy=0.0):
        """派生修改:replace 返回新对象,原对象不变。"""
        return replace(self, x=self.x + dx, y=self.y + dy)


if __name__ == "__main__":
    p = Point.from_dict({"x": "1.5", "y": 2})
    print(p, "|", p.to_dict())

    q = p.moved(dx=1.0)
    print("派生新对象:", q, "| 原对象不变:", p)

    try:
        p.x = 99
    except dataclasses.FrozenInstanceError as e:
        print("冻结保护:", e)

    print("冻结对象可哈希,集合去重后:", len({p, q, p.moved()}))
