"""值班交接文档:事件汇总 + 未闭环事项带优先级带状态,新人一眼接得住"""

EVENTS = [
    ("incident", "dws_user 延迟 40 分钟,已扩容恢复", "P2", "closed"),
    ("incident", "埋点上报量下跌 12%,根因 SDK 发版,待观察", "P1", "watching"),
    ("change", "ads_board 口径切换 v3,已公告", "P3", "done"),
    ("alert", "小文件数量超阈值,待合并", "P3", "open"),
]
PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2}


def handover(events, oncall_from="A", oncall_to="B", date_str="2025-10-28"):
    open_items = sorted((e for e in events if e[3] != "done"),
                        key=lambda e: PRIORITY_ORDER[e[2]])
    lines = [f"# 值班交接 {date_str} ({oncall_from} -> {oncall_to})", "", "## 已闭环"]
    lines += [f"- [x] {e[1]}" for e in events if e[3] == "done"]
    lines += ["", "## 未闭环(按优先级)"]
    lines += [f"- [{pri}] ({kind}/{status}) {desc}" for kind, desc, pri, status in open_items]
    lines += ["", "## 关键上下文", "- 观察埋点上报量是否回升,跌破 8% 立即升级"]
    return "\n".join(lines)


if __name__ == "__main__":
    print(handover(EVENTS))
    print("\n要点:交接文档机器生成——事件源是工单/告警/变更系统;未闭环项必须带优先级与下一步动作,不能只写'继续观察'")
