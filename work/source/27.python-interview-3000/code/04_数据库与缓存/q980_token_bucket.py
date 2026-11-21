"""令牌桶: 懒惰补充 + 突发容忍"""
import time

class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate, self.capacity = rate, capacity      # 每秒令牌数, 桶容量
        self.tokens, self.last = capacity, time.monotonic()

    def allow(self, cost=1.0):
        now = time.monotonic()
        self.tokens = min(self.capacity,             # 补充并封顶
                          self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False

if __name__ == "__main__":
    tb = TokenBucket(rate=2, capacity=5)               # 均速2/s 突发可到5
    print("瞬时突发 5 次:", [tb.allow() for _ in range(5)], "<- 容量内全过")
    print("第 6 次:", tb.allow())
    time.sleep(0.6)                                    # 攒回约 1.2 个令牌
    print("0.6s 后:", tb.allow(), "<- 速率控制恢复节奏")
    print(f"剩余令牌 {tb.tokens:.2f}")
