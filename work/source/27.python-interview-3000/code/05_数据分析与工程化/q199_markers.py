import sys

try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

@pytest.mark.slow
def test_heavy_computation():
    # pytest -m "not slow" 会跳过它
    assert sum(range(1000)) == 499500

@pytest.mark.skipif(sys.platform == "win32", reason="仅 POSIX 行为")
def test_posix_only():
    assert "/" + "" == "/"

@pytest.mark.xfail(reason="已知 bug ISSUE-123")
def test_known_bug():
    # 预期失败:当前实现有 bug,修复后这里变 XPASS 提醒摘掉标记
    assert 1 / 0 == float("inf")

def test_fast():
    assert 2 + 2 == 4
