from typing import Optional, Union

def parse(raw: Optional[str]) -> int:
    if raw is None:                       # 收窄:此后 raw 是 str
        return 0
    return int(raw)

def to_str(value: Union[int, str]) -> str:
    if isinstance(value, int):            # isinstance 分支收窄
        return str(value)
    return value.upper()

def get_setting(store: dict, key: str) -> int:
    value = store.get(key)
    if value is None:
        return 0
    return value                          # mypy 已知是 int

if __name__ == "__main__":
    print(parse(None), parse("42"))
    print(to_str(7), to_str("hi"))
    print(get_setting({"k": 5}, "k"), get_setting({}, "k"))
