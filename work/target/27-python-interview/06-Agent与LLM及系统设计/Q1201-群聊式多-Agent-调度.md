---
title: [Q1201] 群聊式多 Agent 调度
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1201 · 群聊式多 Agent 调度

> 难度:★★★☆ | 标签:多 Agent, 调度

**问**:AutoGen 那种"拉个群"的协作方式,调度器怎么决定谁发言?怎么防无限循环?

**答**:群聊调度器维护发言规则:轮转(固定顺序)、路由(由 LLM 或规则选最相关的下一个发言者)、自选(每个 Agent 声明"我想发言"的意愿分数)。防失控三闸:最大轮数硬上限、重复检测(发言内容相似度过高即判收敛/僵局)、终止条件(出现 TERMINATE 意图或任务完成信号)。群聊的价值在观点碰撞,风险在成本(每轮全员可见,token 消耗 O(n²))——所以大群要控制历史窗口,只带最近 N 条。

```python
# file: code/06_Agent与LLM及系统设计/q1201_group_chat.py
"""群聊调度:路由选人 + 发言意愿分 + 轮数上限 + 僵局检测。"""
import re


class Participant:
    def __init__(self, name, interest):
        self.name, self.interest = name, interest      # interest: 关键词 -> 分
        self.history = None                            # 指向群聊历史(共享)

    def want_to_speak(self, last_msg):
        return sum(w for k, w in self.interest.items() if k in last_msg)

    def speak(self, msg):
        raise NotImplementedError


class GroupChat:
    TERMINATE = re.compile(r"同意|达成一致|task complete", re.I)

    def __init__(self, participants, max_rounds=6):
        self.members, self.max_rounds = participants, max_rounds
        self.history, self.cost = [], 0

    def run(self, topic):
        last = topic
        for rnd in range(self.max_rounds):
            scores = [(m.want_to_speak(last), m) for m in self.members]
            scores.sort(key=lambda x: -x[0])
            speaker = scores[0][1]
            if scores[0][0] == 0:
                print("  无人愿意发言,提前收敛")
                break
            msg = speaker.speak(last)
            self.history.append(msg)
            self.cost += len(self.history) + 10        # 全员可见,成本随历史增长
            print(f"  round{rnd}: {msg[:36]}")
            if self.TERMINATE.search(msg):
                print("  收到终止意图,结束")
                break
            if len(self.history) >= 2 and self.history[-1][:20] == self.history[-2][:20]:
                print("  检测到重复发言,僵局熔断")
                break
            last = msg
        return self.history, self.cost


if __name__ == "__main__":
    members = [
        Participant("planner", {"方案": 3, "计划": 2}),
        Participant("engineer", {"实现": 3, "成本": 2}),
        Participant("critic", {"风险": 3, "意见": 2}),
    ]
    chat = GroupChat(members, max_rounds=6)
    seq = ["方案已出,请评估实现成本", "成本可控,但有风险", "风险有缓解方案,同意,达成一致"]
    for m in members:
        m.history = chat.history                       # 共享群聊历史
        def make_speak(m):
            def speak(_msg):
                return f"{m.name}: {seq[min(len(m.history), 2)]}"
            return speak
        m.speak = make_speak(m)

    history, cost = chat.run("设计导出功能的方案与实现成本")
    assert 0 < len(history) <= 6, "轮数上限生效"
    assert chat.TERMINATE.search(history[-1]), "终止意图结束对话"
    print(f"群聊 {len(history)} 轮收敛,总成本 {cost}")
```

**追问**:
- 发言历史对每个成员都全量可见吗?答:默认可见但建议按"相关性窗口"裁剪(最近 N 条+摘要),成员多时全员广播成本平方级增长,可用主题分频道。
- 两个成员互相吹捧刷轮次怎么办?答:重复/相似度检测 + 每成员单题发言配额,超配额强制换人。
