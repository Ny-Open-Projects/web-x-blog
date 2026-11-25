---
title: "[Q6734] 批量 INSERT 拼成一条 SQL：包超限被服务端直接断开"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6734 · 批量 INSERT 拼成一条 SQL：包超限被服务端直接断开

难度：P6 ｜ 标签：MySQL、max_allowed_packet、批量写入、错误码

基线：Python 3.12；MySQL 8.0 `max_allowed_packet` 默认 64MB（5.7 为 4MB）；纯 Python 模拟按字节预算分批。

**问**：为了提速把 5000 行拼成一条 `INSERT INTO t VALUES (...),(...)`，本地跑得很好，线上偶发 `MySQL server has gone away` / `Got a packet bigger than 'max_allowed_packet' bytes`，重试还是失败。行数没变，为什么换个环境就炸？

**答**：
- **结论**：`max_allowed_packet` 限制**单条 SQL 语句或单个网络包**的大小，服务端与客户端各有一份，实际生效取较小值。超限时服务端不是返回普通 SQL 错误，而是**直接关闭连接**（`ER_NET_PACKET_TOO_LARGE` 1153），客户端看到的往往是 `2006 server has gone away`。因为是连接级错误，重试同样失败，池里那条连接也废了。默认值：8.0 是 64MB，5.7 及更早是 4MB；云数据库参数模板、代理层还各有自己的上限。
- **取舍**：多值 INSERT 把 N 次 RTT 压成 1 次，写入吞吐提升非常明显；但单语句过长会带来四个副作用：超出 packet、binlog 事件巨大（从库回放尖刺）、锁持有时间变长、失败时整条回滚。所以分批要按**字节预算**（如 512KB~1MB/批）而不是按行数——一行 2KB 的文本和一行 20 字节的 ID 完全不是一回事。
- **实战**：① 批次大小按 `sum(len(col.encode())) + 开销` 累加，达阈值 flush，并给单行超限单独的逃生路径（超长文本改单行 INSERT）；② 客户端与服务端 `max_allowed_packet` 对齐，启动时 `SHOW VARIABLES` 校验；③ `executemany` 在多数驱动里同样会拼多值语句，受同一限制；④ 批次序号写进日志，失败能定位到"哪一批"并单独重放。

```python
"""按字节预算分批，而不是按行数分批。"""


def encode_row(row: tuple[str, ...]) -> int:
    """估算一行在 SQL 里占的字节：值 + 引号/逗号/括号的固定开销。"""
    return sum(len(v.encode("utf-8")) for v in row) + 2 * len(row) + 3


def batches_by_rows(rows: list[tuple[str, ...]], per_batch: int):
    for i in range(0, len(rows), per_batch):
        yield rows[i:i + per_batch]


def batches_by_bytes(rows: list[tuple[str, ...]], max_bytes: int):
    buf: list[tuple[str, ...]] = []
    size = 0
    for row in rows:
        n = encode_row(row)
        if buf and size + n > max_bytes:
            yield buf
            buf, size = [], 0
        if n > max_bytes:
            raise ValueError(f"单行 {n} 字节已超过批次上限 {max_bytes}，需拆列或单行写")
        buf.append(row)
        size += n
    if buf:
        yield buf


if __name__ == "__main__":
    # 20000 行短 ID + 1 行 700KB 的备注，模拟"行数不多但字节爆炸"
    rows = [(str(i), "x" * 10) for i in range(20000)]
    rows.append(("20000", "y" * (700 * 1024)))

    LIMIT = 1024 * 1024
    by_row = list(batches_by_rows(rows, 20001))
    total = sum(encode_row(r) for r in by_row[0])
    print(f"按行数分 1 批，估算 {total} 字节，超 1MB:", total > LIMIT)

    by_size = list(batches_by_bytes(rows, LIMIT))
    print("按字节分", len(by_size), "批，各批字节:",
          [sum(encode_row(r) for r in b) for b in by_size])

    # 单行本身就超过上限：必须拆列或单独走单行 INSERT（改小 limit 复现）
    try:
        list(batches_by_bytes([("x", "z" * 8000)], 4096))
    except ValueError as e:
        print("单行超限:", e)
    print("结论：行数不是容量单位，字节数才是；超长行要单独逃生")
```

**追问一**：为什么线上的 `max_allowed_packet` 会比本地小？
→ 解析：本地常用 docker 或自建 `my.cnf` 调大过；云数据库走参数模板默认值，代理/负载均衡层还可能再压一遍包大小。客户端侧（如 mysqlclient 的 `max_allowed_packet` 参数）默认也可能只有 16MB，先撞的是它。

**追问二**：超限之后为什么这条连接不能放回池里复用？
→ 解析：服务端已经 `close()`，客户端要到下次读写才发现（半开连接），拿到的错误是 `BrokenPipeError` / `server has gone away`。必须把该连接标记为坏连接并 `close()`，不能归还；`pool_pre_ping=True` 能在借出时探活，但多一次 RTT，通常只对闲置连接开启。
