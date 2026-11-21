"""模拟 slowlog: 记录超阈值命令并给出治理建议"""
import time
from collections import deque

class SlowLog:
    def __init__(self, threshold_ms=1.0, maxlen=128):
        self.threshold, self.log = threshold_ms, deque(maxlen=maxlen)

    def execute(self, cmd, cost_ms):
        if cost_ms >= self.threshold:
            self.log.appendleft((time.strftime("%H:%M:%S"), cmd, cost_ms))

    def report(self):
        tips = {"KEYS": "生产禁用, 改 SCAN", "HGETALL": "大 hash 拆分或 HSCAN",
                "SMEMBERS": "改 SSCAN", "LRANGE0-1": "限制范围", "EVAL": "缩短脚本"}
        for ts, cmd, ms in self.log:
            head = cmd.split()[0]
            tip = tips.get(cmd, tips.get(head, "检查数据规模"))
            print(f"{ts} {ms:6.1f}ms {cmd}  -> {tip}")

if __name__ == "__main__":
    sl = SlowLog()
    sl.execute("GET user:1", 0.2)                  # 未超阈值不记录
    sl.execute("KEYS *", 850.0)
    sl.execute("HGETALL feed:2", 120.0)
    sl.execute("EVAL ...", 45.0)
    sl.report()
    print("配置: slowlog-log-slower-than 1000 (微秒), slowlog-max-len 128")
