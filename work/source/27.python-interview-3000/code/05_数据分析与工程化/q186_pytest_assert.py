def add(a, b):
    return a + b

def test_add():
    # 裸 assert 即可,失败时 pytest 会展示 add(1, 2) 的实际值
    assert add(1, 2) == 3

def test_add_negative():
    result = add(-1, -2)
    # 失败时输出类似: assert -3 == -4  where -3 = add(-1, -2)
    assert result == -4

if __name__ == "__main__":
    # 手动验证:用 python -m pytest 运行本文件
    import subprocess, sys
    print("请用: python -m pytest q186_pytest_assert.py 运行")
