---
title: [Q1482] Agent 死循环检测与熔断:动作签名与观测停滞
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1482 · Agent 死循环检测与熔断:动作签名与观测停滞

> 难度:★★★★ | 标签:Agent, 死循环, 熔断

**问**:Agent 在生产里反复调用同一个搜索、或者翻页参数在变但页面永远返回同一内容,怎么自动发现并止损?

**答**:死循环有两种形态,要分别检测。第一种是动作签名重复:把工具名加排序后的参数哈希成签名,滑窗内同一签名出现达到阈值就熔断,这能抓住参数完全相同的重试循环。第二种是观测停滞:即使参数在变,只要连续多步的环境观测完全相同,说明行动没有产生任何信息增量,同样要熔断。熔断动作是立即终止主循环并向模型注入一条系统消息说明原因,让上层决定改写计划还是放弃。面试加分点在于指出这两个信号互补:只查签名会漏掉参数微调的假推进,只查观测会把合法的等待误判为死循环。

```python
# file: code/06_Agent与LLM及系统设计/q1482_loop_breaker.py
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
```

**追问**:
- 阈值怎么定? 答:经验上签名重复 3 次、观测停滞 3 步已经足够灵敏,滑窗取 8 步可以容忍偶发的合法重复;
- 熔断后怎么办? 答:记录熔断原因进轨迹,给用户降级话术,并把该任务标记为需要人工或换策略,而不是静默重启再循环一次。
