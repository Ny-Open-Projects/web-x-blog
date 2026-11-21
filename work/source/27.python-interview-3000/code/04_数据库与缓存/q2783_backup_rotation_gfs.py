"""备份保留的三代轮换: 日 7 周 4 月 3, 恢复点与存储成本兼得"""
from datetime import date, timedelta

TODAY = date(2026, 11, 5)
backups = [TODAY - timedelta(days=i) for i in range(0, 121)]   # 每日一份共 121 份

def latest_on_or_before(target, pool):
    cands = [b for b in pool if b <= target]
    return max(cands) if cands else None

keep = set()
for i in range(7):                                   # 日备: 最近 7 天
    b = latest_on_or_before(TODAY - timedelta(days=i), backups)
    if b:
        keep.add(b)
d, sundays = TODAY, []                               # 周备: 最近 4 个周日
while len(sundays) < 4:
    if d.weekday() == 6:
        sundays.append(d)
    d -= timedelta(days=1)
for s in sundays:
    b = latest_on_or_before(s, backups)
    if b:
        keep.add(b)
firsts, d = [], TODAY.replace(day=1)                 # 月备: 最近 3 个月每月 1 号
for _ in range(3):
    firsts.append(d)
    d = (d - timedelta(days=1)).replace(day=1)
for f in firsts:
    b = latest_on_or_before(f, backups)
    if b:
        keep.add(b)

print("备份池 %d 份, 三代轮换后保留 %d 份, 删除 %d 份" % (len(backups), len(keep), len(backups) - len(keep)))
print("保留样例: 最近", sorted(keep, reverse=True)[:3], "最早", min(keep))
print("恢复点覆盖: 7 天内每日, 1 个月内每周, 3 个月内每月")
