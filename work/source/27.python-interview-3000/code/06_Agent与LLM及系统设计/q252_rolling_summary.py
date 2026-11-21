"""滚动摘要:达到阈值时压缩旧历史,保留最近 N 轮原文。"""


class FakeSummarizer:
    def summarize(self, texts: list[str], prev_summary: str) -> str:
        joined = "; ".join(t[:8] for t in texts)
        return f"摘要[此前:{prev_summary[:12]}] + 新增:{joined}"


class RollingChat:
    def __init__(self, summarizer, threshold_msgs: int = 6, keep_recent: int = 2):
        self.sum, self.thr, self.keep = summarizer, threshold_msgs, keep_recent
        self.messages, self.summary = [], ""

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) >= self.thr:
            cut = len(self.messages) - self.keep
            old = [m["content"] for m in self.messages[:cut]]
            self.summary = self.sum.summarize(old, self.summary)
            self.messages = self.messages[cut:]
            print(f"  [压缩] 已摘要 {cut} 条,当前摘要长度 {len(self.summary)}")

    def status(self):
        return f"摘要={self.summary[:30]}... 原文{len(self.messages)}条"


if __name__ == "__main__":
    chat = RollingChat(FakeSummarizer(), threshold_msgs=6, keep_recent=2)
    for i in range(8):
        chat.add("user" if i % 2 == 0 else "assistant", f"第{i}轮对话内容若干字")
    print(chat.status())
