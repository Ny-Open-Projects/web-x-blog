"""Q2571 工具黑白名单的运行时热切换:换表不换进程。

策略表是唯一事实源,切换用整体替换而不是逐项修补,版本号单调
递增;被 deny 的工具当场拦截并带版本信息,切换动作留痕可审计。
"""


class ToolGate:
    def __init__(self, policy):
        self._policy = dict(policy)
        self.version = 1
        self.log = []

    def switch(self, new_policy, reason):
        self.version += 1
        self._policy = dict(new_policy)
        self.log.append((self.version, reason))

    def check(self, tool):
        return self._policy.get(tool, "deny") == "allow"

    def call(self, tool):
        if not self.check(tool):
            raise PermissionError("tool denied by policy v" + str(self.version) + ":" + tool)
        return {"tool": tool, "ok": True}


def main():
    gate = ToolGate({"search": "allow", "calc": "allow"})
    assert gate.call("search")["ok"]
    gate.switch({"search": "deny", "calc": "allow"}, "审计发现搜索越权")
    try:
        gate.call("search")
        raise SystemExit(1)
    except PermissionError as exc:
        print("热切换后拦截:", exc)
    assert gate.call("calc")["ok"]
    assert gate.version == 2 and gate.log == [(2, "审计发现搜索越权")]
    gate.switch({"search": "allow", "calc": "allow"}, "审计整改通过恢复")
    assert gate.call("search")["ok"] and gate.version == 3
    print("当前版本:", gate.version, "切换记录:", gate.log)


if __name__ == "__main__":
    main()
