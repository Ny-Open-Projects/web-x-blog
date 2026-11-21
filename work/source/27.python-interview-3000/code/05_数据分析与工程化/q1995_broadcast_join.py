"""小维表广播 join:维表进内存 dict,大表分块流式查表,无 shuffle"""

DIM_USER = {"u1": "VIP", "u2": "普通", "u3": "VIP", "u4": "普通", "u5": "普通"}

FACT_CHUNKS = [
    [("o1", "u1", 200), ("o2", "u3", 150)],
    [("o3", "u2", 88), ("o4", "u9", 66)],   # u9 不在维表
    [("o5", "u1", 320), ("o6", "u5", 99)],
]


def broadcast_join(chunks, dim, default="未知"):
    """大表按块流式过,维表常驻内存 dict,复杂度 O(大表行数),无 shuffle"""
    missed = 0
    for chunk in chunks:
        out = []
        for oid, uid, amt in chunk:
            level = dim.get(uid)
            if level is None:
                missed += 1
                level = default
            out.append((oid, uid, amt, level))
        yield out, missed


def naive_join_cost(chunks, dim):
    """对照:每行全量扫维表,O(大表 x 维表),维表大时不可行"""
    scans = 0
    for chunk in chunks:
        for row in chunk:
            for k in dim:
                scans += 1
                if k == row[1]:
                    break
    return scans


if __name__ == "__main__":
    total_miss = 0
    for chunk, missed in broadcast_join(FACT_CHUNKS, DIM_USER):
        for row in chunk:
            print("  ", row)
        total_miss = missed
    probes = sum(len(c) for c in FACT_CHUNKS)
    scans = naive_join_cost(FACT_CHUNKS, DIM_USER)
    print(f"广播查表 {probes} 次;朴素嵌套循环扫描 {scans} 次(维表 {len(DIM_USER)} 行)")
    print(f"未命中维表的行 {total_miss} 条,已用默认值标记并单独计数")
    print("要点:几十 MB 内的维表广播最优;广播表要设大小上限并定时刷新;未命中给默认值且计数,不让 join 静默丢行")
