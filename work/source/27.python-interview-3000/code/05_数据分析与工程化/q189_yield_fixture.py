try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

steps = []

@pytest.fixture
def a():
    steps.append("setup a")
    yield "a"
    steps.append("teardown a")

@pytest.fixture
def b(a):
    steps.append("setup b")
    yield f"b on {a}"
    steps.append("teardown b")

@pytest.fixture
def c(b):
    steps.append("setup c")
    yield f"c on {b}"
    steps.append("teardown c")

def test_order(c):
    # setup: a, b, c
    assert c == "c on b on a"

def test_teardown_order():
    # 上一个测试结束后,清理顺序是 c, b, a
    assert steps == ["setup a", "setup b", "setup c",
                     "teardown c", "teardown b", "teardown a"]
