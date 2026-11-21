"""秒杀: Lua 原子扣减 + 一人一单 + MQ 异步落库(模拟)"""
import queue
import threading

SECKILL_LUA = """
local stock = tonumber(redis.call('GET', KEYS[1]) or '0')
if redis.call('SETNX', KEYS[2], ARGV[1]) == 0 then
  return -2                                    -- 一人一单: 重复
end
if stock <= 0 then
  redis.call('DEL', KEYS[2])                   -- 回收资格
  return -1                                    -- 售罄
end
redis.call('DECR', KEYS[1])
return 1
"""

class FakeRedis:
    def __init__(self, stock):
        self.kv = {"stock": stock}
        self.lock = threading.Lock()

    def eval(self, script, keys, args):
        with self.lock:
            key_stock, key_user = keys
            if key_user in self.kv:              # SETNX 已存在: 重复下单
                return -2
            stock = int(self.kv.get(key_stock, 0))
            if stock <= 0:
                return -1                        # 售罄
            self.kv[key_user] = "1"              # 记录资格
            self.kv[key_stock] = stock - 1
            return 1

if __name__ == "__main__":
    r = FakeRedis(stock=3)
    mq = queue.Queue()
    def buyer(uid):
        rc = r.eval(SECKILL_LUA, ["stock", f"u:{uid}:order"], [uid])
        if rc == 1:
            mq.put(uid)                          # 成功才入队落库
        return rc
    codes = {}
    uids = [0, 1, 2, 3, 4, 0]                    # 最后一个是重复用户
    ts = [threading.Thread(target=lambda i=i: codes.__setitem__(i, buyer(uids[i])))
          for i in range(len(uids))]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print("扣减结果:", codes, "<- 3 个 1 成功, 1 个 -1 售罄, 1 个 -2 重复")
    print("MQ 待落库:", list(mq.queue), "-> 消费者建订单, 失败幂等回补")
