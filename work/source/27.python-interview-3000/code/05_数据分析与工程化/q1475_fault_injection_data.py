"""故障注入测试数据生成:向干净数据注入缺失、重复、格式错与极端值"""

import random

random.seed(20250616)

CLEAN = [
    {"user_id": i, "age": 18 + i % 40, "city": ["北京", "上海", "广州"][i % 3]}
    for i in range(20)
]


def inject(rows, null_rate=0.1, dup_rate=0.05, corrupt_rate=0.1, outlier_rate=0.05):
    rng = random.Random(42)
    out = []
    for row in rows:
        r = dict(row)
        if rng.random() < null_rate:
            r["age"] = None
        if rng.random() < corrupt_rate:
            r["age"] = rng.choice(["二十", "N/A", "18.5.1"])
        if rng.random() < outlier_rate:
            r["age"] = rng.choice([-999, 9999])
        out.append(r)
    n_dup = int(len(out) * dup_rate)
    out += [dict(rng.choice(out)) for _ in range(n_dup)]
    rng.shuffle(out)
    return out


def audit(rows):
    nulls = sum(1 for r in rows if r["age"] is None)
    corrupt = sum(1 for r in rows if isinstance(r["age"], str))
    outliers = sum(1 for r in rows if isinstance(r["age"], int)
                   and not 0 <= r["age"] <= 120)
    ids = [r["user_id"] for r in rows]
    dupes = len(ids) - len(set(ids))
    return {"nulls": nulls, "corrupt": corrupt, "outliers": outliers, "dupes": dupes}


if __name__ == "__main__":
    dirty = inject(CLEAN)
    print("注入后行数:", len(dirty), "干净行数:", len(CLEAN))
    print("质量审计:", audit(dirty))
    again = inject(CLEAN)
    print("同种子可复现:", dirty == again)
    print("要点:测试数据集必须可复现,审计函数同时就是清洗逻辑的验收器")
