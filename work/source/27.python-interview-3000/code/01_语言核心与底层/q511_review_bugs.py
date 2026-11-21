def bug1_mutable_default(items=[]):
    items.append(1)
    return items

def bug2_is_vs_eq(a, b):
    return (a + b) is (a + b)             # 两次拼接是不同对象:不要用 is 比内容

def bug3_swallow():
    try:
        return int("x")
    except Exception:                     # 裸捕且不记录:错误静默丢失
        return None

def bug4_escaped_input(box=None):
    box = box if box is not None else {}
    box.setdefault("k", []).append(1)
    return box

if __name__ == "__main__":
    print(bug1_mutable_default(), bug1_mutable_default())
    print("is vs eq:", bug2_is_vs_eq("ab", ""))
    print("swallowed:", bug3_swallow())
    print(bug4_escaped_input(), bug4_escaped_input())
