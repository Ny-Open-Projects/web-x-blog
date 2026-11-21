"""Agent 轨迹折叠:近 N 步保留原文,更早步骤折叠为一行台账,超预算再丢最旧行。"""
import json


def est_tokens(text):
    return max(1, len(text) // 2)            # 演示用粗估:2 字符 1 token


class TrajectoryFolder:
    """近详远略:verbatim 保留最近 keep_recent 步,旧步骤折叠成单行台账。"""

    def __init__(self, keep_recent=3, budget=10 ** 9):
        self.keep_recent = keep_recent
        self.budget = budget

    def fold(self, steps):
        """steps: [{action, args, result}] 按时间序,返回 (折叠文本, 报告)。"""
        old, recent = steps[:-self.keep_recent], steps[-self.keep_recent:]
        ledger = []
        for i, s in enumerate(old, 1):
            args = ",".join("%s=%s" % kv for kv in s["args"].items())
            ledger.append("步骤%d %s(%s) -> 已完成" % (i, s["action"], args))
        recent_text = [json.dumps(s, ensure_ascii=False) for s in recent]
        while ledger and est_tokens("\n".join(ledger + recent_text)) > self.budget:
            ledger = ledger[1:]                  # 超预算:从最旧的台账行开始丢
        text = "\n".join(ledger + recent_text)
        return text, {"ledger_lines": len(ledger), "verbatim_steps": len(recent)}


if __name__ == "__main__":
    steps = [{"action": "search", "args": {"q": "q%d" % i},
              "result": "结果" * 10} for i in range(8)]

    text, rep = TrajectoryFolder(keep_recent=3).fold(steps)
    assert rep == {"ledger_lines": 5, "verbatim_steps": 3}
    assert "步骤1 search(q=q0) -> 已完成" in text, "旧步骤折叠为台账行"
    assert '"result"' in text, "近 3 步保留完整工具结果"

    text2, rep2 = TrajectoryFolder(keep_recent=3, budget=130).fold(steps)
    assert rep2["ledger_lines"] < rep["ledger_lines"], "超预算时台账逐行丢弃"
    assert rep2["verbatim_steps"] == 3, "最近步骤永不折叠"
    assert est_tokens(text2) <= 130
    print("轨迹折叠通过:5 行台账加 3 步原文,紧预算再丢最旧行,近端永不折叠")
