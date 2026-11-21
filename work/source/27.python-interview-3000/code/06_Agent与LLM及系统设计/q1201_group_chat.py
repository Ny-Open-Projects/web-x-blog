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
