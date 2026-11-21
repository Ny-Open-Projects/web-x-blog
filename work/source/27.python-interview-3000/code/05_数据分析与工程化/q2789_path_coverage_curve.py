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
