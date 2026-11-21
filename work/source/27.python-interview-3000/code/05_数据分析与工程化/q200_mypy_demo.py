from typing import Optional


def find_user(user_id: int, cache: dict[int, str]) -> Optional[str]:
    # 返回值可能为 None,调用方必须处理
    return cache.get(user_id)


def send_welcome(name: str) -> str:
    # mypy 会报错:Argument 1 has incompatible type Optional[str]
    # return send_welcome(find_user(1, {}))
    user = find_user(1, {})
    if user is None:
        return "guest"
    return f"welcome {user}"


def test_none_handling():
    assert find_user(1, {}) is None
    assert send_welcome("ada") == "welcome ada"
