---
title: [Q297] Excel 导出在大数据量下的内存问题
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q297 · Excel 导出在大数据量下的内存问题
> 难度:★★★ | 标签:数据处理, 性能

**问**:导出 100 万行 Excel 报 OOM,怎么解决?

**答**:三种手段:一是流式生成,用 openpyxl 的 `write_only` 模式逐行写不回读,并从数据库 `fetchmany` 分批取数;二是控制格式,`xlsxwriter` 的 constant_memory 模式;三是超过一定行数降级为 CSV(Excel 单 sheet 上限约 104 万行)。生成后放对象存储返回下载链接,避免 HTTP 响应超时。

```python
# file: code/06_Agent与LLM及系统设计/q297_excel_export.py
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
```

**追问**:
- write_only 模式限制?——只支持追加不可回读改样式;样式按列预配置;需要复杂样式考虑拆 sheet 或换 xlsxwriter。
- 导出超时怎么防?——异步任务生成后对象存储链接;同步 HTTP 大导出会被网关超时与内存拖垮。
- 为什么 104 万行要降级 CSV?——xlsx 单 sheet 行数硬上限;超限写入直接报错,提前检查并切分多 sheet 或转 CSV。

---
