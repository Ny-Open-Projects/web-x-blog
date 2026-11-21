"""埋点覆盖率对账:埋点方案清单对实收事件,输出缺失事件与缺字段"""

PLAN = {
    "order_submit": {"required": ["order_id", "amount", "channel"]},
    "pay_success": {"required": ["order_id", "pay_type"]},
    "search_click": {"required": ["query", "pos"]},
}
RECEIVED = {
    "order_submit": {"order_id": 500, "amount": 498, "channel": 120},
    "pay_success": {"order_id": 470},
    "page_view": {"url": 9000},
}
SAMPLE_TOTAL = 500
COV_LINE = 0.9   # 字段到达率 90% 算达标


def audit(plan, received):
    report = []
    for event, spec in plan.items():
        if event not in received:
            report.append((event, "事件缺失", 0.0, []))
            continue
        fields = received[event]
        missing = [f for f in spec["required"]
                   if fields.get(f, 0) < SAMPLE_TOTAL * COV_LINE]
        hit = sum(1 for f in spec["required"]
                  if fields.get(f, 0) >= SAMPLE_TOTAL * COV_LINE)
        cov = hit / len(spec["required"])
        report.append((event, "字段不全" if missing else "正常", cov, missing))
    extra = sorted(e for e in received if e not in plan)
    return report, extra


if __name__ == "__main__":
    report, extra = audit(PLAN, RECEIVED)
    for event, status, cov, missing in report:
        line = f"{event:<14} {status:<6} 字段覆盖 {cov:.0%}"
        if missing:
            line += f"  缺: {missing}"
        print(line)
    print(f"未登记事件(埋点野数据): {extra}")
    print("要点:以埋点方案为基准逐事件对账,字段级到达率 90% 算达标;野事件要么补登记要么清退,长期挂着会污染事件字典")
