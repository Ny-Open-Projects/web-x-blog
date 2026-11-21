"""CSV 导出端点的流式生成: 生成器分块产出 + 恒定内存(纯标准库)。"""
import csv
import io


def csv_stream(header, rows, batch=128, bom=True):
    """把行迭代器切成固定大小的字节块, 逐块 yield; 内存峰值只与 batch 相关。

    首块用 utf-8-sig 加 BOM, Excel 打开才不乱码; 后续块纯 utf-8。
    """
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\r\n")
    writer.writerow(header)
    yield buf.getvalue().encode("utf-8-sig" if bom else "utf-8")
    buf.seek(0)
    buf.truncate(0)
    count = 0
    for row in rows:
        writer.writerow(row)
        count += 1
        if count % batch == 0:
            yield buf.getvalue().encode("utf-8")
            buf.seek(0)
            buf.truncate(0)
    if buf.tell():
        yield buf.getvalue().encode("utf-8")


def rows_from_db(total):
    """模拟数据库游标: 一次只取一行, 不整表进内存。"""
    for i in range(1, total + 1):
        if i == 7:
            yield (i, '含"引号"与,逗号的名字', "12.50")
        else:
            yield (i, "订单-%d" % i, "%.2f" % (i * 1.5))


HEADER = ["id", "name", "amount"]
TOTAL = 1000

chunks = list(csv_stream(HEADER, rows_from_db(TOTAL), batch=128))
sizes = [len(c) for c in chunks]
print("产出 %s 个字节块, 单块最大 %s 字节, 总计 %s 字节" % (len(chunks), max(sizes), sum(sizes)))
assert max(sizes) < 64 * 1024, "每块体积有上界, 与总行数无关"

payload = b"".join(chunks)
assert payload[:3] == b"\xef\xbb\xbf", "首块带 BOM"
assert payload.endswith(b"\r\n")

parsed = list(csv.reader(io.StringIO(payload.decode("utf-8-sig"))))
print("回读解析: 表头=%s, 数据行=%s" % (parsed[0], len(parsed) - 1))
assert parsed[0] == HEADER and len(parsed) - 1 == TOTAL
assert parsed[7] == ["7", '含"引号"与,逗号的名字', "12.50"], "csv 引号转义可逆"

# 空结果也要有表头, 客户端才能渲染空表格
empty = b"".join(csv_stream(HEADER, iter([]), batch=128))
assert empty.decode("utf-8-sig").strip() == ",".join(HEADER)

# 惰性验证: 只取前两块时, 上游行迭代器没有被消费完
# 第一块只含表头不消费行, 第二块才消费第一批 batch 行
lazy_rows = rows_from_db(TOTAL)
stream = csv_stream(HEADER, lazy_rows, batch=128)
next(stream)
next(stream)
del stream
consumed = len(list(lazy_rows))
print("只拉两块后游标剩余 %s 行未消费, 证明是惰性拉取" % consumed)
assert consumed == TOTAL - 128

# WSGI 出口: 直接把生成器交给响应体迭代器, 边生成边发送
wsgi_body = iter(csv_stream(HEADER, rows_from_db(5), batch=2))
headers = [
    ("Content-Type", "text/csv; charset=utf-8"),
    ("Content-Disposition", "attachment; filename=orders.csv"),
]
print("响应头:", dict(headers)["Content-Disposition"])
print("CSV 流式导出演示通过")
