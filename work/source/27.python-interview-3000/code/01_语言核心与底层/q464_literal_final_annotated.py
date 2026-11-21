from typing import Literal, Final, Annotated, get_type_hints

Mode = Literal["read", "write", "append"]

MAX_RETRIES: Final = 3

Timeout = Annotated[int, "seconds", "gt=0"]

def open_file(path: str, mode: Mode = "read") -> str:
    return f"opened {path} with {mode}"

def connect(host: str, timeout: Timeout = 5) -> str:
    return f"connected {host} timeout={timeout}"

if __name__ == "__main__":
    print(open_file("a.txt"))
    print(open_file("a.txt", "write"))
    print(open_file("a.txt", "rw"))       # 运行时不拦:mypy 才报错
    print(connect("db.local"))
    print(get_type_hints(connect, include_extras=True))
    print("MAX_RETRIES:", MAX_RETRIES)
