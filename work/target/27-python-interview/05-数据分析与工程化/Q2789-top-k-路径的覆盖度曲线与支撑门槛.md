---
title: [Q2789] top-k 路径的覆盖度曲线与支撑门槛
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2789 · top-k 路径的覆盖度曲线与支撑门槛

> 难度:★★☆☆ | 标签:路径分析, 覆盖度

**问**:面试官:路径报表展示 top-10 还是 top-50?你的依据是什么?

**答**:依据是覆盖度曲线,不是拍脑袋。把完整路径按支撑数降序排列算累计覆盖:top-3 覆盖 66.7%,top-5 覆盖 83.3%,其余 2 条长尾合计只占 16.7%;覆盖 80% 的最小 k 是 5,且门槛后的每条路径支撑占比都不到 10%。这条曲线就是支撑门槛的谈判工具:报表展示 top-5,其余全部进"其他"桶,不逐条展开;业务坚持要看更多时,加一行"长尾合计"即可。注意覆盖度对会话数而言——路径数有 7 条,长尾路径条数多但每条贡献小,报表的篇幅应该跟着流量走而不是跟着路径种类走。

```python
# file: code/05_数据分析与工程化/q2789_path_coverage_curve.py
"""top-k 路径覆盖度曲线: k 取多大才够, 支撑门槛定在哪"""

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
    seen, out = set(), []
    for p in path:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def full_path_supports(sessions):
    counts = {}
    for s in sessions:
        key = tuple(compress_loop(s))
        counts[key] = counts.get(key, 0) + 1
    return sorted(counts.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    paths = full_path_supports(SESSIONS)
    total = sum(s for _, s in paths)
    print(f"压缩后 distinct 完整路径 {len(paths)} 条, 覆盖会话 {total} 条")
    covered, cums = 0, []
    for k, (path, sup) in enumerate(paths, 1):
        covered += sup
        ratio = covered / total
        cums.append(ratio)
        print(f"k={k}  支撑 {sup}  累计覆盖 {ratio:.1%}  {' -> '.join(path[:4])}")
    k80 = next(i + 1 for i, r in enumerate(cums) if r >= 0.8)
    leftover = 1 - cums[k80 - 1]
    print(f"覆盖 80% 只需 top-{k80} 条路径, 其余 {len(paths) - k80} 条合计仅占 {leftover:.1%}")
    assert k80 <= 5, "本例 80% 覆盖不应超过 5 条路径"
    assert leftover < 0.2 and all(s / total < 0.1 for _, s in paths[k80:]), "门槛后的路径都应是长尾"
    print("要点: 覆盖度曲线的拐点就是支撑门槛, 低于门槛的路径进长尾桶聚合展示, 报表不逐条追")
```

**追问**:
- 追问 1:覆盖目标和支撑门槛谁先定?—— 先定覆盖目标(如 80%),曲线反解出 k,再换算成最小支撑数,门槛是推导结果不是输入。
- 追问 2:长尾什么时候值得关注?—— 当某条长尾路径支撑持续上升突破门槛时,它就是新兴路径,监控其排名变化即可自动发现。
