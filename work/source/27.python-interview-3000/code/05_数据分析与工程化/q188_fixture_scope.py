try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

@pytest.fixture(scope="session")
def db_pool():
    # 整个测试会话只创建一次
    return {"connected": True}

@pytest.fixture(scope="function")
def fresh_user(db_pool):
    # function 级依赖 session 级:合法
    return {"name": "alice", "db": db_pool}

def test_a(fresh_user):
    assert fresh_user["db"]["connected"]

def test_b(fresh_user):
    # fresh_user 在每个测试中都是新实例,测试间互不污染
    fresh_user["name"] = "bob"
    assert fresh_user["name"] == "bob"

def test_c(fresh_user):
    assert fresh_user["name"] == "alice"
