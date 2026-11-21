"""模拟编码切换阈值 + zset 双结构分工; 有 redis 时打印真实 OBJECT ENCODING"""
import sys

THRESHOLDS = {"list-max-listpack-size": 128, "hash-max-listpack-entries": 128,
              "zset-max-listpack-entries": 128, "zset-max-listpack-value": 64}

class MiniZSet:
    """listpack 阶段: 单列表; 超阈值升级 skiplist+dict 双结构"""
    def __init__(self):
        self.mode = "listpack"
        self.pairs = []          # [(member, score)]
        self.dict = {}           # member -> score

    def add(self, member, score):
        if self.mode == "listpack":
            self.pairs.append((member, score))
            if len(self.pairs) > THRESHOLDS["zset-max-listpack-entries"] or \
               len(member) > THRESHOLDS["zset-max-listpack-value"]:
                self.mode = "skiplist"
                self.dict = dict(self.pairs)
        else:
            self.dict[member] = score

if __name__ == "__main__":
    z = MiniZSet()
    for i in range(THRESHOLDS["zset-max-listpack-entries"] + 1):
        z.add(f"m{i}", i)
    print("元素超阈值后编码:", z.mode, "<- listpack 升级为 skiplist")
    print("skiplist 管 zrangebyscore, dict 管 zscore, 两者共享元素")

    try:
        import redis
        r = redis.Redis(decode_responses=True)
        r.zadd("enc_demo", {"a": 1})
        print("真实编码(小 zset):", r.object("ENCODING", "enc_demo"))
        r.delete("enc_demo")
    except Exception as e:
        print("无可用 redis, 仅演示:", type(e).__name__)
