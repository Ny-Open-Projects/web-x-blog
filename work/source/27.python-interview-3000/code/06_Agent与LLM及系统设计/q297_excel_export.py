import csv
import io


def export_stream(rows_iter, columns: list) -> io.StringIO:
    """逐行写入 StringIO,不持有全量数据;生产中可换 xlsx write_only。
    这里用 csv 演示流式思路,rows_iter 支持数据库游标分批产出。"""
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(columns)
    for row in rows_iter:      # 迭代器,内存 O(1)
        writer.writerow(row)
    return out


def fake_db_cursor(total: int, batch: int):
    """模拟分批取数:fetchmany 模式。"""
    start = 0
    while start < total:
        yield from [(i, f"name{i}") for i in range(start, min(start + batch, total))]
        start += batch


if __name__ == "__main__":
    buf = export_stream(fake_db_cursor(1000, 100), ["id", "name"])
    print(buf.getvalue()[:60], "...")
