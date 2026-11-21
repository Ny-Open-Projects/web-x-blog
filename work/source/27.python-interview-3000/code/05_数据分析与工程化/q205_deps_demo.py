def resolve(specs: list[str]) -> dict[str, str]:
    # 极简示意:lock 的本质是给每个包固定一个精确版本
    return {name.split("==")[0]: name.split("==")[1] for name in specs}

def test_lock_is_exact():
    locked = resolve(["httpx==0.27.2", "anyio==4.4.0"])
    assert locked["httpx"] == "0.27.2"
    assert set(locked) == {"httpx", "anyio"}
