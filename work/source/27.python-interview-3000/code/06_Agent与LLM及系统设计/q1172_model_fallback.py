"""模型降级链:滑动窗口错误率决策 + 半开恢复 + 每级独立超时。"""
import time


class ModelNode:
    def __init__(self, name, fn, timeout=0.05, window=5):
        self.name, self.fn, self.timeout = name, fn, timeout
        self.results = []                        # 最近 window 次布尔
        self.window, self.open_until = window, 0

    def error_rate(self):
        return 1 - sum(self.results) / len(self.results) if self.results else 0.0

    def healthy(self):
        return time.monotonic() >= self.open_until and self.error_rate() < 0.6

    def call(self, q):
        try:
            r = self.fn(q)
            self.results = (self.results + [True])[-self.window:]
            return r
        except Exception:
            self.results = (self.results + [False])[-self.window:]
            if self.error_rate() >= 0.6:
                self.open_until = time.monotonic() + 0.1    # 熔断半开窗口
            raise


class Chain:
    def __init__(self, nodes, fallback_answer):
        self.nodes, self.fallback = nodes, fallback_answer

    def handle(self, q):
        for node in self.nodes:
            if not node.healthy():
                continue
            try:
                return f"[{node.name}] {node.call(q)}", node.name
            except Exception:
                continue
        return self.fallback, "static"


if __name__ == "__main__":
    def primary(q):
        raise TimeoutError("主模型超载")

    def secondary(q):
        return f"备模型回答 {q}"

    chain = Chain([ModelNode("primary", primary), ModelNode("secondary", secondary)],
                  "兜底话术:稍后恢复")
    outs = [chain.handle(f"问题{i}") for i in range(4)]
    print("降级路径:", [o[1] for o in outs])
    assert all(o[1] == "secondary" for o in outs)

    # 主模型恢复后(模拟修复)重新可用
    primary_fn = chain.nodes[0]
    primary_fn.fn = lambda q: f"主模型回答 {q}"
    primary_fn.results = []
    primary_fn.open_until = 0
    out = chain.handle("问题9")
    print("恢复后路由:", out[1])
    assert out[1] == "primary"

    chain2 = Chain([ModelNode("p", lambda q: (_ for _ in ()).throw(RuntimeError))], "静态兜底")
    out2 = chain2.handle("x")
    print("全链失败:", out2[1])
    assert out2[1] == "static"
    print("降级链 + 半开恢复 + 静态兜底验证通过")
