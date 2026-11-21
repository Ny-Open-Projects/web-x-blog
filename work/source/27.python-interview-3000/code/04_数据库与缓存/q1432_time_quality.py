"""时间数据质量: 未来时间、时区错乱与异常跨度检测"""
from datetime import datetime, timezone

now = datetime(2024, 7, 1, tzinfo=timezone.utc)
rows = [
    (1, datetime(2024, 6, 20, tzinfo=timezone.utc)),
    (2, datetime(2030, 1, 1, tzinfo=timezone.utc)),   # 未来时间
    (3, datetime(1990, 1, 1, tzinfo=timezone.utc)),   # 早于业务起点
    (4, datetime(2024, 6, 28, 8, 0)),                 # naive 时间
]
issues = []
for oid, ts in rows:
    ts_u = ts if ts.tzinfo else ts.replace(tzinfo=timezone.utc)
    if ts_u > now:
        issues.append((oid, "未来时间"))
    if ts_u.year < 2000:
        issues.append((oid, "早于业务起点"))
    if not ts.tzinfo:
        issues.append((oid, "缺少时区标注"))
print("时间质量异常:", issues)
print("修时钟与传参比修数据治本: 先查 NTP 与入库代码")
