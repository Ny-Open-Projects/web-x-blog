"""dataclass field 的 metadata:驱动序列化映射。"""
from dataclasses import dataclass, fields, field


@dataclass
class User:
    id: int = field(metadata={"wire": "user_id", "fmt": "int"})
    name: str = field(metadata={"wire": "full_name", "fmt": "str"})
    note: str = field(default="", metadata={"wire": None})  # None 表示不外发


def to_wire(obj):
    out = {}
    for f in fields(obj):
        wire = f.metadata.get("wire")
        if wire:
            out[wire] = getattr(obj, f.name)
    return out


def from_wire(cls, raw):
    kwargs = {}
    for f in fields(cls):
        wire = f.metadata.get("wire")
        if wire and wire in raw:
            kwargs[f.name] = raw[wire]
    return cls(**kwargs)


if __name__ == "__main__":
    u = User(7, "Ada")
    print("字段到线上名的映射:",
          {f.name: f.metadata.get("wire") for f in fields(u)})
    w = to_wire(u)
    print("to_wire:", w)
    print("from_wire 回读:", from_wire(User, w))
    print("note 不外发:", "note" not in w)
