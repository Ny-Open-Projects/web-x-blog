"""Agent 身份与最小权限:独立身份 + 能力表 + 委托不放大 + 审计。"""


class Identity:
    def __init__(self, name, capabilities):
        self.name, self.caps = name, set(capabilities)
        self.audit = []

    def _covers(self, action):
        if action in self.caps:
            return True
        prefix = action.split(":")[0]
        return f"{prefix}:*" in self.caps        # 通配能力覆盖同前缀

    def can(self, action):
        return self._covers(action)

    def delegate(self, child_name, child_caps):
        """委托:子身份能力必须是父能力(含通配)的子集。"""
        illegal = [c for c in child_caps if not self._covers(c)]
        assert not illegal, f"权限放大被拒绝: {illegal}"
        return Identity(child_name, child_caps)


class Resource:
    def __init__(self):
        self.rows = [{"id": 1, "owner": "u1", "secret": "salary"}]
        self.access_log = []

    def access(self, identity, action, resource_id):
        allowed = identity.can(f"{action}:{resource_id}") or identity.can(f"{action}:*")
        self.access_log.append((identity.name, action, resource_id, allowed))
        if not allowed:
            raise PermissionError(f"{identity.name} 无 {action} 权限 {resource_id}")
        return next(r for r in self.rows if r["id"] == resource_id)


if __name__ == "__main__":
    reader = Identity("research-agent", ["read:1", "read:2"])
    writer = Identity("ops-agent", ["read:*", "write:1"])
    res = Resource()

    row = res.access(reader, "read", 1)
    print("reader 读 row1: ok")
    try:
        res.access(reader, "write", 1)
    except PermissionError as e:
        print("越权被拒:", e)
    assert not reader.can("write:1")

    # 委托不放大:research 想给自己发写权限
    try:
        reader.delegate("sub-agent", ["write:1"])
    except AssertionError as e:
        print("委托放大拦截:", e)

    # 合法委托:只读子集(read:* 覆盖 read:1)
    sub = writer.delegate("helper", ["read:1"])
    assert sub.can("read:1") and not sub.can("write:1")
    print("合法委托成功,子权限是父的子集")

    res.access(sub, "read", 1)               # 子身份独立审计
    assert len({l[0] for l in res.access_log}) >= 2, "独立身份可审计"
    print("访问审计:", res.access_log)
