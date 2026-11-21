"""演示幂等工具:同一幂等键重复调用只执行一次,并支持断点恢复。"""
import hashlib


class IdempotentToolbox:
    def __init__(self):
        self.executed: dict[str, str] = {}   # 幂等键 -> 结果
        self.checkpoint: set[str] = set()    # 已完成步骤

    @staticmethod
    def make_key(task_id: str, step: int, params: dict) -> str:
        raw = f"{task_id}|{step}|{sorted(params.items())}"
        return hashlib.sha256(raw.encode()).hexdigest()[:12]

    def send_email(self, key: str, to: str, body: str) -> str:
        if key in self.executed:
            return f"[幂等命中] 返回缓存结果:{self.executed[key]}"
        result = f"邮件已发送给 {to}"
        self.executed[key] = result
        return result


if __name__ == "__main__":
    box = IdempotentToolbox()
    key = box.make_key("task_A", 3, {"to": "boss@x.com", "body": "日报"})
    print(box.send_email(key, "boss@x.com", "日报"))
    # 模拟崩溃后重跑,同一 key 再次调用
    print(box.send_email(key, "boss@x.com", "日报"))
