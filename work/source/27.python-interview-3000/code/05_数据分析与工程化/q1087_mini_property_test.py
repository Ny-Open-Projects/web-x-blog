import random

def prop_len_preserved(input_list):
    out = sorted(set(input_list))  # 故意有 bug 的实现:去重导致长度不守恒
    return len(out) == len(input_list)

def shrink_list(xs, prop):
    """贪心缩小:逐个删元素,仍失败则保留更小反例"""
    current = list(xs)
    i = 0
    while i < len(current):
        candidate = current[:i] + current[i + 1:]
        if not prop(candidate):
            current = candidate
        else:
            i += 1
    return current

def run_property(prop, cases=50, seed=1):
    random.seed(seed)
    for _ in range(cases):
        xs = [random.randint(0, 3) for _ in range(random.randint(1, 8))]
        if not prop(xs):
            return shrink_list(xs, prop)
    return None

if __name__ == "__main__":
    minimal = run_property(prop_len_preserved)
    if minimal is None:
        print("本轮随机未触发 bug")
    else:
        print(f"发现最小反例: {minimal},重复元素被 sorted(set()) 丢弃")
