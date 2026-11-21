"""解析一段慢日志样例, 按总耗时聚合出最该优化的语句模式"""
import re
from collections import defaultdict

SAMPLE = """
# Time: 2024-05-01T10:00:00
# Query_time: 2.1 Lock_time: 0.01 Rows_sent: 20 Rows_examined: 200000
SELECT * FROM orders WHERE user_id = 7 ORDER BY created_at;
# Time: 2024-05-01T10:05:00
# Query_time: 0.3 Lock_time: 0.02 Rows_sent: 5 Rows_examined: 60000
SELECT * FROM orders WHERE user_id = 9 ORDER BY created_at;
# Time: 2024-05-01T10:09:00
# Query_time: 1.5 Lock_time: 0.00 Rows_sent: 100 Rows_examined: 100
SELECT * FROM big_report WHERE day = '2024-04-30';
"""

PAT = re.compile(
    r"Query_time: ([\d.]+).*?Rows_sent: (\d+) Rows_examined: (\d+)\s+(.*?;)", re.S)

if __name__ == "__main__":
    stats = defaultdict(lambda: [0.0, 0, 0])
    for qt, sent, examined, sql in PAT.findall(SAMPLE):
        pattern = re.sub(r"= \S+", "= ?", sql.strip())[:60]
        stats[pattern][0] += float(qt)
        stats[pattern][1] += int(examined)
        stats[pattern][2] += 1
    for sql, (total, rows, n) in sorted(stats.items(), key=lambda x: -x[1][0]):
        print(f"总耗时 {total:>5.1f}s  次数 {n}  累计扫描 {rows} 行\n  {sql}")
