"""故障复盘: 把 MTTR 拆成可行动的四段"""
from datetime import datetime

FMT = "%H:%M:%S"
timeline = [
    ("10:00:00", "故障发生", "上游链路无探测, 暂无感知"),
    ("10:03:00", "告警触发", "错误率越限"),
    ("10:08:00", "值班响应", "开始查错误日志"),
    ("10:21:00", "定位根因", "连接池打满"),
    ("10:26:00", "止血动作", "重启代理 扩容连接上限"),
    ("10:31:00", "服务恢复", "错误率归零"),
]
t = {name: datetime.strptime(ts, FMT) for ts, name, _ in timeline}

def mins(a, b):
    return (t[b] - t[a]).total_seconds() / 60

td, ta = mins("故障发生", "告警触发"), mins("告警触发", "值班响应")
tt, tm = mins("值班响应", "定位根因"), mins("定位根因", "服务恢复")
print("检测 %.0f 分 -> 认领 %.0f 分 -> 定位 %.0f 分 -> 处置 %.0f 分, MTTR 合计 %.0f 分"
      % (td, ta, tt, tm, td + ta + tt + tm))
print("可行动结论: 检测 %.0f 分补上游探测, 定位 %.0f 分沉淀 runbook" % (td, tt))
for ts, name, note in timeline:
    print("  %s  %-6s %s" % (ts, name, note))
