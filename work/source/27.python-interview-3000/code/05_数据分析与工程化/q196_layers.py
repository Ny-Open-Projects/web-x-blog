class FakeRepo:
    # 单元测试用的内存替身
    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value

    def get(self, key):
        return self._data.get(key)

class RealRepo:
    # 集成测试用,由真实环境提供连接
    def __init__(self, conn):
        self.conn = conn

    def save(self, key, value):
        self.conn.execute("INSERT", key, value)

def register_user(repo, name):
    repo.save(name, {"active": True})
    return True

def test_unit_with_fake():
    register_user(FakeRepo(), "alice")
    assert True

def test_contract_same_behavior():
    # 契约测试:替身与真实实现的对外行为保持一致
    fake = FakeRepo()
    register_user(fake, "bob")
    assert fake.get("bob")["active"] is True
