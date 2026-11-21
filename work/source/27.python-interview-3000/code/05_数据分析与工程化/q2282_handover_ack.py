"""值班交接的承接确认: 必填校验与跨班次追踪"""

from collections import namedtuple

Item = namedtuple("Item", "title level status next_action shifts")
ITEMS = [
    Item("埋点上报量下跌排查中", "P1", "进行中", "9 点拉日志看上报通道", 1),
    Item("回填任务已完成 80%", "P2", "进行中", "白天继续, 配额剩 20 片", 2),
    Item("新增报表需求已交付", "P3", "已闭环", "", 0),
    Item("慢查询原因待查", "P2", "进行中", "", 1),   # 缺下一步动作
]
REQUIRED = ("level", "status", "next_action")


def ack(item, incoming):
    if item.status == "已闭环":
        return None
    missing = [f for f in REQUIRED if not getattr(item, f)]
    if missing:
        return f"无法承接 [{item.title}]: 缺必填字段 {missing}"
    return f"{incoming} 已承接 [{item.level}] {item.title} -> {item.next_action} (已滚动 {item.shifts} 班)"


if __name__ == "__main__":
    for it in ITEMS:
        result = ack(it, "白班")
        print(result if result else f"[归档备查] {it.title} 已闭环不需承接")
    drift = [it.title for it in ITEMS if it.status != "已闭环" and it.shifts >= 2]
    print(f"跨班次漂移提醒: {drift if drift else '无'}")
    print("要点: 承接是显式动作不是已读; 必填缺失打回; 未闭环项跨班滚动计数, 超两班升级")
