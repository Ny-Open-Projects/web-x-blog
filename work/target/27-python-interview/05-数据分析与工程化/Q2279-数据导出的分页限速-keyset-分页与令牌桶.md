---
title: [Q2279] 数据导出的分页限速:keyset 分页与令牌桶
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2279 · 数据导出的分页限速:keyset 分页与令牌桶

> 难度:★★★☆ | 标签:导出, 限流

**问**:业务要批量导出千万行数据,直接给一个全量接口会被打挂,你怎么设计?

**答**:两个机制组合。分页用 keyset 而不是 offset:每页返回下一页游标(上一页最后一行的键),深翻页性能恒定且翻页期间数据变动不影响一致性;offset 分页翻到十万页时数据库要扫过前面所有行,必挂。限速用按客户端的令牌桶:每秒补充固定令牌、桶有容量上限,取不到令牌直接返回限流响应,客户端拿到明确的"稍后重试"而不是拖死服务端。实测 1000 行按 200 行一页,令牌桶 burst 3 时前三页成功,第四页被限流,cursor 停在 599,客户端退避后带 cursor 续传——断点续传是 keyset 的天然副产品。导出任务还应支持后台异步生成加下载链接,同步接口只服务小批量;限流配额按客户端分级,大客户单独配额池。

```python
# file: code/05_数据分析与工程化/q2279_export_pagination.py
"""数据导出的分页限速: keyset 分页与令牌桶"""

import time


class TokenBucket:
    def __init__(self, rate_per_sec, burst):
        self.rate, self.burst = rate_per_sec, burst
        self.tokens = float(burst)
        self.last = time.monotonic()

    def take(self, n=1):
        now = time.monotonic()
        self.tokens = min(self.burst, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= n:
            self.tokens -= n
            return True
        return False   # 简化: 不等待, 直接拒绝让客户端退避


def export_page(table, cursor=None, page_size=200, bucket=None):
    """模拟 keyset 分页: cursor 是上一页最后一行 id"""
    if bucket is not None and not bucket.take():
        return [], cursor, "rate_limited"
    start = 0 if cursor is None else cursor + 1
    end = min(start + page_size, 1000)   # 表里共 1000 行
    rows = list(range(start, end))
    return rows, (rows[-1] if rows else cursor), "ok"


if __name__ == "__main__":
    bucket = TokenBucket(rate_per_sec=1000, burst=3)
    cursor, pages, fetched = None, 0, 0
    while cursor is None or cursor < 999:
        rows, cursor, status = export_page("orders", cursor, 200, bucket)
        if status == "rate_limited":
            print(f"第 {pages + 1} 页被限流, 客户端应退避重试, cursor 停在 {cursor} 可续传")
            break
        pages += 1
        fetched += len(rows)
        print(f"页 {pages}: 行 {rows[0]}-{rows[-1]} cursor={cursor}")
    print(f"已取 {fetched} 行; keyset 深翻页不退化, 限流按客户端配额, cursor 即断点")
```

**追问**:
- 追问 1:keyset 的游标键怎么选?—— 唯一且单调的列(自增 id 或 时间加id 复合),键不唯一会漏行或重行,复合键在排序里也要保持唯一序。
- 追问 2:导出期间数据在变怎么办?—— 按快照读或带上界条件(如 updated_at 小于任务开始时间),保证导出自洽。
