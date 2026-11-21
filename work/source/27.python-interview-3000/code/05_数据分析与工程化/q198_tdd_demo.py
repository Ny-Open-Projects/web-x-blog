# Red:先写失败测试,定义期望行为
def test_split_name():
    from q198_tdd_demo import split_full_name  # noqa
    first, last = split_full_name("Ada Lovelace")
    assert first == "Ada"
    assert last == "Lovelace"

def test_split_name_single():
    from q198_tdd_demo import split_full_name
    # Green 阶段补的边界:只有一个词时 last 为空
    first, last = split_full_name("Cher")
    assert first == "Cher"
    assert last == ""

def split_full_name(full):
    # Refactor 后的实现:最小实现通过全部测试
    parts = full.split()
    if not parts:
        return "", ""
    return parts[0], " ".join(parts[1:])
