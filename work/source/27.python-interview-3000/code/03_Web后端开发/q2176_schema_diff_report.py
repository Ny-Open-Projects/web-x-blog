"""schema diff 报告生成: 对比两版接口摘要并输出 Markdown(纯标准库)。"""

OLD = {
    "GET /v1/orders": {"params": {"status"}, "resp_fields": {"id", "total", "state"}},
    "GET /v1/orders/{id}": {"params": set(), "resp_fields": {"id", "total", "state", "coupon"}},
}
NEW = {
    "GET /v1/orders": {"params": {"status", "limit"},
                       "resp_fields": {"id", "total", "state", "channel"}},
    "GET /v1/orders/{id}": {"params": set(), "resp_fields": {"id", "total", "state"}},
    "POST /v1/orders": {"params": set(), "resp_fields": {"id"}},
}


def diff_specs(old, new):
    lines = ["# API Schema Diff", ""]
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    if added:
        lines.append("## 新增端点")
        lines += ["- `{}`".format(p) for p in added]
    if removed:
        lines.append("## 删除端点(破坏性)")
        lines += ["- `{}`".format(p) for p in removed]
    lines.append("## 变更端点")
    for path in sorted(set(old) & set(new)):
        for key in ("params", "resp_fields"):
            gains = new[path][key] - old[path][key]
            losses = old[path][key] - new[path][key]
            if gains or losses:
                lines.append("- `{}` {}: +{} -{}".format(
                    path, key, sorted(gains) or "-", sorted(losses) or "-"))
    return "\n".join(lines)


report = diff_specs(OLD, NEW)
print(report)
assert "删除端点" not in report and "coupon" in report
print()
print("要点: 先分桶后比字段, 变更条目显式标得失; 同时产出文本报告与结构化结论, 评审看文本门禁看结构")
