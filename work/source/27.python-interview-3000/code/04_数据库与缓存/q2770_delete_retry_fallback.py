"""失效删除失败的兜底: 重试队列消化故障期, TTL 是最后防线"""
class FlakyRedis:
    def __init__(self):
        self.up = False
        self.data = {"p:42": "旧值"}

    def delete(self, k):
        if not self.up:
            raise IOError("redis 不可达")
        self.data.pop(k, None)

cache = FlakyRedis()
retry_queue = []
TTL_S = 60.0

def invalidate(k):
    try:
        cache.delete(k)
        return True
    except IOError:
        if k not in retry_queue:
            retry_queue.append(k)
        return False

ok = invalidate("p:42")
print("故障期失效请求:", "成功" if ok else "失败, 进入重试队列 %s" % retry_queue)
cache.up = True
flushed = 0
guard = 0
while retry_queue and guard < 100:
    guard += 1
    k = retry_queue.pop(0)
    try:
        cache.delete(k)
        flushed += 1
    except IOError:
        retry_queue.append(k)
print("恢复后补删 %d 个键, 剩余队列 %s" % (flushed, retry_queue))
print("若重试始终失败, 键上的 TTL %.0f 秒兜底: 最坏陈旧窗口 = min(补删成功时刻, TTL)" % TTL_S)
