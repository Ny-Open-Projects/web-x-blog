"""结构化输出重试:预算 + 指数退避 + 错误注入修复 prompt + 升级路径。"""
import json, random, time


class FlakyLLM:
    """前 2 次固定输出坏 JSON,第 3 次恢复(桩不模拟修复收益,只演示重试预算)。"""

    def __init__(self):
        self.calls = 0

    def generate(self, prompt):
        self.calls += 1
        if self.calls >= 3:
            return '{"city": "上海", "days": 2}'
        return "我觉得答案是 上海玩两天"          # 自然语言,不合法


def parse_with_retry(llm, prompt, max_attempts=3, budget_usd=0.5, cost_per=0.1):
    spent, errors = 0.0, []
    for attempt in range(1, max_attempts + 1):
        if spent + cost_per > budget_usd:
            return None, "budget_exhausted", spent
        repair_note = f"修复提示:上次输出不合法,错误={errors[-1]}" if errors else ""
        raw = llm.generate(prompt + repair_note)
        spent += cost_per
        try:
            obj = json.loads(raw)
            if not isinstance(obj, dict) or "city" not in obj:
                raise ValueError("缺少 city 字段")
            return obj, "ok", spent
        except Exception as e:
            errors.append(str(e))
            backoff = min(2 ** attempt + random.random() * 0.1, 1.0)
            time.sleep(backoff * 0.01)            # 演示用缩小 100 倍
    return None, "attempts_exhausted", spent


if __name__ == "__main__":
    llm = FlakyLLM()
    obj, status, spent = parse_with_retry(llm, "提取城市与天数:")
    print(f"状态={status} 结果={obj} 花费={spent:.1f} 尝试={llm.calls} 次")
    assert status == "ok" and obj["city"] == "上海"
    assert llm.calls == 3, "前两次失败,第 3 次成功"

    tight = FlakyLLM()
    obj2, status2, _ = parse_with_retry(tight, "提取:", max_attempts=5, budget_usd=0.25)
    print(f"小预算场景: 状态={status2}")
    assert status2 == "budget_exhausted", "预算护栏应先于尝试次数生效"
    print("重试预算护栏通过")
