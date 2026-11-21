"""解析 MySQL 慢日志文本, 聚合 TOP 慢 SQL(参数归一化)"""
import re
from collections import defaultdict

SAMPLE = """
# Time: 2024-05-01T10:00:00
# Query_time: 3.2 Lock_time: 0.001 Rows_sent: 10 Rows_examined: 900000
SELECT * FROM orders WHERE user_name = 'alice' ORDER BY created_at;
# Time: 2024-05-01T10:01:00
# Query_time: 2.8 Lock_time: 0.001 Rows_sent: 10 Rows_examined: 880000
SELECT * FROM orders WHERE user_name = 'bob' ORDER BY created_at;
"""

QUERY_TIME_RE = re.compile(r"Query_time:\s*([\d.]+)")
SQL_RE = re.compile(r"^(SELECT|UPDATE|DELETE|INSERT).*", re.I | re.S)


def normalize(sql: str) -> str:
    """把字面量换成 ? 聚合同模板"""
    return re.sub(r"'[^']*'", "?", sql.strip().rstrip(";"))


def top_slow(log_text: str, top_n: int = 3) -> list:
    stat = defaultdict(lambda: [0, 0.0])   # 模板 -> [次数, 总耗时]
    for block in log_text.split("# Time: ")[1:]:
        m = QUERY_TIME_RE.search(block)
        s = SQL_RE.search(block)
        if m and s:
            tpl = normalize(s.group(0))
            stat[tpl][0] += 1
            stat[tpl][1] += float(m.group(1))
    return sorted(stat.items(), key=lambda kv: kv[1][1], reverse=True)[:top_n]


if __name__ == "__main__":
    for tpl, (cnt, total) in top_slow(SAMPLE):
        print(f"共 {cnt} 次 累计 {total:.1f}s  模板: {tpl}")
