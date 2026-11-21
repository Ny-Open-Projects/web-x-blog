"""摘要轮转窗口:近 N 轮保原文,超预算时把最老消息折叠进滚动摘要。"""


class FakeLLM:
    def summarize(self, texts):
        # 桩:抽取句子中的"事实型"片段模拟摘要
        facts = [t for t in texts if any(k in t for k in ["叫", "偏好", "预算", "城市"])]
        return "已知事实:" + ";".join(facts) if facts else "暂无关键事实"


class RollingWindow:
    def __init__(self, budget_tokens=25, keep_recent=2):
        self.summary = ""
        self.recent = []                       # (role, content)
        self.budget, self.keep = budget_tokens, keep_recent
        self.llm = FakeLLM()

    def _tokens(self):
        return sum(len(c) for _, c in self.recent) + len(self.summary)

    def add(self, role, content):
        self.recent.append((role, content))
        self._compact()

    def _compact(self):
        while len(self.recent) > self.keep and self._tokens() > self.budget:
            oldest = [self.recent.pop(0)[1] for _ in range(min(2, len(self.recent) - self.keep))]
            new = self.llm.summarize(oldest)
            self.summary = (self.summary + ";" + new) if self.summary else new

    def build_messages(self):
        msgs = []
        if self.summary:
            msgs.append(("system", "历史摘要:" + self.summary))
        msgs.extend(self.recent)
        return msgs


if __name__ == "__main__":
    w = RollingWindow()
    dialog = [
        ("user", "我叫小王,偏好靠窗座位"),
        ("assistant", "好的已记录"),
        ("user", "帮我查去北京的航班,预算一千五"),
        ("assistant", "找到 3 个航班"),
        ("user", "最近天气怎么样"),
    ]
    for r, c in dialog:
        w.add(r, c)
    for m in w.build_messages():
        print(f"[{m[0]}] {m[1]}")
    assert "小王" in w.summary, "事实信息必须进摘要"
    assert len(w.recent) <= w.keep + 1
    print("轮转后保留原文", len(w.recent), "条,摘要长度", len(w.summary))
