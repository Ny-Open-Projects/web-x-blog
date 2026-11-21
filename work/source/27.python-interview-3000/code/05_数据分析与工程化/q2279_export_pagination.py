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
