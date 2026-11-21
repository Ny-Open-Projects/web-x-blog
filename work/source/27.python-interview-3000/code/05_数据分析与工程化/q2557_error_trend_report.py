"""错误统计的跨期对比: 环比差值 新增类别与治理成效"""

PREV = {"upstream": 5, "data": 10, "infra": 2}
CURR = {"upstream": 9, "data": 4, "infra": 2, "code": 3}


def trend_report(prev, curr):
    lines, total_delta = [], 0
    cats = sorted(set(prev) | set(curr),
                  key=lambda c: (0 if prev.get(c, 0) == 0 else 1,
                                 -(curr.get(c, 0) - prev.get(c, 0))))
    for cat in cats:
        p, c = prev.get(cat, 0), curr.get(cat, 0)
        delta = c - p
        total_delta += delta
        if p == 0:
            tag, pct = "[新增]", "无法计算环比"
        else:
            pct = f"{delta / p:+.0%}"
            tag = "[恶化]" if delta > 0 else ("[改善]" if delta < 0 else "[持平]")
        lines.append(f"  {cat:<9} {p:3d} -> {c:3d}  差 {delta:+3d}  {pct:<8} {tag}")
    lines.append(f"  合计      {sum(prev.values()):3d} -> {sum(curr.values()):3d}  差 {total_delta:+3d}")
    return lines


if __name__ == "__main__":
    lines = trend_report(PREV, CURR)
    print("错误分类环比报告(上期 -> 本期):")
    print("\n".join(lines))
    assert "code" in lines[0] and "[新增]" in lines[0], "code 类应标记为新增且排最前"
    up_line = next(l for l in lines if l.strip().startswith("upstream"))
    data_line = next(l for l in lines if l.strip().startswith("data"))
    assert "[恶化]" in up_line and "[改善]" in data_line
    print("要点: 环比比绝对量更能驱动行动, 新增类别永远置顶, 改善类别要写进周报给团队正反馈")
