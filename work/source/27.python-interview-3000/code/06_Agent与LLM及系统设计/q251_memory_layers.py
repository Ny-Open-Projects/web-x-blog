"""三层记忆的内存实现:短期窗口、滚动摘要、长期向量检索(假 embedding)。"""


class MemorySystem:
    def __init__(self, window_size: int = 3):
        self.window_size = window_size
        self.short_term: list[dict] = []
        self.summary: str = ""
        self.long_term: list[tuple[str, list[int]]] = []

    # ---- 短期:滑动窗口 ----
    def add_short(self, role: str, content: str):
        self.short_term.append({"role": role, "content": content})
        if len(self.short_term) > self.window_size * 2:
            dropped = self.short_term.pop(0)
            self._fold_to_summary(dropped)

    def _fold_to_summary(self, msg: dict):
        self.summary = (self.summary + " " + msg["content"])[:80]

    # ---- 长期:假向量检索 ----
    @staticmethod
    def fake_embed(text: str) -> list[int]:
        return [ord(c) % 10 for c in text[:8]]

    def add_long(self, fact: str):
        self.long_term.append((fact, self.fake_embed(fact)))

    def recall(self, query: str, k: int = 2) -> list[str]:
        qv = self.fake_embed(query)
        scored = sorted(self.long_term,
                        key=lambda x: -sum(a * b for a, b in zip(x[1], qv)))
        return [fact for fact, _ in scored[:k]]

    def build_context(self) -> list[dict]:
        msgs = []
        if self.summary:
            msgs.append({"role": "system", "content": f"历史摘要: {self.summary}"})
        if self.long_term:
            facts = self.recall("用户的偏好")
            msgs.append({"role": "system", "content": f"相关长期记忆: {facts}"})
        return msgs + self.short_term


if __name__ == "__main__":
    mem = MemorySystem(window_size=2)
    mem.add_long("用户偏好简洁回答")
    for i in range(4):
        mem.add_short("user", f"第{i}个问题,比较长的一句话")
    for m in mem.build_context():
        print(m["role"], ":", m["content"][:40])
