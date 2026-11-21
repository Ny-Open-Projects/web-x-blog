"""值班交接摘要生成:事件流到结构化交接文档"""

EVENTS = [
    # 时刻, 级别, 事件, 是否已解决
    ("02:10", "P1", "ads_funnel 任务失败,水位线告警", True),
    ("02:40", "P1", "ads_funnel 重跑成功,数据恢复", True),
    ("05:00", "P2", "kafka consumer lag 升至 40 万", True),
    ("07:30", "P3", "BI 群反馈看板刷新慢,已回复排期", False),
    ("08:50", "P2", "某上游表 schema 新增列,待评估影响", False),
]

TEMPLATE = """值班交接摘要 {date}
一、未解决事项 优先处理
{open_items}
二、已处理事项 备查
{closed_items}
三、风险与建议
{risks}"""


def handover(events, date="2025-06-16"):
    order = {"P1": 0, "P2": 1, "P3": 2}
    open_items = sorted([e for e in events if not e[3]], key=lambda e: order[e[1]])
    closed_items = sorted([e for e in events if e[3]], key=lambda e: order[e[1]])
    risks = []
    if any("schema" in e[2] for e in open_items):
        risks.append("- 上游 schema 变更: 今日内跑一次影响面分析")
    if any("lag" in e[2] for e in events):
        risks.append("- 消费积压反复: 关注消费者容量与重平衡")
    return TEMPLATE.format(
        date=date,
        open_items="\n".join(f"- [{e[1]}] {e[0]} {e[2]}" for e in open_items) or "- 无",
        closed_items="\n".join(f"- [{e[1]}] {e[0]} {e[2]}(已解决)" for e in closed_items),
        risks="\n".join(risks) or "- 无")


if __name__ == "__main__":
    print(handover(EVENTS))
