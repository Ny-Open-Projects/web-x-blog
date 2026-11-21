"""Prompt 回归:结构指纹快照 + 评估集打分门禁,新旧版本自动对比。"""


class FakeLLM:
    def __init__(self, behavior):
        self.behavior = behavior

    def generate(self, prompt):
        if "v2" in prompt:  # 模拟新版 prompt 的行为变化
            return '{"answer": "重试后再试", "intent": "售后", "confidence": 0.7}'
        return self.behavior


def fingerprint(output):
    """结构指纹:键集合 + intent 字段值,忽略易变的 confidence 数值。"""
    import json
    obj = json.loads(output)
    return {"keys": sorted(obj.keys()), "intent": obj.get("intent")}


EVAL_SET = [
    ("退货怎么操作", "intent=售后"),
    ("发票怎么开", "intent=售后"),
    ("今天天气如何", "intent=闲聊"),
]


def score(llm):
    ok = 0
    for q, expect in EVAL_SET:
        out = llm.generate(q)
        fp = fingerprint(out)
        want = expect.split("=")[1]
        ok += fp["intent"] == want
    return ok / len(EVAL_SET)


if __name__ == "__main__":
    v1 = FakeLLM('{"answer": "请联系客服", "intent": "售后", "confidence": 0.9}')
    v2 = FakeLLM('{"answer": "重试后再试", "intent": "售后", "confidence": 0.7}')
    base_fp = fingerprint(v1.generate("退货怎么操作"))
    new_fp = fingerprint(v2.generate("退货怎么操作"))
    print("v1 指纹:", base_fp)
    print("v2 指纹:", new_fp)
    assert base_fp["keys"] == new_fp["keys"], "输出 schema 漂移,拒绝上线"
    s1, s2 = score(v1), score(v2)
    print(f"回归分: v1={s1:.0%} v2={s2:.0%}")
    gate = s2 >= s1 - 0.02
    print("门禁结论:", "放行" if gate else "阻断")
    assert gate
