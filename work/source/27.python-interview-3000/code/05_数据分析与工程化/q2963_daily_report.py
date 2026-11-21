"""日报自动生成: 事件聚合 -> 指标计算 -> Markdown 渲染 -> 落盘"""
import os
import tempfile
from collections import defaultdict
from datetime import date

# (user, action, revenue) 的当日事件流
EVENTS = [
    ("u1", "visit", 0.0), ("u1", "pay", 199.0),
    ("u2", "visit", 0.0), ("u2", "pay", 58.5),
    ("u3", "visit", 0.0),
    ("u4", "visit", 0.0), ("u4", "pay", 320.0),
    ("u5", "pay", 99.0),
    ("u6", "visit", 0.0),                        # 只看不买
    ("u1", "visit", 0.0), ("u2", "visit", 0.0),  # 同一用户多次访问
]


def aggregate(events):
    """聚合出日报核心指标, 口径全部写明, 不留口头解释空间"""
    m = {"visitors": set(), "payers": set(), "revenue": 0.0, "orders": 0}
    for user, action, revenue in events:
        if action == "visit":
            m["visitors"].add(user)
        elif action == "pay":
            m["payers"].add(user)
            m["revenue"] += revenue
            m["orders"] += 1
    m["uv"] = len(m["visitors"])
    m["pay_users"] = len(m["payers"])
    m["pay_rate"] = round(m["pay_users"] / m["uv"] * 100, 1) if m["uv"] else 0.0
    m["arppu"] = round(m["revenue"] / m["pay_users"], 2) if m["pay_users"] else 0.0
    return m


def render(m, day):
    """纯函数渲染: 同样指标必出同样文案, 便于 diff 与回归"""
    lines = [
        "# 日报 %s" % day,
        "",
        "| 指标 | 值 | 口径 |",
        "|---|---|---|",
        "| 访问用户 UV | %d | 当日去重 visit 用户 |" % m["uv"],
        "| 支付人数 | %d | 当日去重 pay 用户 |" % m["pay_users"],
        "| 支付单数 | %d | pay 事件次数 |" % m["orders"],
        "| 营收 | %.2f | pay 事件金额求和 |" % m["revenue"],
        "| 付费率 | %.1f%% | 支付人数 / UV |" % m["pay_rate"],
        "| 客单价 ARPPU | %.2f | 营收 / 支付人数 |" % m["arppu"],
    ]
    return "\n".join(lines) + "\n"


def main():
    day = date(2026, 3, 1).isoformat()
    m = aggregate(EVENTS)
    md = render(m, day)
    out_dir = tempfile.mkdtemp(prefix="daily_report_")
    path = os.path.join(out_dir, "report_%s.md" % day)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    print("已落盘:", path, "(%d 字节)" % os.path.getsize(path))
    print(md.rstrip())
    return path


if __name__ == "__main__":
    main()
    print("要点: 聚合与渲染分离, 渲染是纯函数; 落盘路径带日期, 表里每行带口径, 收到日报的人不用再问算法")
