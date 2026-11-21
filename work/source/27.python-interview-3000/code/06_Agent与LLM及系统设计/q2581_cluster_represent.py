"""Q2581 聚类的代表查询与长尾合并:报得出一二三,也兜得住其余。

每个簇选出现次数最多的原始写法当代表,低于支持度的簇整体并入
长尾桶,报表只展示头部,长尾合并计数,避免小簇淹没重点。
"""
from collections import Counter


def pick_representatives(groups, min_support):
    reps, tail = [], []
    for members in groups.values():
        if len(members) >= min_support:
            reps.append((Counter(members).most_common(1)[0][0], len(members)))
        else:
            tail.extend(members)
    reps.sort(key=lambda x: -x[1])
    return reps, tail


def main():
    groups = {
        "k1": ["Python GIL 是什么", "什么是 Python GIL", "python gil 是什么?"],
        "k2": ["redis 持久化", "Redis 持久化!", "Redis 持久化"],
        "k3": ["怎么买咖啡", "买咖啡"],
    }
    reps, tail = pick_representatives(groups, min_support=3)
    assert len(reps) == 2 and reps[0][1] == 3 and reps[1][1] == 3, reps
    assert tail == ["怎么买咖啡", "买咖啡"], tail
    reps2, tail2 = pick_representatives(groups, min_support=2)
    assert len(reps2) == 3 and tail2 == []
    print("代表查询:", reps)
    print("长尾合并条数:", len(tail), "→", tail)
    print("支持度降到 2 后:", reps2, "长尾", tail2)


if __name__ == "__main__":
    main()
