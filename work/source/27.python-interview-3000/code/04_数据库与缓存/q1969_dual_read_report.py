"""双写期读对比: 抽样双读与差异归因报告"""
import random

random.seed(11)

old_db = {}
new_db = {}
for i in range(1, 1001):
    old_db["u%d" % i] = {"name": "user%d" % i, "age": 20 + i % 30, "vip": i % 5 == 0}
    new_db["u%d" % i] = {"name": "user%d" % i, "age": 20 + i % 30, "vip": i % 5 == 0}

# 制造三类真实不一致: 丢写 旧值残留 口径差异
del new_db["u333"]
new_db["u500"]["age"] = 99
new_db["u700"]["vip"] = not new_db["u700"]["vip"]

def sample_report(old, new, rate=0.05, fields=("name", "age", "vip"), extra=()):
    """随机抽样加上强制覆盖的已知问题键 修复后重跑可复检"""
    keys = random.sample(sorted(old.keys()), int(len(old) * rate))
    keys = sorted(set(keys) | set(extra))
    report = {"checked": len(keys), "missing_in_new": [], "value_diff": {}}
    for k in keys:
        o, n = old.get(k), new.get(k)
        if n is None:
            report["missing_in_new"].append(k)
            continue
        for f in fields:
            if o[f] != n[f]:
                report["value_diff"].setdefault(f, []).append(k)
    return report

rep = sample_report(old_db, new_db, extra=["u333", "u500", "u700"])
print("抽样双读报告 -> 检查", rep["checked"], "条  新库缺失", len(rep["missing_in_new"]),
      "条  字段差异:", {f: len(ks) for f, ks in rep["value_diff"].items()})
print("缺失明细:", rep["missing_in_new"])

def attribute(k, o, n):
    """把差异归因到根因与动作 修复要能按归因分类重跑"""
    if n is None:
        return "双写链路丢写 查写入端错误日志并补写"
    if o["vip"] != n["vip"]:
        return "布尔或枚举映射口径不一致 查转换层"
    return "疑似回放顺序或并发覆盖 以源库为准订正"

for k in rep["missing_in_new"][:3]:
    print(f"{k}: {attribute(k, old_db.get(k), new_db.get(k))}")
for f, ks in rep["value_diff"].items():
    k = ks[0]
    print(f"{k} 字段 {f}: {attribute(k, old_db[k], new_db[k])}")
print("结论: 对比报告三要素 抽样比例 差异分类 归因到动作 修复后重跑验证收敛率")
