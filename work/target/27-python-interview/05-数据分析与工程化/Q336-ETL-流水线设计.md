---
title: [Q336] ETL 流水线设计
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q336 · ETL 流水线设计

> 难度:★★★ | 标签:ETL, 架构

**问**:设计一条 ETL 流水线时,你会考虑哪些工程要素?

**答**:分层设计:Extract 负责幂等拉数(记录水位)、Transform 做纯函数式转换(输入输出明确、可单测)、Load 原子写入(先写临时文件再 rename 或事务提交)。横切要素:失败重试与断点续跑、每步的行数与校验和日志、元数据(批次号、数据日期、代码版本)落盘、告警与死信处理。核心纪律:Transform 层不碰网络和数据库连接,保持可复现;所有步骤以"数据日期 + 批次"为键,天然支持重跑不产生重复。

```python
# file: code/05_数据分析与工程化/q336_etl_pipeline.py
import json
import os

def extract(src_path, processed_marker):
    """Extract:带水位标记,幂等拉取。"""
    if os.path.exists(processed_marker):
        print("already processed, skip")
        return []
    with open(src_path) as f:
        return [line.strip() for line in f if line.strip()]

def transform(records):
    """Transform:纯函数,输入输出明确,可单测。"""
    return [r.upper() for r in records if "bad" not in r]

def load(rows, dst_path, marker, batch_meta):
    """Load:先写临时文件再原子 rename。"""
    tmp = dst_path + ".tmp"
    with open(tmp, "w") as f:
        f.write("\n".join(rows))
    os.replace(tmp, dst_path)                      # 原子替换
    with open(marker, "w") as f:
        json.dump(batch_meta, f)

if __name__ == "__main__":
    src, dst, marker = "src.txt", "dst.txt", ".processed"
    with open(src, "w") as f:
        f.write("apple\nBAD seed\nbanana\n")
    rows = transform(extract(src, marker))
    load(rows, dst, marker, {"batch": "2026-11-01", "rows": len(rows)})
    print(open(dst).read().splitlines(), open(marker).read())
    os.remove(src); os.remove(dst); os.remove(marker)
```

**追问**:
- 水位推进为什么「先处理后提交」?——先推进再处理,失败就丢数据;处理成功后提交水位,重复执行由幂等写入兜底。
- 断点续跑的粒度?——按任务内分片(文件/分区/批)记录完成标记,失败从最小未完成片重跑,而不是整任务重来。
- Transform 层为什么要保持纯函数?——不碰外部状态才能单测、才能并发重跑;IO 与计算分离后,任何一步都能本地复现。

---
