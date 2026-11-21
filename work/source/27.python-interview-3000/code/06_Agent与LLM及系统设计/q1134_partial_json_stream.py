"""分片 JSON 流式解析:补全闭合括号实现渐进解析,仅用于展示,执行用完整缓冲。"""


def try_partial_parse(buf: str):
    """把不完整 JSON 补闭合后尝试解析;引号内的花括号不参与配对。"""
    stack, in_str, esc = [], False, False
    for ch in buf:
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "{[":
            stack.append(ch)
        elif ch in "}]":
            if stack:
                stack.pop()
    patched = buf + ('"' if in_str else "") + "".join("}" if c == "{" else "]" for c in reversed(stack))
    try:
        return patched, json.loads(patched)
    except Exception:
        return None, None


import json

if __name__ == "__main__":
    deltas = ['{"city": ', '"北京", ', '"days": ', '3}']
    buf = ""
    for d in deltas:
        buf += d
        patched, obj = try_partial_parse(buf)
        print(f"收到分片 {d!r:>12} -> 渐进解析: {obj}")
    final = json.loads(buf)  # done 后用完整缓冲解析
    assert final == {"city": "北京", "days": 3}
    print("最终参数:", final, "可安全执行工具")
