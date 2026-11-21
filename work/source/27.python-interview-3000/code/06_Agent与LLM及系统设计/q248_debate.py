"""辩论模式:三个 Agent 独立作答、互相批驳并修订答案,裁判按收敛度裁决。"""
from collections import Counter


class Debater:
    def __init__(self, name, answer, policy):
        self.name, self.answer, self.policy = name, answer, policy

    def revise(self, others: list[str]) -> str:
        """看到对方答案后按策略修订自己的结论(真实场景由 LLM 完成)。"""
        self.answer = self.policy(others)
        return self.answer


def run_debate(debaters: list[Debater], judge, max_rounds: int = 3):
    for round_no in range(1, max_rounds + 1):
        for d in debaters:
            others = [x.answer for x in debaters if x is not d]
            print(f"  第{round_no}轮 {d.name} 修订为:{d.revise(others)}")
        votes = Counter(d.answer for d in debaters)
        if votes.most_common(1)[0][1] == len(debaters):
            print(f"  第{round_no}轮 全体收敛,提前结束")
            break
    return judge({d.name: d.answer for d in debaters})


def judge(answers: dict) -> str:
    return f"多数派结论:{Counter(answers.values()).most_common(1)[0][0]}"


if __name__ == "__main__":
    ds = [Debater("A", "方案1", lambda o: "方案1"),
          Debater("B", "方案1", lambda o: "方案1"),
          Debater("C", "方案2", lambda o: "方案1" if o.count("方案1") >= 2 else "方案2")]
    print(run_debate(ds, judge))
