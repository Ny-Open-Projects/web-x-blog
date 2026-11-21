"""迟到数据修正:窗口级重算 + 版本号合并,封存窗口走离线补数"""

BASE = {"10:00-10:59": 300, "11:00-11:59": 420}   # 常规流已发布窗口结果
LATE = [
    ("10:00-10:59", 70),   # 迟到明细
    ("09:00-09:59", 50),   # 窗口已封存
    ("10:00-10:59", 70),   # 重复迟到,幂等去重
]

PUBLISHED = {}


def publish(window, value, version, source):
    """只有更高版本才覆盖:修正流版本高于常规流,重复到达不回退"""
    cur = PUBLISHED.get(window)
    if cur is None or version > cur["version"]:
        PUBLISHED[window] = {"value": value, "version": version, "source": source}
        return True
    return False


def apply_late(base, late):
    out = dict(base)
    seen, skipped = set(), []
    for w, amt in late:
        if w not in out:
            skipped.append((w, amt))
            continue
        if (w, amt) in seen:
            continue
        seen.add((w, amt))
        out[w] += amt
    return out, skipped


if __name__ == "__main__":
    fixed, skipped = apply_late(BASE, LATE)
    print("修正前:", BASE)
    print("修正后:", fixed)
    print("封存窗口(走离线补数,不静默丢):", skipped)
    publish("10:00-10:59", 300, 1, "batch")
    print("修正流发布生效:", publish("10:00-10:59", 370, 2, "late-fix"))
    print("同版本重复发布被拒:", publish("10:00-10:59", 370, 2, "late-fix"))
    print("要点:迟到处理=窗口级重算 + 版本号合并 + 幂等指纹去重;窗口封存后到的数据走补数流程并留下审计记录")
