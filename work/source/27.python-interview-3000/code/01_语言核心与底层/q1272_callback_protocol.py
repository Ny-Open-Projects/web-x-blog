from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Handler(Protocol):
    def __call__(self, event: str, payload: int) -> None: ...


def register(fn: Handler) -> None:
    if not callable(fn):                 # 运行时只做这个守门
        raise TypeError("need a callable")
    fn("start", 1)


if __name__ == "__main__":
    def my_handler(event, payload):
        print("got", event, payload)

    register(my_handler)
    print("isinstance my_handler:", isinstance(my_handler, Handler))
    print("isinstance 'text'    :", isinstance("text", Handler))
    print("isinstance print     :", isinstance(print, Handler),
          "<- 只查 __call__ 存在,不查签名")
