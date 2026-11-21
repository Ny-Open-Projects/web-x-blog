
READ = frozenset({"doc:read", "doc:list"})
WRITE = frozenset({"doc:read", "doc:list", "doc:write"})
ADMIN = WRITE | frozenset({"user:manage"})     # frozenset 支持集合运算


def can(granted, needed):
    """所需权限是否全部被授予:子集判定。"""
    return frozenset(needed) <= granted


def undirected_edges(pairs):
    """无向边去重:a-b 与 b-a 是同一条边——用 frozenset 作 key。"""
    seen = {}
    for a, b in pairs:
        edge = frozenset((a, b))
        seen[edge] = seen.get(edge, 0) + 1
    return {tuple(sorted(e)): n for e, n in seen.items()}


def normalize_tags(tags):
    """API 边界:接受任意可迭代,归一成不可变集合,防外部漂移。"""
    return frozenset(tags)


if __name__ == "__main__":
    print("can(ADMIN, [doc:write, user:manage]):",
          can(ADMIN, ["doc:write", "user:manage"]))
    print("can(READ, [doc:write]):", can(READ, ["doc:write"]))

    print("edges:", undirected_edges([("a", "b"), ("b", "a"), ("b", "c")]))

    tags = ["db", "cache", "db"]
    frozen = normalize_tags(tags)
    tags.append("evil")                         # 调用方继续改原列表
    print("frozen tags unaffected:", frozen)

    groups = {frozenset((1, 2)): "pair", frozenset((3,)): "single"}
    print("set-as-dict-key:", groups[frozenset((2, 1))])
    try:
        {{1, 2}: "x"}
    except TypeError:
        print("set literal key -> TypeError 不可哈希")
