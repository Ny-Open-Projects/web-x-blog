---
title: [Q2788] 路径分析的 top-k 序列:前缀树计数与回环压缩
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2788 · 路径分析的 top-k 序列:前缀树计数与回环压缩

> 难度:★★★☆ | 标签:路径分析, 前缀树

**问**:面试官:让你算用户路径的 top-k 高频序列,你的实现骨架是什么?

**答**:两步:回环压缩加前缀树。压缩把同一会话内重复出现的页面只保留首次,12 条会话里 2 条命中压缩,"逛了又逛"的用户与直通用户归入同一路径形状,否则重复浏览会无限拉长路径、稀释支撑数;然后把压缩路径逐条插入前缀树,叶子节点记"终点支撑数"。全路径支撑 top5:首页-搜索-商品详情-加购-支付 与 首页-分类-商品详情-加购-支付 各 3 条,搜索直购 2 条,其余 1 条。前缀树的优势是任意前缀的 top-k 都是树上一次 DFS,还能顺着树往下滑看"这一步之后用户去哪",天然支持"截断到第 n 步"的口径。

```python
# file: code/05_数据分析与工程化/q2788_path_topk_trie.py
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
```

**追问**:
- 追问 1:回环压缩会丢什么信息?—— 丢失重复浏览强度,频次与疲劳类分析必须回到原始序列,压缩只服务路径归类。
- 追问 2:k 取多大才合理?—— 看下一题的覆盖度曲线,用累计覆盖目标反解 k,而不是拍脑袋定 10 条。
