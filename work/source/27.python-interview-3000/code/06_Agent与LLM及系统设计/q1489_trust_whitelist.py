"""信任分级工具白名单:工具带信任分,分级放行,清洁运行升级、失败降级隔离。"""


class TrustRegistry:
    """工具信任注册表:0-100 信任分映射四级,放行规则与升降级闭环。"""

    TIERS = [(80, "verified"), (50, "trial"), (20, "watch"), (0, "quarantined")]

    def __init__(self, tools=None):
        self.score = {}                    # tool -> 信任分
        self.clean_streak = {}
        self.calls = []
        for name, s in (tools or {}).items():
            self.score[name] = s

    def tier(self, tool):
        s = self.score[tool]
        for floor, name in self.TIERS:
            if s >= floor:
                return name
        return "quarantined"

    def allow(self, tool, user_role="user"):
        """verified 直放;trial 与 watch 允许但降级记录;quarantined 仅管理员可临时放行。
        拒绝的调用同样写入审计,便于回溯谁在什么时候试图调用。"""
        t = self.tier(tool)
        if t == "quarantined" and user_role != "admin":
            self.calls.append((tool, t, False))
            return False, t
        self.calls.append((tool, t, True))
        return True, t

    def report(self, tool, ok):
        """运行反馈:成功累计清洁次数,连续 3 次成功升 10 分;失败清零并扣 15 分。"""
        if ok:
            self.clean_streak[tool] = self.clean_streak.get(tool, 0) + 1
            if self.clean_streak[tool] >= 3:
                self.score[tool] = min(100, self.score[tool] + 10)
                self.clean_streak[tool] = 0
        else:
            self.clean_streak[tool] = 0
            self.score[tool] = max(0, self.score[tool] - 15)

    def quorum_tools(self):
        return [t for t in self.score if self.tier(t) in ("verified", "trial")]


if __name__ == "__main__":
    reg = TrustRegistry({"web_search": 90, "code_run": 60, "mail_send": 30, "shell_exec": 5})
    assert reg.tier("web_search") == "verified"
    assert reg.tier("code_run") == "trial"
    assert reg.tier("mail_send") == "watch"
    assert reg.tier("shell_exec") == "quarantined"

    assert reg.allow("web_search")[0] is True
    assert reg.allow("shell_exec")[0] is False              # 普通角色拒绝
    assert reg.allow("shell_exec", user_role="admin")[0] is True
    assert [(c[0], c[2]) for c in reg.calls] == [("web_search", True), ("shell_exec", False), ("shell_exec", True)]

    for _ in range(3):                                      # 连续清洁 → 升 10 分
        reg.report("mail_send", True)
    assert reg.score["mail_send"] == 40 and reg.tier("mail_send") == "watch"
    for _ in range(6):
        reg.report("mail_send", True)                       # 40→50 越过 trial 线
    assert reg.tier("mail_send") == "trial"

    reg.report("code_run", False)                           # 失败扣分,可能滑向隔离
    assert reg.score["code_run"] == 45
    for _ in range(3):
        reg.report("code_run", False)                       # 45→30→15→0
    assert reg.tier("code_run") == "quarantined"
    assert sorted(reg.quorum_tools()) == ["mail_send", "web_search"]
    print("信任分级通过:四级放行、连续清洁升级、失败降级到隔离,管理员可临时放行")
