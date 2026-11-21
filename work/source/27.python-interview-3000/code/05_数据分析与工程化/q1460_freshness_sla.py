"""数据新鲜度 SLA:每表时限、延迟分级与联系人路由"""

import datetime as dt

TABLES = [
    # 表, 承诺时刻, 实际就绪时刻, SLA 分钟, 负责人
    ("ads_realtime", dt.time(0, 15), dt.time(0, 12), 15, "实时组"),
    ("dwd_trade", dt.time(3, 0), dt.time(3, 20), 15, "数仓组"),
    ("ads_report", dt.time(8, 0), dt.time(7, 30), 30, "报表组"),
]


def lag_minutes(planned, actual, day=dt.date(2025, 6, 16)):
    delta = dt.datetime.combine(day, actual) - dt.datetime.combine(day, planned)
    return delta.total_seconds() / 60


def grade(lag, sla):
    if lag <= 0:
        return "OK"
    if lag <= sla:
        return "WARN 已延迟但在 SLA 内"
    return "BREACH 违约"


if __name__ == "__main__":
    for name, planned, actual, sla, owner in TABLES:
        lag = lag_minutes(planned, actual)
        g = grade(lag, sla)
        notify = "电话值班" if g.startswith("BREACH") else \
                 ("群里 @负责人" if g.startswith("WARN") else "无需通知")
        print(f"{name}: 延迟 {lag:+.0f} 分钟 SLA {sla} -> {g} 通知: {notify}")
    print("新鲜度 SLA 要写进服务目录,违约率按周统计进团队健康报告")
