"""路径分析的 top-k 序列: 前缀树计数与回环压缩"""

SESSIONS = [
    ["首页", "搜索", "商品详情", "支付"],
    ["首页", "搜索", "商品详情", "加购", "支付"],
    ["首页", "搜索", "商品详情", "加购", "支付"],
    ["首页", "搜索", "商品详情", "搜索", "商品详情", "支付"],
    ["首页", "搜索", "商品详情", "加购"],
    ["首页", "分类", "商品详情", "加购", "支付"],
    ["首页", "分类", "商品详情", "支付"],
    ["首页", "分类", "商品详情", "分类", "商品详情", "加购", "支付"],
    ["首页", "搜索", "支付"],
    ["首页", "活动页", "商品详情", "支付"],
    ["首页", "搜索", "商品详情", "加购", "支付"],
    ["首页", "分类", "商品详情", "加购", "支付"],
]


def compress_loop(path):
    """回环压缩: 同一页面在一条会话内只保留首次出现"""
    seen, out = set(), []
    for p in path:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def build_trie(paths):
    root = {"count": 0, "ends": 0, "children": {}}
    for p in paths:
        node = root
        node["count"] += 1
        for step in p:
            node = node["children"].setdefault(step, {"count": 0, "ends": 0, "children": {}})
            node["count"] += 1
        node["ends"] += 1  # 会话在此节点终止
    return root


def collect_terminal(node, prefix, out):
    """收集完整路径及其终点支撑数"""
    if node["ends"]:
        out.append((list(prefix), node["ends"]))
    for step, child in node["children"].items():
        prefix.append(step)
        collect_terminal(child, prefix, out)
        prefix.pop()


if __name__ == "__main__":
    compressed = [compress_loop(s) for s in SESSIONS]
    n_loop = sum(1 for a, b in zip(SESSIONS, compressed) if a != b)
    print(f"会话数 {len(SESSIONS)}, 命中回环压缩 {n_loop} 条")
    trie = build_trie(compressed)
    k_paths = []
    collect_terminal(trie, [], k_paths)
    k_paths.sort(key=lambda x: -x[1])
    top5 = k_paths[:5]
    for path, sup in top5:
        print(f"  支撑 {sup:2d}  {' -> '.join(path)}")
    top1 = " -> ".join(top5[0][0])
    assert top1 == "首页 -> 搜索 -> 商品详情 -> 加购 -> 支付", f"top1 应为搜索加购主路径, 实际 {top1}"
    total = sum(s for _, s in k_paths)
    assert total == len(SESSIONS), "全部终点路径支撑之和应等于会话总数"
    print(f"要点: 回环压缩让'逛了又逛'的用户和直购用户归入同一路径, 前缀树天然支持任意前缀的 top-k")
