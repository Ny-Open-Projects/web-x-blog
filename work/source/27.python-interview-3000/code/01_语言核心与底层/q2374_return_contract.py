"""返回契约三选一:None、raise 与空对象各自的适用场景。"""


class _User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"你好,{self.name}"


_USERS = {"u1": _User("张三")}


def find_user_none(uid):
    """缺失是常态:返回 None。"""
    return _USERS.get(uid)


class _Guest:
    """空对象:与真用户同接口,行为安全默认。"""
    name = "访客"

    def greet(self):
        return f"你好,{self.name}"


def find_user_null(uid):
    return _USERS.get(uid, _Guest())


class NotFoundError(LookupError):
    pass


def find_user_strict(uid):
    user = _USERS.get(uid)
    if user is None:
        raise NotFoundError(f"user {uid!r} 不存在")
    return user


if __name__ == "__main__":
    print("None 式:", find_user_none("u9"))

    guest = find_user_null("u9")
    print("空对象式:", guest.greet())
    print("命中真实用户:", find_user_null("u1").greet())

    try:
        find_user_strict("u9")
    except NotFoundError as exc:
        print("raise 式:", exc)

    try:
        find_user_none("u9").name
    except AttributeError as exc:
        print("None 式延迟爆炸:", exc)
