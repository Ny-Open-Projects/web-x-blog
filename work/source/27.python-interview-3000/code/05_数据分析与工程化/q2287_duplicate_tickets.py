"""重复工单合并: Jaccard 相似聚类, 同一故障只修一次"""

TICKETS = [
    ("T1", "数据大盘 订单指标 为空"),
    ("T2", "订单指标 为空 大盘"),
    ("T3", "导出报表 失败 超时"),
    ("T4", "报表 导出 超时 失败"),
    ("T5", "登录 页面 白屏"),
]


def jaccard(a, b):
    x, y = set(a.split()), set(b.split())
    if not x or not y:
        return 0.0
    return len(x & y) / len(x | y)


def cluster(items, threshold=0.5):
    groups = []   # [代表id, [成员id]]
    text_of = dict(items)
    for tid, text in items:
        for g in groups:
            if jaccard(text_of[g[0]], text) >= threshold:
                g[1].append(tid)
                break
        else:
            groups.append([tid, [tid]])
    return groups


if __name__ == "__main__":
    text_of = dict(TICKETS)
    groups = cluster(TICKETS)
    for rep, members in groups:
        extra = f" <- 合并 {members[1:]}" if len(members) > 1 else ""
        print(f"代表 {rep} 「{text_of[rep]}」{extra}")
    dup = sum(len(m) - 1 for _, m in groups)
    print(f"原始 {len(TICKETS)} 单合并为 {len(groups)} 组, 减少 {dup} 单重复处理")
    print("要点: 先分词再算 Jaccard; 阈值宁松勿紧, 拆开比漏合便宜; 合并关系留痕, 修复后批量关单")
