"""keyword-only 与 positional-only:API 演进的安全阀。"""
import inspect


def create_user(name, /, *, role="member", active=True):
    # / 之前只能按位置;* 之后只能按关键字
    return {"name": name, "role": role, "active": active}


def legacy(name, role="member"):
    return {"name": name, "role": role}


if __name__ == "__main__":
    print("正常调用:", create_user("alice", role="admin"))
    try:
        create_user(name="bob")          # name 是 positional-only
    except TypeError as e:
        print("按关键字传 name:", str(e)[:48])
    try:
        create_user("carol", "admin")    # role 是 keyword-only
    except TypeError as e:
        print("按位置传 role:", str(e)[:48])
    print("签名自省:", str(inspect.signature(create_user)))
    print("旧接口兼容:", legacy("dave"))
