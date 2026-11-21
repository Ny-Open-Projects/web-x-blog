try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

@pytest.fixture
def base_config():
    return {"env": "test", "timeout": 5}

def test_uses_fixture(base_config):
    # 放在 tests/conftest.py 中即可被同目录所有测试直接使用
    assert base_config["env"] == "test"

def pytest_addoption(parser):
    # 实际项目写在 conftest.py 顶层,这里演示其内容
    parser.addoption("--env", default="test", help="指定测试环境")
