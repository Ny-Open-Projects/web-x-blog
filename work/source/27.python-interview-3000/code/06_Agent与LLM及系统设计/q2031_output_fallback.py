"""输出格式退级链:严格 JSON → 宽松提取 → 模板兜底,逐级记录触发原因。"""
import json
import re


class FakeLLM:
    """桩:按脚本吐出预定输出,不联网。"""

    def __init__(self, script):
        self.script = list(script)

    def chat(self, _messages):
        return self.script.pop(0)


def strict_parse(text):
    return json.loads(text)


def lenient_parse(text):
    """宽松级:剥代码围栏,提取首个平衡大括号块,容忍尾逗号。"""
    fence_pat = "`" * 3 + r"(?:json)?\s*(.*?)" + "`" * 3
    fence = re.search(fence_pat, text, re.S)
    if fence:
        text = fence.group(1)
    start = text.find("{")
    if start < 0:
        raise ValueError("找不到 JSON 主体")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                candidate = re.sub(r",\s*([}\]])", r"\1", text[start:i + 1])
                return json.loads(candidate)
    raise ValueError("大括号不闭合")


def template_parse(text, fields):
    """模板级:正则逐字段抓,抓不到填默认值,绝不让整次调用报废。"""
    out = {}
    for name in sorted(fields):
        pattern, default = fields[name]
        m = re.search(pattern, text)
        out[name] = m.group(1) if m else default
    return out


def parse_with_chain(text, fields):
    try:
        return {"data": strict_parse(text), "level": "strict", "reason": None}
    except Exception as e1:
        try:
            return {"data": lenient_parse(text), "level": "lenient", "reason": str(e1)}
        except Exception as e2:
            return {"data": template_parse(text, fields),
                    "level": "template", "reason": str(e2)}


if __name__ == "__main__":
    FIELDS = {"amount": (r"金额[:：]\s*(\d+)", "0"),
              "city": (r"城市[:：]\s*(\S+)", "未知")}
    llm = FakeLLM([
        '{"amount": 42, "city": "杭州"}',                      # 干净 JSON
        '好的,结果如下:\n' + "`" * 3 + 'json\n{"amount": 42,}\n' + "`" * 3 + '\n请查收',  # 围栏加尾逗号
        '人工看了下,金额: 42 元,城市: 北京',                     # 自由文本
        '抱歉,我没算出来',                                     # 全兜底
    ])

    r1 = parse_with_chain(llm.chat([]), FIELDS)
    assert r1["level"] == "strict" and r1["data"] == {"amount": 42, "city": "杭州"}

    r2 = parse_with_chain(llm.chat([]), FIELDS)
    assert r2["level"] == "lenient" and r2["data"]["amount"] == 42
    assert r2["reason"], "退级必须留下严格级失败的原因"

    r3 = parse_with_chain(llm.chat([]), FIELDS)
    assert r3["level"] == "template"
    assert r3["data"] == {"amount": "42", "city": "北京"}

    r4 = parse_with_chain(llm.chat([]), FIELDS)
    assert r4["level"] == "template" and r4["data"] == {"amount": "0", "city": "未知"}
    print("退级链通过:strict→lenient→template 三级各就位,每级留触发原因")
