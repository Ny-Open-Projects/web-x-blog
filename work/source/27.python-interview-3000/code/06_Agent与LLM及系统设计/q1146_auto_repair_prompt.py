"""校验失败自动修复:错误注入 prompt,修复后重新全量校验,轮次封顶。"""
import json


def validate(obj):
    errs = []
    if "city" not in obj or not obj["city"]:
        errs.append("$.city: 必填,非空字符串")
    if not isinstance(obj.get("days"), int) or obj["days"] < 1:
        errs.append("$.days: 必须是 >=1 的整数")
    return errs


class RepairLLM:
    """第一次给坏输出,收到修复提示后给好输出的桩。"""

    def __init__(self):
        self.fixed = False

    def generate(self, prompt):
        if "只输出修正后的完整 JSON" in prompt:
            self.fixed = True
            return json.dumps({"city": "广州", "days": 2})
        return json.dumps({"city": "", "days": 0})


def run_with_repair(llm, task, schema_hint, max_repairs=2):
    raw = llm.generate(task)
    for i in range(max_repairs + 1):
        errs = validate(json.loads(raw))
        if not errs:
            return json.loads(raw), i
        repair_prompt = (
            f"原任务:{task}\n上次输出:{raw}\n错误列表:{json.dumps(errs, ensure_ascii=False)}\n"
            f"schema 提示:{schema_hint}\n只输出修正后的完整 JSON,不要解释。"
        )
        raw = llm.generate(repair_prompt)
    raise ValueError("修复轮次耗尽")


if __name__ == "__main__":
    llm = RepairLLM()
    obj, rounds = run_with_repair(llm, "提取行程信息", '{"city": str, "days": int>=1}')
    print(f"修复 {rounds} 轮后通过:", obj)
    assert obj == {"city": "广州", "days": 2}
    assert llm.fixed and rounds == 1, "应恰好一轮修复成功"
    print("修复后重新全量校验,闭环成立")
