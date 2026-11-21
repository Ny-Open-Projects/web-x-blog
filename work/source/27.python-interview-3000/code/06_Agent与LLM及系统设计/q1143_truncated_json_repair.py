"""截断 JSON 抢救:状态机补闭合符恢复部分字段,必填缺失时拒绝带病执行。"""
import json


def repair(buf):
    """返回 (repaired_obj, truncated, missing_reason)。"""
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
    fixed = buf + ('"' if in_str else "") + "".join("}" if c == "{" else "]" for c in reversed(stack))
    try:
        obj = json.loads(fixed)
        return obj, True, None
    except json.JSONDecodeError as e:
        return None, True, str(e)


def is_safe(obj, required):
    if obj is None:
        return False
    return all(k in obj and obj[k] not in ("", None) for k in required)


if __name__ == "__main__":
    truncated = '{"order": "A1001", "amount": 99.5, "items": ["书", "笔'
    obj, flag, err = repair(truncated)
    print("抢救结果:", obj, "截断:", flag)
    assert obj == {"order": "A1001", "amount": 99.5, "items": ["书", "笔"]}

    required = ["order", "amount", "status"]      # status 没来得及生成
    safe = is_safe(obj, required)
    print("必填完整性:", "可执行" if safe else "拒绝执行,走重试")
    assert not safe, "缺 status 必须拒绝带病执行"

    hopeless = '{"a": {"b": [1, "x" 2'
    obj2, _, err2 = repair(hopeless)
    print("不可修复样例:", obj2, err2)
    assert obj2 is None
    print("抢救器通过")
