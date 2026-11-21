"""Q2576 降级模式的最小工具集:能力降配但核心链路不断。

把工具集按运行模式配成档位:full 全量,degraded 只留核心;
降级触发时整体切档,被裁工具的调用当场拦截,Agent 按预演好的
替代路径走缓存兜底,而不是临场报错找不到路。
"""

PROFILES = {
    "full": {"search": "allow", "calc": "allow", "mail": "allow"},
    "degraded": {"search": "deny", "calc": "allow", "mail": "deny"},
}


class Agent:
    def __init__(self, profile):
        self.profile = profile

    def use(self, tool):
        if PROFILES[self.profile].get(tool) != "allow":
            raise PermissionError(tool + " 在 " + self.profile + " 模式不可用")
        return tool + "-ok"


def plan_route(agent, need_search):
    if need_search:
        try:
            agent.use("search")
            return "live-search"
        except PermissionError:
            return "cache-fallback"
    agent.use("calc")
    return "calc-path"


def main():
    full = Agent("full")
    assert plan_route(full, True) == "live-search"
    assert plan_route(full, False) == "calc-path"
    degraded = Agent("degraded")
    assert plan_route(degraded, True) == "cache-fallback"
    assert plan_route(degraded, False) == "calc-path"
    blocked = False
    try:
        degraded.use("mail")
        raise SystemExit(1)
    except PermissionError as exc:
        blocked = True
        print("最小工具集拦截:", exc)
    assert blocked, "mail 应被降级档拦截"
    print("full 模式:", plan_route(full, True))
    print("degraded 模式:", plan_route(degraded, True), "核心链路 calc 仍可用")


if __name__ == "__main__":
    main()
