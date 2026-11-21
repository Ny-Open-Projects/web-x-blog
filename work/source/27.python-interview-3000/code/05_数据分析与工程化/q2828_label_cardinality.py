"""标签基数审计: 用 distinct/total 比值找出混进标签的唯一值字段"""

RECORDS = [
    {"service": "pay", "env": "production", "region": "cn-north-1", "level": "error", "user_id": f"u{i:03d}"}
    for i in range(10)
]
RECORDS[3]["region"] = "cn-east-1"
RECORDS[7]["region"] = "cn-south-1"
RECORDS[5]["level"] = "warn"
RECORDS[8]["level"] = "info"

UNIQUE_RATIO = 0.8   # distinct/total 超过它即视为唯一值字段


def cardinality_audit(records):
    total = len(records)
    keys = set()
    for r in records:
        keys.update(r)
    report = []
    for key in sorted(keys):
        distinct = len({r[key] for r in records if key in r})
        ratio = distinct / total
        verdict = "疑似唯一值字段, 应移出标签" if ratio >= UNIQUE_RATIO else "OK"
        report.append((key, distinct, ratio, verdict))
    return report


if __name__ == "__main__":
    print(f"{'标签':<10}{'distinct':>9}{'total':>7}{'比值':>7}  判定")
    flagged = []
    for key, distinct, ratio, verdict in cardinality_audit(RECORDS):
        print(f"{key:<10}{distinct:>9}{len(RECORDS):>7}{ratio:>7.1%}  {verdict}")
        if verdict != "OK":
            flagged.append(key)
    assert flagged == ["user_id"], "只有 user_id 应被判为唯一值字段"
    assert len({r['region'] for r in RECORDS}) == 3, "region 应是低基数标签"
    print("建议: 把 user_id 改写进 message 或单独建索引, 标签里只留聚合维度")
    print("要点: 高基数标签会让日志系统按值建倒排, 存储与查询双爆炸; 审计脚本每周扫采样即可发现")
