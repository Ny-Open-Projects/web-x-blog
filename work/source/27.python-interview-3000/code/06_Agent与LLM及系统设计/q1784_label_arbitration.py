"""双标注仲裁:两标注一致即采纳,不一致交资深终审,输出一致率报表。"""


def arbitrate(l1, l2, senior=None):
    if l1 == l2:
        return {"label": l1, "how": "agree"}
    if senior is None:
        return {"label": None, "how": "escalate"}   # 资深未表态:挂起
    return {"label": senior, "how": "senior_decides"}


class LabelingFlow:
    def __init__(self, senior_labels):
        self.senior = senior_labels                  # 资深仲裁预案:样本 -> 标签
        self.done = []
        self.agree = 0

    def process(self, sample_id, l1, l2):
        r = arbitrate(l1, l2, self.senior.get(sample_id))
        if r["how"] == "agree":
            self.agree += 1
        self.done.append(dict(r, sample_id=sample_id))
        return r

    def report(self):
        total = len(self.done)
        return {"total": total,
                "agreement_rate": self.agree / total if total else 0.0,
                "escalated": sum(1 for d in self.done if d["how"] == "senior_decides")}


if __name__ == "__main__":
    flow = LabelingFlow({"s2": "bad", "s4": "good"})
    flow.process("s1", "good", "good")               # 一致:直接采纳
    flow.process("s2", "good", "bad")                # 冲突:资深裁定
    flow.process("s3", "bad", "bad")
    flow.process("s4", "good", "bad")
    r5 = flow.process("s5", "good", "bad")           # 资深未表态:挂起
    assert r5 == {"label": None, "how": "escalate"}

    rep = flow.report()
    assert rep["total"] == 5 and rep["agreement_rate"] == 0.4
    assert rep["escalated"] == 2
    labels = {d["sample_id"]: d["label"] for d in flow.done}
    assert labels["s2"] == "bad" and labels["s4"] == "good"
    assert labels["s5"] is None, "挂起样本不入评估集"
    print("标注仲裁通过:一致即采纳 冲突交资深,一致率与升级数可量化")
