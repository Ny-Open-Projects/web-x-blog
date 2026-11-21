"""用 Python 函数模拟 EVAL 扣库存脚本, 展示 KEYS/ARGV 分离与原子性"""
import threading

STOCK_LUA = """
local stock = tonumber(redis.call('GET', KEYS[1]) or '-1')
local want  = tonumber(ARGV[1])
if stock >= want then
  return redis.call('DECRBY', KEYS[1], want)
else
  return -1
end
"""

class FakeRedis:
    def __init__(self):
        self.store = {"stock:1": 10}
        self.lock = threading.Lock()

    def eval(self, script, keys, args):
        """逐行解释脚本语义的等价实现(教学用)"""
        with self.lock:                          # redis 单线程: 脚本天然原子
            key, want = keys[0], int(args[0])
            stock = int(self.store.get(key, -1))
            if stock >= want:
                self.store[key] = stock - want
                return self.store[key]
            return -1

if __name__ == "__main__":
    r = FakeRedis()
    print("脚本:\n" + STOCK_LUA.strip())
    print("扣 5 件 ->", r.eval(STOCK_LUA, ["stock:1"], [5]))
    print("再扣 6 件 ->", r.eval(STOCK_LUA, ["stock:1"], [6]), "<- 不足返回 -1")
    print("剩余:", r.store["stock:1"])
