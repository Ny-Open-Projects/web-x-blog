from __future__ import annotations   # 注解惰性求值,低版本也可安全书写新式注解

from typing import Optional, TypeVar, Generic, TypedDict

T = TypeVar("T")

def first(items: list[T]) -> Optional[T]:   # 3.10+ 可写 T | None
    return items[0] if items else None

class Config(TypedDict):
    host: str
    port: int

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    def get(self) -> T:
        return self.item

if __name__ == "__main__":
    print(first([1, 2]), first([]))
    b: Box[str] = Box("hello")
    print(b.get().upper())
    cfg: Config = {"host": "localhost", "port": 8080}
    print(cfg)
    print(__import__("typing").get_type_hints(first))  # 运行时可读取注解
