"""工具权限分级:注册表声明级别,执行器按级走 直接/审计/审批 三种门。"""


class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, level, fn, param_level=None):
        self.tools[name] = {"level": level, "fn": fn, "param_level": param_level}

    def effective_level(self, name, args):
        t = self.tools[name]
        if t["param_level"]:
            dynamic = t["param_level"](args)
            if dynamic:
                return dynamic
        return t["level"]


class Executor:
    def __init__(self, registry, approval_flow):
        self.registry, self.approvals = registry, approval_flow
        self.audit = []

    def execute(self, agent_clearance, name, args):
        level = self.registry.effective_level(name, args)
        order = {"READ": 0, "WRITE": 1, "DESTRUCTIVE": 2, "EXTERNAL": 3}
        if order[level] > order[agent_clearance]:
            raise PermissionError(f"{name} 需要级别 {level},Agent 只有 {agent_clearance}")
        if level in ("DESTRUCTIVE", "EXTERNAL"):
            ok = self.approvals(name, args)
            if not ok:
                self.audit.append((name, "denied"))
                raise PermissionError(f"{name} 未获审批")
            self.audit.append((name, "approved"))
        else:
            self.audit.append((name, "auto"))
        return self.registry.tools[name]["fn"](**args)


if __name__ == "__main__":
    reg = ToolRegistry()
    reg.register("search_docs", "READ", lambda q: f"results for {q}")
    reg.register("update_order", "WRITE", lambda order_id, note: f"order {order_id} updated")
    reg.register("delete_order", "DESTRUCTIVE", lambda order_id: f"order {order_id} deleted")
    reg.register("read_order", "READ", lambda order_id: f"order {order_id}",
                 param_level=lambda a: "DESTRUCTIVE" if a["order_id"] == "secret-1" else None)

    def human_gate(name, args):
        return name != "delete_order" or args["order_id"] != "root-1"   # 演示:删 root-1 拒批

    ex = Executor(reg, human_gate)
    print(ex.execute("READ", "search_docs", {"q": "政策"}))
    print(ex.execute("WRITE", "update_order", {"order_id": "o1", "note": "改地址"}))
    assert ("search_docs", "auto") in ex.audit

    try:
        ex.execute("WRITE", "delete_order", {"order_id": "o2"})
    except PermissionError as e:
        print("级别不足:", e)
    try:
        ex.execute("DESTRUCTIVE", "delete_order", {"order_id": "root-1"})
    except PermissionError as e:
        print("审批拒绝:", e)
    try:
        ex.execute("READ", "read_order", {"order_id": "secret-1"})
    except PermissionError as e:
        print("参数敏感升级:", e)
    print("四级门禁与参数级动态升级均生效")
