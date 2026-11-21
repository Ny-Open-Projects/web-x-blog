
class UserBuilder:
    def __init__(self):
        self._data = {"id": 1, "name": "alice", "age": 30, "active": True}

    def with_name(self, name):
        self._data["name"] = name
        return self

    def with_age(self, age):
        self._data["age"] = age
        return self

    def inactive(self):
        self._data["active"] = False
        return self

    def build(self):
        return dict(self._data)

def is_active_minor(user):
    """业务规则:未成年且处于激活态是非法组合"""
    return user["age"] < 18 and user["active"]

if __name__ == "__main__":
    base = UserBuilder().build()
    minor = UserBuilder().with_age(17).build()
    minor_inactive = UserBuilder().with_age(17).inactive().build()
    assert not is_active_minor(base), "默认成年用户是合法组合"
    assert is_active_minor(minor), "未成年且激活正是要测的非法组合"
    assert not is_active_minor(minor_inactive), "未成年但未激活是合法组合"
    print(base, minor, minor_inactive)
