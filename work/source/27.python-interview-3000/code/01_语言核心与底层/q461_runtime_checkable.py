from typing import Protocol, runtime_checkable

@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None:
        """协议方法:只关心名字存在"""

class DBConn:
    def close(self) -> None:
        print("db closed")

class FileHandle:
    def close(self) -> None:
        print("file closed")

def close_all(resources):
    for r in resources:
        if isinstance(r, Closeable):      # 运行时结构检查:只看成员名
            r.close()

if __name__ == "__main__":
    close_all([DBConn(), FileHandle(), object()])
    print(isinstance(DBConn(), Closeable))
    print(issubclass(DBConn, Closeable))

    class Fake:
        close = 42                        # 签名完全不对也能通过
    print(isinstance(Fake(), Closeable))  # True:证明它不检查签名
