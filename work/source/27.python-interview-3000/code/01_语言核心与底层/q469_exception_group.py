import sys

def batch_process(items):
    errors = []
    results = []
    for i, item in enumerate(items):
        try:
            if item < 0:
                raise ValueError(f"negative item {i}")
            results.append(item * 2)
        except ValueError as e:
            errors.append(e)
    if errors:
        raise ExceptionGroup("batch failed", errors)   # 3.11+
    return results

if __name__ == "__main__":
    if sys.version_info < (3, 11):
        print(f"该特性需要 Python 3.11+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")
        sys.exit(0)

    # except* 是 3.11 新语法,只能放在字符串里按需编译执行
    demo = """
try:
    batch_process([1, -2, 3, -4])
except* ValueError as eg:
    print("value errors:", [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("type errors:", [str(e) for e in eg.exceptions])
"""
    exec(demo, globals())

    eg = ExceptionGroup("mixed", [ValueError("v"), TypeError("t")])
    print(type(eg).__name__, len(eg.exceptions))
    print("group message:", eg.message)
