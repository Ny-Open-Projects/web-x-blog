"""Agent 死循环检测与熔断:动作签名滑窗去重 + 无进展检测 + 熔断强制终止。"""
from collections import Counter, deque


class LoopBreaker:
    """以 动作签名+观测指纹 判断是否在空转:同签名反复出现或观测无变化即熔断。"""

    def __init__(self, repeat_limit=3, stale_limit=3, window=8):
        self.repeat_limit = repeat_limit
        self.stale_limit = stale_limit
        self.window = window
        self.signatures = deque(maxlen=window)
        self.observations = deque(maxlen=window)
        self.tripped = False
        self.reason = None

    @staticmethod
    def _sig(action, args):
        return action + "|" + ",".join(f"{k}={args[k]}" for k in sorted(args))

    def step(self, action, args, observation):
        """每次 Agent 循环调用一次:返回 True 表示放行,False 表示已熔断。"""
        if self.tripped:
            return False
        self.signatures.append(self._sig(action, args))
        self.observations.append(str(observation))
        most = Counter(self.signatures).most_common(1)[0]
        if most[1] >= self.repeat_limit and most[0] == self.signatures[-1]:
            self.tripped, self.reason = True, f"动作 {most[0]} 在近 {len(self.signatures)} 步重复 {most[1]} 次"
            return False
        if len(set(self.observations)) == 1 and len(self.observations) >= self.stale_limit:
            self.tripped, self.reason = True, f"连续 {len(self.observations)} 步观测无变化"
            return False
        return True


def run_agent(breaker, scripted):
    """脚本化 Agent 主循环桩:依次执行 (action,args,observation)。"""
    trace = []
    for action, args, obs in scripted:
        if not breaker.step(action, args, obs):
            trace.append(("halted", breaker.reason))
            break
        trace.append((action, obs))
    return trace


if __name__ == "__main__":
    # 场景 1:同一个搜索反复带相同参数
    b1 = LoopBreaker()
    t1 = run_agent(b1, [("search", {"q": "天气"}, "晴 25 度"),
                        ("search", {"q": "天气"}, "晴 25 度"),
                        ("search", {"q": "天气"}, "晴 25 度")])
    assert t1[-1][0] == "halted" and "重复" in b1.reason

    # 场景 2:参数在变,但页面观测始终一样(翻页被禁)
    b2 = LoopBreaker()
    t2 = run_agent(b2, [("next_page", {"p": 2}, "end of list"),
                        ("next_page", {"p": 3}, "end of list"),
                        ("next_page", {"p": 4}, "end of list")])
    assert t2[-1][0] == "halted" and "观测无变化" in b2.reason

    # 场景 3:正常推进,不应熔断
    b3 = LoopBreaker()
    t3 = run_agent(b3, [("search", {"q": "a"}, "r1"), ("open", {"id": 1}, "r2"),
                        ("extract", {"id": 1}, "r3"), ("finish", {}, "r4")])
    assert all(step[0] != "halted" for step in t3) and not b3.tripped
    print("死循环检测通过:重复签名熔断、观测停滞熔断、正常轨迹放行")
