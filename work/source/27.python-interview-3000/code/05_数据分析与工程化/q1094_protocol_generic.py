from typing import Generic, Protocol, TypeVar, runtime_checkable

@runtime_checkable
class Closer(Protocol):
    def close(self) -> None:
        pass

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get(self) -> T:
        return self.item

class Conn:
    def close(self) -> None:
        print("conn closed")

def shutdown(resource: Closer) -> None:
    resource.close()

if __name__ == "__main__":
    shutdown(Conn())               # 结构满足协议,无需继承
    b: Box[int] = Box(3)
    print(b.get() + 1)
    print("isinstance 运行时检查:", isinstance(Conn(), Closer))
