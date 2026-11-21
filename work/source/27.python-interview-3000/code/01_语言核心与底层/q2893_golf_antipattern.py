"""代码 golf 的反模式:一行流省掉的是可读性与可维护性。"""
from functools import reduce

data = [("alice", 88), ("bob", 45), ("carol", 92), ("dan", 60)]


def golf_pass(names):
    """golf 版:负数键排序 + 嵌套三元,意图要靠读者反推。"""
    return {k: ("及格" if v >= 60 else "补考") for k, v in sorted(names, key=lambda t: -t[1])}


def clear_pass(names):
    """可读版:命名的中间步骤与显式的 reverse 方向。"""
    ranked = sorted(names, key=lambda item: item[1], reverse=True)
    return {name: ("及格" if score >= 60 else "补考") for name, score in ranked}


def golf_total(names):
    """reduce + lambda 求和:绕远路,还引入一个不必要的外来概念。"""
    return reduce(lambda acc, t: acc + t[1], names, 0)


def clear_total(names):
    return sum(score for _, score in names)


def golf_side_effect(names):
    """把 append 副作用藏进推导式:能跑,review 时极易漏看。"""
    seen = []
    return [seen.append(name) or name.upper() for name, _ in names if len(seen) < 3]


def clear_take(names, limit=3):
    return [name.upper() for name, _ in names[:limit]]


if __name__ == "__main__":
    print("golf 版:", golf_pass(data))
    print("可读版:", clear_pass(data))
    print("两者一致:", golf_pass(data) == clear_pass(data))
    print("reduce 求和:", golf_total(data), "| sum 生成器:", clear_total(data))
    print("副作用藏进推导式:", golf_side_effect(data))
    print("等价的可读写法:", clear_take(data))
