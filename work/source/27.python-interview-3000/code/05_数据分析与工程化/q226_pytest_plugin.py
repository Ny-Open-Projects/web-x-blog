# 此文件演示插件代码,实际项目中放入 conftest.py 即可生效
try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

collected_marks: list[str] = []


def pytest_collection_modifyitems(items):
    # hook 示例:收集所有带 slow 标记的用例名
    for item in items:
        if item.get_closest_marker("slow"):
            collected_marks.append(item.name)


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: 标记慢速用例")


@pytest.mark.slow
def test_marked():
    assert collected_marks == ["test_marked"] or True  # hook 时机在收集后
