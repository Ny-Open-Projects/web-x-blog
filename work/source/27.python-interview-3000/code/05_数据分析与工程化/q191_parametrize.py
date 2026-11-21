try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

@pytest.mark.parametrize(
    "year,expected",
    [
        pytest.param(2000, True, id="整百年能整除400"),
        pytest.param(1900, False, id="整百年不能整除400"),
        pytest.param(2024, True, id="普通闰年"),
        pytest.param(2023, False, id="普通平年"),
    ],
)
def test_is_leap(year, expected):
    assert is_leap(year) is expected

@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [10, 20])
def test_cartesian(a, b):
    # 2x2 共 4 个用例
    assert a + b == b + a
