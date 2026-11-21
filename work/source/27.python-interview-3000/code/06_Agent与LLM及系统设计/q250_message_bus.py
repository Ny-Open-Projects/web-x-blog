"""消息总线 + 共享黑板:Agent 间只传引用与摘要,产物存黑板按需拉取。"""


class Blackboard:
    def __init__(self):
        self.artifacts: dict[str, str] = {}

    def put(self, key: str, content: str) -> str:
        ref = f"artifact::{key}"
        self.artifacts[key] = content
        return ref

    def get(self, ref: str) -> str:
        return self.artifacts.get(ref.removeprefix("artifact::"), "")


class MessageBus:
    def __init__(self, blackboard: Blackboard):
        self.board = blackboard
        self.inbox: dict[str, list[dict]] = {}

    def send(self, to: str, summary: str, ref: str = ""):
        self.inbox.setdefault(to, []).append({"summary": summary, "ref": ref})

    def receive(self, agent: str) -> list[dict]:
        msgs = self.inbox.pop(agent, [])
        for m in msgs:  # 接收方按需拉取全文
            if m["ref"]:
                m["full"] = self.board.get(m["ref"])[:20] + "..."
        return msgs


if __name__ == "__main__":
    board = Blackboard()          # 先建黑板再建总线,避免元组赋值右侧引用未定义名
    bus = MessageBus(board)
    ref = board.put("report_v1", "这是一份很长的行业分析报告全文..." * 3)
    bus.send("writer", "调研完成,请基于报告写稿", ref=ref)
    print("writer 收到:", bus.receive("writer"))
