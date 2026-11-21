"""Q2987 结构化输出的完整校验层:解析-修复-重试。

LLM 输出不可信:可能带 markdown 代码栅栏、尾逗号、中文引号、前后
闲话。校验层三步:先剥栅栏提取 JSON 候选;解析失败做廉价自动修复;
仍失败则把错误信息拼回提示词,让模型带上下文重试,重试次数封顶。
栅栏字符用 chr(96)*3 运行时拼接,避免与文档围栏冲突。
"""
import json

FENCE = chr(96) * 3  # 反引号栅栏,运行时拼接


class FakeLLM:
    """依次吐出预设输出:第一轮带栅栏+闲话,第二轮干净 JSON。"""
    def __init__(self, outputs):
        self.outputs = list(outputs)

    def chat(self, prompt: str) -> str:
        return self.outputs.pop(0)


def strip_fences(raw: str) -> str:
    text = raw.strip()
    if text.startswith(FENCE):  # 剥掉开头栅栏(如 json 标注)到首个换行
        text = text[text.find("\n") + 1:]
    if text.endswith(FENCE):    # 剥掉结尾栅栏
        text = text[:-len(FENCE)].rstrip()
    return text.strip()


def cheap_fix(text: str) -> str:
    text = text.replace(",", ",")   # 中文逗号归一
    text = text.replace(":", ":")   # 中文冒号归一
    text = text.rstrip(",")
    if text.endswith("}"):          # 尾逗号修复
        text = text[:-2] + "}"
    return text


def extract_json(text: str):
    for cand in (text, cheap_fix(text)):
        try:
            return json.loads(cand)
        except (json.JSONDecodeError, ValueError):
            continue
    return None


def structured_call(llm, schema_hint: str, retries: int = 2):
    prompt = "输出 JSON,字段要求:" + schema_hint
    last_err = "no output"
    for _ in range(retries + 1):
        raw = llm.chat(prompt)
        body = strip_fences(raw)
        obj = extract_json(body)
        if obj is not None:
            return obj
        last_err = body[:60]
        prompt = ("你上次的输出无法解析(" + last_err +
                  "),请只输出合法 JSON,字段:" + schema_hint)
    raise ValueError("结构化输出解析失败:" + last_err)


if __name__ == "__main__":
    llm = FakeLLM([
        "好的,结果如下:" + FENCE + "json\n{'name': '订单A', 'qty': 2,}\n" + FENCE,
        FENCE + "json\n{\"name\": \"订单A\", \"qty\": 2}\n" + FENCE,
    ])
    obj = structured_call(llm, "name, qty")
    assert obj == {"name": "订单A", "qty": 2}, obj
    print("第一轮带栅栏/中文标点/尾逗号 → 自动修复失败 → 带错误重试成功:", obj)
