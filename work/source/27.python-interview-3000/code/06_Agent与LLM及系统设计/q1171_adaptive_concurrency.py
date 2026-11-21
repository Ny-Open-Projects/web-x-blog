"""自适应并发:加性增乘性减 AIMD,429 退避,任务池随窗口伸缩。"""
import random, threading, time
from concurrent.futures import ThreadPoolExecutor


class AdaptiveLimiter:
    def __init__(self, initial=2, max_c=16):
        self.limit, self.max_c = initial, max_c
        self.lock = threading.Lock()
        self.cooldown_until = 0

    @property
    def value(self):
        return self.limit

    def on_success(self):
        with self.lock:
            self.limit = min(self.max_c, self.limit + 1)   # 加性增

    def on_429(self):
        with self.lock:
            self.limit = max(1, self.limit // 2)            # 乘性减
            self.cooldown_until = time.monotonic() + 0.05

    def wait_gate(self):
        while time.monotonic() < self.cooldown_until:
            time.sleep(0.005)


class BatchRunner:
    def __init__(self, llm, limiter):
        self.llm, self.limiter = llm, limiter

    def call(self, q):
        self.limiter.wait_gate()
        try:
            r = self.llm(q)
            self.limiter.on_success()
            return r
        except RuntimeError:
            self.limiter.on_429()
            raise

    def run(self, questions):
        done, pending = [], list(questions)
        while pending:
            batch, pending = pending[: self.limiter.value], pending[self.limiter.value:]
            try:
                with ThreadPoolExecutor(max_workers=self.limiter.value) as ex:
                    done += list(ex.map(self.call, batch))
            except RuntimeError:
                pending = batch + pending                  # 429 的整批退回重跑
        return done


class FlakyLLM:
    def __init__(self):
        self.calls = 0

    def __call__(self, q):
        self.calls += 1
        if self.calls in (3, 7):
            raise RuntimeError("429 Too Many Requests")
        return f"ok:{q}"


if __name__ == "__main__":
    runner = BatchRunner(FlakyLLM(), AdaptiveLimiter(initial=2))
    out = runner.run([f"q{i}" for i in range(12)])
    print("完成", len(out), "条,最终窗口", runner.limiter.value)
    assert len(out) == 12, "429 任务必须全部重试成功"
    assert runner.limiter.value >= 2
    print("AIMD 自适应限速收敛,窗口自动恢复")
