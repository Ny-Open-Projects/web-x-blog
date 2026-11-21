"""JSON 深度限制: 防 RecursionError 与 C 栈溢出(纯标准库)。"""
import json

MAX_DEPTH = 64


def measure_depth(text, limit=MAX_DEPTH):
    """迭代扫描嵌套深度, 字符串内的括号不算; 超限或结构非法返回 -1, 否则返回最大深度。"""
    depth, in_str, esc, maxd = 0, False, False, 0
    for ch in text:
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
        elif ch in "[{":
            depth += 1
            maxd = max(maxd, depth)
            if depth > limit:
                return -1
        elif ch in "]}":
            depth -= 1
            if depth < 0:
                return -1
    if depth != 0 or in_str:
        return -1
    return maxd


def safe_loads(text):
    if measure_depth(text) == -1:
        raise ValueError("JSON 嵌套超限或结构非法")     # 由调用处捕获
    return json.loads(text)


deep = "[" * 5000 + "]" * 5000
try:
    json.loads(deep)
except RecursionError:
    print("直接 loads 深度 5000: RecursionError, 默认递归上限 1000 是最后防线而非设计")

try:
    safe_loads(deep)
except ValueError as e:
    print("safe_loads 拦下:", e)

legit = json.dumps({"a": {"b": [1, 2, {"c": 3}]}})
print("正常载荷深度:", measure_depth(legit), "解析:", safe_loads(legit))
crafted = "[" * 65 + "]" * 65
print("深度 65 载荷被限制拦截:", measure_depth(crafted) == -1)
