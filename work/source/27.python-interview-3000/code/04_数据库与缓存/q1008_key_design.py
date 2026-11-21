"""key 构造器 + TTL 抖动"""
import random

class KeyBuilder:
    def __init__(self, app="mall"):
        self.app = app

    def make(self, *parts) -> str:
        return ":".join([self.app] + [str(p).lower() for p in parts])

def ttl_with_jitter(base_sec, jitter_ratio=0.15):
    delta = base_sec * jitter_ratio
    return int(base_sec + random.uniform(-delta, delta))

if __name__ == "__main__":
    kb = KeyBuilder()
    print(kb.make("stock", "sku123"))
    print(kb.make("user", "profile", 10086))
    print("同批缓存 TTL 抖动:", [ttl_with_jitter(300) for _ in range(6)])
    print("无抖动 1000 个 key 同秒过期 -> 集体回源 = 惊群; 有抖动则错峰")
