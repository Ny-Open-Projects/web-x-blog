
def explain_hint(sql: str, has_index: bool, rows_scanned: int, rows_returned: int) -> str:
    selectivity = rows_returned / max(rows_scanned, 1)
    if not has_index:
        return "全表扫描: 为过滤列建索引或改写查询"
    if selectivity < 0.05:
        return "索引选择性差: 考虑复合索引或覆盖索引"
    if rows_scanned > 100000:
        return "扫描量过大: 分页改 keyset 或强制 LIMIT"
    return "执行计划正常: 查锁等待与连接池"

print(explain_hint("SELECT * FROM orders WHERE user_id=1", False, 500000, 10))
print(explain_hint("SELECT * FROM orders WHERE status='x'", True, 400000, 300000))
