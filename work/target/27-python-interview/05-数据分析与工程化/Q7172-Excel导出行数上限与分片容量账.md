---
title: [Q7172] Excel导出行数上限与分片容量账
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7172 · Excel 导出的行数上限与分片容量账

难度：P6 ｜ 标签：容量规划、Excel、导出
基线：openpyxl 3.x（xlsx 格式硬上限：单 sheet 1,048,576 行 × 16,384 列）。

**问**：运营要导出全量订单（800 万行）成 Excel，任务 OOM 或生成失败。xlsx 的硬上限怎么算？分片导出的容量账（内存、时间、文件数）怎么设计？

**答**：**结论**：xlsx 有两条硬约束：**单 sheet 1,048,576 行**（800 万行至少 8 个 sheet/文件）和**写入内存模型**——openpyxl 默认把整个 workbook 缓存在内存再写盘，百万行轻松吃掉数 GB。分片导出的账要算三笔：① 文件数 = ceil(行数 / 每片行数)，每片行数上限受 1,048,576 与内存双重约束，经验值 20-50 万行/片；② 写入耗时 ≈ 行数 × 每行写耗时（带样式每行贵 3-10 倍）；③ 打包与传输体积（xlsx 本质是 zip 的 XML，数值多时体积友好，字符串重复多时要靠 shared strings 压缩）。

**取舍**：三个层级的方案：① openpyxl `write_only=True`（流式写，内存 O(1)，慢但稳）；② 换 CSV/Parquet 给机器消费，Excel 只给人看摘要——多数"导出 Excel"的需求其实是"导出数据"，改格式是最便宜的解；③ 真要大表 Excel 就按"每 sheet 接近上限 + 多文件 + zip 打包"，并用流式写。默认样式（每 cell 设 font）是导出慢的头号杀手，样式只按列头设。

**实战**：导出任务做成异步 Job（返回下载链接），分片大小按"内存实测 × 安全系数"定；超过行数阈值的请求直接拒绝并推荐 CSV，避免用户拿 Excel 当数据库。

```python
import math

XLSX_MAX_ROWS = 1_048_576      # 硬上限（含表头占用 1 行）

def export_plan(n_rows: int, chunk_rows: int = 200_000,
                write_only: bool = True) -> dict:
    """分片导出方案与容量账。"""
    usable = XLSX_MAX_ROWS - 1              # 表头占一行
    if chunk_rows > usable:
        chunk_rows = usable
    files = math.ceil(n_rows / chunk_rows)
    # 内存账：普通模式 ≈ 行数 × 每行 2KB（含 cell 对象开销），write_only ≈ O(1)
    mem_mb = 0.002 * chunk_rows if write_only else 0.002 * n_rows
    # 时间账：write_only 每行约 5us，带样式每行约 30us
    sec = n_rows * (5e-6 if write_only else 3e-5)
    return {
        "files": files,
        "chunk_rows": chunk_rows,
        "peak_mem_mb": round(mem_mb, 1),
        "write_seconds": round(sec, 1),
        "verdict": ("OK：异步任务 + 分片"
                    if files <= 200 else
                    "规模过大：改 CSV/Parquet，Excel 不适合此量级"),
    }

print(export_plan(8_000_000))
# 8M 行 -> 40 个文件，write_only 峰值内存仅 ~400MB

# 流式写演示：write_only 模式逐行追加，不攒内存（openpyxl 3.x）
from openpyxl import Workbook
import tempfile, os

wb = Workbook(write_only=True)
ws = wb.create_sheet("orders")
ws.append(["id", "amount"])
for i in range(10_000):                     # 10 万行也不会爆内存
    ws.append([i, 100 + i % 7])
path = os.path.join(tempfile.gettempdir(), "slice.xlsx")
wb.save(path)
size_kb = os.path.getsize(path) // 1024
print(f"write_only 写 10k 行成功，文件 {size_kb}KB")

# 对照硬上限：单行超过 2^14=16384 列会抛异常（列维度同样有硬上限）
try:
    ws3 = wb.create_sheet("bad")
    ws3.append([1] * (16384 + 1))           # 构造超列限
except Exception as e:                       # openpyxl 抛出维度类异常
    print("超限保护:", type(e).__name__)
os.remove(path)
```

**追问 1**：为什么 xlsx 的行上限是 1,048,576 而不是整数？
提示：2^20 行 × 2^14 列的设计，是 OOXML 规范里 row/column 引用编码的位宽上限；不是性能问题，是格式规范，任何实现（openpyxl/Excel/WPS）都一样。

**追问 2**：为什么"每 cell 设样式"会让导出慢 3-10 倍？
提示：xlsx 里样式是对象引用，openpyxl 对每个 cell 做 Python 对象构建 + 样式查重；百万 cell 的样式查重本身就是 O(n) 的字典操作加对象分配——样式按列头/条件格式收敛即可。

**追问 3**：如果运营坚持要"一个 Excel 里全量"，怎么办？
提示：技术不成立（硬上限）+体验不成立（百万行 Excel 无法翻阅），正确响应是回到需求本质：他们要的通常是筛选、透视或对账，给出预聚合 sheet + 明细分文件 + 筛选说明的组合方案，而不是硬扛格式。

## 背诵要点
1. xlsx 硬上限 2^20 = 1,048,576 行/Sheet；openpyxl 默认全量缓存内存，write_only 才是流式 O(1)。
2. 分片账：文件数 = ceil(行数/每片行)，每片 20-50 万行；样式按 cell 设是耗时头号杀手。
3. 需求本质判断：要"导出数据"给 CSV/Parquet，Excel 只给人看摘要；超量级直接拒绝并给替代方案。

## 复盘追问
1. 你们平台上最大的 Excel 导出是多少行？当时用了 write_only 还是普通模式，内存峰值实测多少？
2. 如果运营明天要"带透视表和条件格式"的大导出，你的方案边界（哪部分 openpyxl 做不了）清楚吗？
