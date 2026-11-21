"""按写入速率估算自增 ID 耗尽时间, 演示容量规划"""
from datetime import datetime, timedelta

INT_MAX = 2_147_483_647
BIGINT_MAX = 9_223_372_036_854_775_807

def days_left(current, rate_per_sec, unsigned=False):
    cap = (4_294_967_295 if unsigned else INT_MAX) - current
    return cap / rate_per_sec / 86400

if __name__ == "__main__":
    for name, cur, rate in [("订单表", 1_900_000_000, 500),
                            ("消息流水", 2_000_000_000, 5000),
                            ("小业务表", 500_000_000, 10)]:
        print(f"{name}: 剩余 {days_left(cur, rate):.0f} 天耗尽"
              f" (按 {rate}/s, 有符号 int)")
    print(f"bigint 上限 {BIGINT_MAX}, 以 5000/s 也需 "
          f"{BIGINT_MAX / 5000 / 86400 / 365:.0f} 年")
