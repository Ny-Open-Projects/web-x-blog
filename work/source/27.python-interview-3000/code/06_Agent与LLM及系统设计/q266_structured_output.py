"""结构化输出:Schema 校验 + 带错误反馈的修复重试 + 兜底。"""
from __future__ import annotations
import json

SCHEMA = {"name": str, "age": int, "tags": list}


class FlakyLLM:
    """第一次输出坏 JSON,第二次输出缺字段,第三次正确。"""

    def __init__(self):
        self.n = 0

    def chat(self, messages):
        self.n += 1
        if self.n == 1:
            return "好的!{`name`: `李雷`, age: 25}"      # 非法 JSON
        if self.n == 2:
            return '{"name": "李雷", "tags": ["a"]}'       # 缺 age
        return '{"name": "李雷", "age": 25, "tags": ["a"]}'


def validate(obj: dict) -> list[str]:
    errors = []
    for k, typ in SCHEMA.items():
        if k not in obj:
            errors.append(f"缺少字段 {k}")
        elif not isinstance(obj[k], typ):
            errors.append(f"字段 {k} 应为 {typ.__name__}")
    return errors


def extract_json(text: str) -> str:
    text = text.strip().strip("`")
    start, end = text.find("{"), text.rfind("}")
    return text[start:end + 1] if start >= 0 and end > start else text


def structured_call(llm, max_retries: int = 3) -> dict | None:
    feedback = ""
    for attempt in range(1, max_retries + 1):
        raw = llm.chat([{"role": "user", "content": feedback or "输出 JSON"}])
        try:
            obj = json.loads(extract_json(raw))
        except json.JSONDecodeError as exc:
            feedback = f"你上次的输出不是合法 JSON({exc}),请只输出合法 JSON"
            continue
        errors = validate(obj)
        if not errors:
            print(f"第 {attempt} 次成功")
            return obj
        feedback = f"校验失败:{errors}。请按 Schema 补全后重新输出全部字段"
    return None


if __name__ == "__main__":
    print(structured_call(FlakyLLM()))
