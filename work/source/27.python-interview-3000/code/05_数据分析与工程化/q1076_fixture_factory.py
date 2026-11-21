
class UserStore:
    def __init__(self):
        self.users = []

    def add(self, name):
        user = {"id": len(self.users) + 1, "name": name}
        self.users.append(user)
        return user

def make_user_fixture(store):
    """pytest 真实用法:conftest 里 yield 这个工厂,测试内按需调用"""
    created = []

    def _make(name="alice", role="member"):
        user = store.add(name)
        user["role"] = role
        created.append(user)
        return user

    _make.created = created
    return _make

if __name__ == "__main__":
    store = UserStore()
    new_user = make_user_fixture(store)
    u1 = new_user()
    u2 = new_user("bob", role="admin")
    print(u1, u2)
    print("本次测试创建:", new_user.created, "清理时逐个回收即可")
