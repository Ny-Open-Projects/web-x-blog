from collections import deque

class KappaPipeline:
    """概念级 Kappa:一切皆流, 重算 = 回放日志。
    批处理等价于一次性回放全部历史事件。"""

    def __init__(self, window=3):
        self.log = deque()               # 持久化的事件日志
        self.window = window

    def append(self, value):
        self.log.append(value)

    def current_view(self):
        vals = list(self.log)[-self.window:]
        return sum(vals) / len(vals) if vals else None

    def recompute(self):
        """回放全量日志重算视图:与增量视图口径一致。"""
        vals = list(self.log)[-self.window:]
        return sum(vals) / len(vals) if vals else None

if __name__ == "__main__":
    p = KappaPipeline(window=3)
    for v in [1, 2, 3, 4]:
        p.append(v)
    assert p.current_view() == p.recompute(), "批流口径必须一致"
    print("view:", p.current_view(), "= recompute:", p.recompute())
