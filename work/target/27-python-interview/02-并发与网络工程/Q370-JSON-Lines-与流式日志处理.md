---
title: [Q370] JSON Lines 与流式日志处理
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q370 · JSON Lines 与流式日志处理

> 难度:★★☆ | 标签:JSON Lines, 日志, 流式

**问**:为什么生产日志常用 JSON Lines 而不是一行文本?如何流式处理一个大到读不进内存的 JSONL 文件?

**答**:JSONL(每行一个 JSON 对象)兼具结构化(可按字段检索、喂给 ELK)与行分割(可逐行流式读、`wc -l`、断点续读)两大优点。处理大文件用逐行迭代,文件对象本身就是惰性迭代器,内存 O(1);坏行做隔离计数而不是中断。写侧要保证"单行原子性":一次 write 一行且带换行。读侧还有个易踩的坑:一行可能是合法 JSON 但不是对象(比如一个裸字符串、数组、数字),`json.loads` 不报错,直接 `.get()` 却会 AttributeError——解析后要先 isinstance 校验再取字段,非对象行同样按坏行隔离。

```python
# file: code/02_并发与网络工程/q370_jsonl.py
"""JSON Lines 写入与流式读取统计。"""
import json


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")  # 一行一对象


def stream_stats(path):
    """逐行流式统计,内存占用与文件大小无关。"""
    total, bad, levels = 0, 0, {}
    with open(path, encoding="utf-8") as f:
        for line in f:  # 惰性迭代,不整读内存
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                rec = json.loads(line)
                # 合法 JSON 不一定是对象(裸字符串/数组/数字), 先校验再取字段
                if not isinstance(rec, dict):
                    bad += 1  # 非对象行按坏行隔离,不中断
                    continue
                levels[rec.get("level", "?")] = levels.get(rec.get("level", "?"), 0) + 1
            except json.JSONDecodeError:
                bad += 1  # 坏行隔离计数,不中断
    return total, bad, levels


if __name__ == "__main__":
    recs = [
        {"ts": "2026-11-01T10:00:00", "level": "INFO", "msg": "start"},
        {"ts": "2026-11-01T10:00:01", "level": "ERROR", "msg": "db down"},
        "这不是合法 JSON 行",  # 模拟写坏的行(裸字符串, JSON 合法但不是对象)
    ]
    write_jsonl("/tmp/app.jsonl", recs)
    print(stream_stats("/tmp/app.jsonl"))
```

**追问**:
- JSONL 与一个大 JSON 数组相比的优势?JSONL 可流式解析、按行追加、失败只影响一行;大数组必须整体解析且追加要重写全文件。
- 如何只读文件最后 N 行?二进制方式 seek 到末尾向前按块找换行符(`tail -n` 原理)。

```mermaid
flowchart LR
    A[应用进程] -->|逐行 write| B[app.jsonl 日志文件]
    B -->|Filebeat tail| C[采集器]
    C -->|批量发送| D[Kafka 或 消息队列]
    D --> E[Logstash 解析]
    E --> F[Elasticsearch 存储]
    F --> G[Kibana 查询]
```
