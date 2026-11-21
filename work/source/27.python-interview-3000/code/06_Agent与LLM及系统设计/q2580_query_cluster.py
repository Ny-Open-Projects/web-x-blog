"""Q2580 查询日志的频次聚类:归一化后按同型合并计数。

日志里的查询十种写法一个意思:大小写 标点 词序 语助词都在抖。
先归一化成规范形(去标点 小写 字符集排序),同规范形即同一簇,
簇内计频,簇大小就是该意图的真实热度。
"""
import re
from collections import Counter

FILLER = set("的吗请一下什么哪些如何")


def normalize(q):
    q = re.sub(r"[^\w\u4e00-\u9fff]+", "", q.lower())
    return "".join(sorted(ch for ch in q if ch not in FILLER))


def cluster(queries):
    groups = {}
    for q in queries:
        groups.setdefault(normalize(q), []).append(q)
    return groups


def main():
    logs = ["Python GIL 是什么", "什么是 Python GIL", "python gil 是什么?",
            "GIL 的作用", "GIL 有什么用", "redis 持久化", "Redis 持久化!",
            "持久化 redis", "怎么买咖啡"]
    groups = cluster(logs)
    sizes = sorted((len(v) for v in groups.values()), reverse=True)
    assert sizes == [3, 3, 1, 1, 1], sizes
    top = max(groups.values(), key=len)
    assert top[0] == "Python GIL 是什么"
    rep = Counter(top).most_common(1)[0][0]
    print("簇数量:", len(groups), "簇大小分布:", sizes)
    print("最大簇成员:", top)
    print("代表查询:", rep)


if __name__ == "__main__":
    main()
