"""循环 else 再辨析:没遇到 break 才执行,continue 与空序列都不影响。"""


def find(items, target):
    """for-else:找完没 break 走 else,天然表达未找到。"""
    for item in items:
        if item == target:
            return f"找到 {target}"
    else:
        return "遍历结束未找到"


def poll(max_attempts, succeed_at):
    """while-else:重试耗尽仍未成功,进 else 收场。"""
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        if attempts == 2:
            continue                # continue 不影响 else
        if attempts == succeed_at:
            break                   # 只有 break 跳过 else
    else:
        return f"重试 {max_attempts} 次仍未成功"
    return f"第 {attempts} 次成功"


if __name__ == "__main__":
    print(find([1, 2, 3], 3))
    print(find([1, 2, 3], 9))
    print(poll(5, 3))
    print(poll(5, 9))

    for _ in []:
        pass
    else:
        print("空序列同样进 else")

    for n in range(3):
        if n == 9:
            break
    else:
        print("没 break 就进 else,与异常无关")

    names = ["a", "b"]
    print("函数式替代:", "b" in names and "找到 b" or "未找到")
