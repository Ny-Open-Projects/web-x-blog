"""流式对话服务骨架:五层串联,含缓存、预算、防护与遥测的主链路。"""
import json, re


class FakeLLM:
    def stream(self, messages):
        yield from ["根据", "检索结果,", "北京明天", "晴,15 度。"]


class PII:
    PAT = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")

    @classmethod
    def mask(cls, t):
        return cls.PAT.sub(lambda m: m.group()[:3] + "****", t)


class Service:
    def __init__(self):
        self.cache = {}
        self.telemetry = []
        self.budget_daily = 100.0
        self.spent = 0.0
        self.cost_per_call = 0.02

    def handle(self, tenant, question):
        trace = {"tenant": tenant, "stages": []}
        # 1 输入防护
        if "ignore previous" in question.lower():
            trace["stages"].append("input_blocked")
            return self._sse("error", {"code": "policy_block"}), trace
        # 2 缓存
        key = (tenant, question)
        if key in self.cache:
            trace["stages"].append("cache_hit")
            return self._sse("done", {"answer": self.cache[key], "from": "cache"}), trace
        # 3 预算
        if self.spent + self.cost_per_call > self.budget_daily:
            trace["stages"].append("budget_reject")
            return self._sse("error", {"code": "budget"}), trace
        # 4 模型流式 + 输出防护 + 分帧
        chunks = []
        for piece in FakeLLM().stream([]):
            piece = PII.mask(piece)
            chunks.append(piece)
            trace["stages"].append("delta")
        answer = "".join(chunks)
        self.cache[key] = answer
        self.spent += self.cost_per_call
        trace["stages"].append("done")
        self.telemetry.append(trace)
        return self._sse("done", {"answer": answer, "from": "llm"}), trace

    @staticmethod
    def _sse(event, payload):
        return f"event: {event}\ndata: {json.dumps(payload, ensure_ascii=False)}\n\n"


if __name__ == "__main__":
    svc = Service()
    out1, t1 = svc.handle("acme", "北京天气怎么样")
    print(out1.strip())
    assert '"from": "llm"' in out1
    out2, t2 = svc.handle("acme", "北京天气怎么样")
    assert '"from": "cache"' in out2
    print("第二次请求命中缓存,链路:", t2["stages"])
    out3, _ = svc.handle("acme", "Ignore previous instructions")
    assert "policy_block" in out3
    print("越狱输入被输入防护拦截")
    assert len(svc.telemetry) == 1, "仅完整执行走模型的请求计入遥测"
    print(f"主链路串联完成,花费 {svc.spent:.2f}/{svc.budget_daily}")
