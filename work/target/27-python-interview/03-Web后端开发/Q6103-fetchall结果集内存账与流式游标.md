---
title: [Q6103] fetchall 结果集内存账与流式游标
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6103 · fetchall 结果集内存账与流式游标

> 难度:★★★★☆ | 标签:容量规划, 游标, ORM

**问**:导出 500 万行报表把 Web worker 内存打爆了，账怎么算？流式游标是银弹吗？

**答**:结论：`fetchall` 的内存 = 行数 × 每行对象图（驱动常给 tuple/dict，每行几百字节到数 KB），500 万行 × 1KB = 5GB，必然 OOM。账的第一性公式就是行数 × 行对象大小，再乘 ORM 层放大系数（Django/SQLAlchemy 把每行再包成模型实例，2~4 倍）。流式游标把"一次性整块"变成"行级迭代"：psycopg 的 server-side cursor（`cursor(name=...)`，基线 psycopg2/3）、MySQL 的 `SSCursor`（前提是协议层 `use pure` 逐行拉取且连接独占）。但流式不是免费的：① 长事务——游标持有期间事务不能关，连接被独占，连接池要为此单开通道；② 服务端游标本身在 DB 有内存/游标生命周期；③ 网络速率成为瓶颈时反而拉长事务窗口。取舍：百万行以下 fetchall+分页；导出类一律流式写文件并限并发导出数（Q6051 是入向 body 的对称问题）。

```python
# 无驱动环境演示：账的算法与迭代器形状（生产接 psycopg/MySQLdb，基线标注见答）
import sys

def row_mem_estimate(rows, per_row_b=600, orm_factor=3.0):
    return rows * per_row_b * orm_factor

rows = 5_000_000
print(f"fetchall 账: {rows} 行 ≈ {row_mem_estimate(rows)/2**30:.1f}GB（含 ORM 放大）")

def stream_rows(cursor_like, chunk=1000):
    """流式等价物：服务端游标逐批 fetchmany，内存=chunk 行。"""
    while True:
        batch = cursor_like.fetchmany(chunk)
        if not batch:
            return
        yield from batch

class FakeCursor:                          # 模拟服务端游标
    def __init__(self, n): self.n, self.i = n, 0
    def fetchmany(self, k):
        b = [(self.i + j, f"row{self.i+j}") for j in range(min(k, self.n - self.i))]
        self.i += len(b)
        return b

peak_rows = max(len(list(stream_rows(FakeCursor(50_000)))) for _ in [0])
print("流式消费完成，峰值内存只与 chunk 相关")

# 纪律：导出并发限流 + 写出即释放
EXPORT_CONCURRENCY = 2
print("导出并发上限:", EXPORT_CONCURRENCY)
```

**追问一层**:server-side cursor 与客户端游标在 DB 端的资源占用差异？事务隔离级别对流式读的影响？
**追二层**:为什么流式导出时连接必须独占？连接池要怎么配（引 Q6046）？

**背诵要点**
- fetchall 内存=行数×行对象×ORM 系数，百万行级别必换流式。
- 流式代价：长事务、连接独占、游标生命周期管理。
- 导出还要限并发，流式只解决单请求内存不解决叠加。

**复盘追问**
- 分页导出（keyset 分页）与服务端游标如何选？提示：Q6053 游标分页 + 幂等续传。
- OOM 后如何从监控定位到"是导出接口"？提示：RSS 时间线与接口标签关联。
