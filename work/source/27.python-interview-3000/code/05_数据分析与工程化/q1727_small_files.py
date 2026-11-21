"""小文件合并策略:按目标大小装箱,单文件无可合并跳过,凑满一组才合并"""

try:
    import pandas as pd
except ImportError:
    pd = None

FILES = [
    ("part=2025-10-01/f1", 8), ("part=2025-10-01/f2", 12), ("part=2025-10-01/f3", 5),
    ("part=2025-10-01/f4", 30), ("part=2025-10-02/f1", 3), ("part=2025-10-02/f2", 2),
    ("part=2025-10-02/f3", 4), ("part=2025-10-03/f1", 120),
]
TARGET_MB = 32


def plan_merge(files, target):
    """同分区贪心装箱:能凑一组合并一组,单文件分区跳过"""
    by_part = {}
    for name, mb in files:
        by_part.setdefault(name.split("/")[0], []).append((name, mb))
    plan = []
    for part, fs in sorted(by_part.items()):
        if len(fs) == 1:
            plan.append((part, "skip", [fs[0][0]]))
            continue
        bucket, bucket_size, groups = [], 0, []
        for name, mb in fs:
            if bucket and bucket_size + mb > target:
                groups.append(bucket)
                bucket, bucket_size = [], 0
            bucket.append(name)
            bucket_size += mb
        if bucket:
            groups.append(bucket)
        for g in groups:
            plan.append((part, "merge", g))
    return plan


if pd is None:
    print("标准库降级:合并计划(装箱目标 32MB)")
    size_of = dict(FILES)
    for part, action, g in plan_merge(FILES, TARGET_MB):
        total = sum(size_of[n] for n in g)
        print(f"  {action:<6} {part} 合计 {total:>3}MB <- {g}")
else:
    df = pd.DataFrame(FILES, columns=["file", "size_mb"])
    df["part"] = df["file"].str.split("/").str[0]
    summary = df.groupby("part")["size_mb"].agg(files="count", total="sum")
    print(summary)
    for part, action, g in plan_merge(FILES, TARGET_MB):
        print(f"  {action:<6} {part} <- {g}")
