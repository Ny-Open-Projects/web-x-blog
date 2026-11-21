"""多供应商统一信封:各家原始响应归一成统一结构,usage 字段对齐,finish_reason 映射。"""
FINISH_MAP = {
    "openai-like": {"stop": "completed", "length": "truncated", "tool_calls": "tool_use"},
    "anthropic-like": {"end_turn": "completed", "max_tokens": "truncated", "tool_use": "tool_use"},
}


def normalize(vendor, raw):
    if vendor == "openai-like":
        out = {"text": raw["choices"][0]["message"].get("content", ""),
               "finish": FINISH_MAP[vendor].get(raw["choices"][0]["finish_reason"], "unknown"),
               "tokens": {"in": raw["usage"]["prompt_tokens"],
                          "out": raw["usage"]["completion_tokens"]}}
    elif vendor == "anthropic-like":
        out = {"text": "".join(b.get("text", "") for b in raw["content"] if b.get("type") == "text"),
               "finish": FINISH_MAP[vendor].get(raw["stop_reason"], "unknown"),
               "tokens": {"in": raw["usage"]["input_tokens"],
                          "out": raw["usage"]["output_tokens"]}}
    else:
        raise ValueError("未知供应商 %s" % vendor)
    out["vendor"] = vendor
    return out


if __name__ == "__main__":
    a = normalize("openai-like", {"choices": [{"message": {"content": "你好"},
                                               "finish_reason": "stop"}],
                                  "usage": {"prompt_tokens": 10, "completion_tokens": 5}})
    b = normalize("anthropic-like", {"content": [{"type": "text", "text": "你好"}],
                                     "stop_reason": "end_turn",
                                     "usage": {"input_tokens": 10, "output_tokens": 5}})
    assert {k: v for k, v in a.items() if k != "vendor"} == {k: v for k, v in b.items() if k != "vendor"}, "两家异构响应归一成同一信封"
    t = normalize("openai-like", {"choices": [{"message": {"content": "截断了"}, "finish_reason": "length"}],
                                  "usage": {"prompt_tokens": 9, "completion_tokens": 100}})
    assert t["finish"] == "truncated", "finish_reason 映射到统一枚举"
    try:
        normalize("unknown-vendor", {})
        raise SystemExit("未知供应商应报错")
    except ValueError:
        pass
    print("统一信封通过:异构归一 finish 映射 未知供应商报错")
