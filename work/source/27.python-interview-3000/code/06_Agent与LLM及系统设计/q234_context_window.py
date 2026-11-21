"""实现一个带 token 预算的滑动窗口消息管理器,超限时丢最旧的非 system 消息。"""


class ContextWindow:
    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
        self.messages: list[dict] = [{"role": "system", "content": ""}]

    @staticmethod
    def _tokens(text: str) -> int:
        return max(1, len(text) // 2)  # 演示用估算

    def _total(self) -> int:
        return sum(self._tokens(m["content"]) for m in self.messages)

    def add(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})
        while self._total() > self.max_tokens and len(self.messages) > 1:
            removed = self.messages.pop(1)  # 保留 system,丢最旧一条
            print(f"  [裁剪] 丢弃旧消息:{removed['content'][:10]}...")

    def render(self) -> int:
        return self._total()


if __name__ == "__main__":
    cw = ContextWindow(max_tokens=30)
    cw.messages[0]["content"] = "你是助手"
    for i in range(5):
        cw.add("user", f"这是第{i}条比较长的用户消息,用来占 token")
        print(f"添加消息{i}后总 token ≈ {cw.render()},消息数 {len(cw.messages)}")
