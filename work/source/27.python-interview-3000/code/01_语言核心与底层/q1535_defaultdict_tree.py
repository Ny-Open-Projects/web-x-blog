import json
from collections import defaultdict


def tree():
    return defaultdict(tree)


def wash(node):
    """把嵌套 defaultdict 递归洗回普通 dict,便于 JSON 与断言。"""
    return {key: wash(child) if isinstance(child, dict) else child
            for key, child in node.items()}


if __name__ == "__main__":
    index = tree()
    index["docs"]["q1526"]["title"] = "loop else"    # 任意深度缺键自动生长
    index["docs"]["q1527"]["title"] = "try else"
    index["meta"]["count"] = 45
    print("nested access:", index["docs"]["q1526"]["title"])

    # 分组:邻接表一行建
    edges = [("a", "b"), ("a", "c"), ("b", "d")]
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    print("adjacency:", dict(adj))

    # 计数桶
    counter = defaultdict(int)
    for ch in "mississippi":
        counter[ch] += 1
    print("count:", dict(counter))

    # 反面:读也会长键,ghost 键污染结构
    _ = index["ghost"]["deeper"]
    print("ghost leaked:", "ghost" in index)

    clean = wash(index)
    del clean["ghost"]                                # 洗净前删掉误访问
    print("json roundtrip:",
          json.dumps(clean, ensure_ascii=False, sort_keys=True))
