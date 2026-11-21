"""值班巡检脚本:聚合多类健康信号,输出一份可行动的巡检报告"""

import datetime as dt

NOW = dt.datetime(2025, 6, 16, 9, 0)

CHECKS = [
    # 检查项, 取值函数, 判定函数 -> 状态与建议
    ("夜间任务失败数", lambda: 3,
     lambda v: ("FAIL", "列出失败任务并逐个定级") if v > 0 else ("OK", "")),
    ("管道积压行数", lambda: 150000,
     lambda v: ("WARN", "评估清空时间,必要时扩容") if v > 100000 else ("OK", "")),
    ("数仓磁盘使用率", lambda: 0.91,
     lambda v: ("WARN", "触发归档清理") if v > 0.85 else ("OK", "")),
    ("核心表新鲜度违约数", lambda: 1,
     lambda v: ("FAIL", "按 SLA 电话通知负责人") if v > 0 else ("OK", "")),
    ("告警静默规则数", lambda: 0,
     lambda v: ("WARN", "检查是否有人误加静默") if v > 0 else ("OK", "")),
]


def patrol():
    report = {"FAIL": [], "WARN": [], "OK": []}
    for name, getter, judge in CHECKS:
        value = getter()
        status, advice = judge(value)
        report[status].append((name, value, advice))
    return report


if __name__ == "__main__":
    report = patrol()
    print(f"值班巡检报告 {NOW:%Y-%m-%d %H:%M}")
    for status in ("FAIL", "WARN", "OK"):
        for name, value, advice in report[status]:
            suffix = f" -> {advice}" if advice else ""
            print(f"[{status}] {name} = {value}{suffix}")
    print("\n结论:先处理 FAIL 再看 WARN;报告直接贴进值班群")
