"""双写对账:分片比对、差异修复与收敛验证(纯标准库)。"""


def shard_of(key, shards=4):
    return sum(key.encode()) % shards


def reconcile(source, target, repair=False):
    report = {"missing": [], "mismatched": [], "extra": [], "repaired": []}
    for key in sorted(set(source) | set(target)):
        in_s, in_t = source.get(key), target.get(key)
        if in_s is None:
            report["extra"].append(key)          # 目标独有,需人工确认
            continue
        if in_t is None:
            report["missing"].append(key)
            if repair:
                target[key] = in_s
                report["repaired"].append((key, "created"))
        elif in_t != in_s:
            report["mismatched"].append((key, in_s, in_t))
            if repair:
                target[key] = in_s
                report["repaired"].append((key, "updated"))
    return report


source = {"o1": 100, "o2": 200, "o3": 300, "o4": 400}
target = {"o1": 100, "o2": 201, "o4": 400, "o5": 999}

first = reconcile(source, target)
print("首轮:", {k: v for k, v in first.items() if v})
reconcile(source, target, repair=True)
second = reconcile(source, target)
print("修复后再对账 missing:", second["missing"], "mismatched:", second["mismatched"])
print("extra 待人工确认:", second["extra"])
print("分片演示:", {s: [k for k in sorted(source) if shard_of(k) == s] for s in range(4)})
