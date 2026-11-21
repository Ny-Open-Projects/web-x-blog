"""写穿透与写回的失败注入: 写穿透失败是阻塞, 写回失败是丢数据"""
class FlakyCache:
    def __init__(self):
        self.data = {}
        self.fail_put = False
        self.fail_flush = False

    def put(self, k, v):
        if self.fail_put:
            raise IOError("缓存不可写")
        self.data[k] = v

    def flush(self, pending):
        if self.fail_flush:
            raise IOError("刷盘失败")
        self.data.update(pending)


db = {}
cache = FlakyCache()

# 写穿透: 先落库再写缓存, 缓存写失败按失效处理, 不留旧值
cache.fail_put = True
try:
    db["p:1"] = "新值"
    cache.put("p:1", "新值")
except IOError as e:
    cache.data.pop("p:1", None)
    print("写穿透失败: %s -> 库已更新, 缓存按失效处理, 下次读回源" % e)
cache.fail_put = False
cache.put("p:1", "新值")
print("写穿透恢复: 缓存 %s" % cache.data)

# 写回: 请求只写缓存即返回, 刷盘前崩溃就是永久丢失
dirty = {"p:2": "新值"}
print("写回: 请求已返回, 脏数据 %s 尚未落库, db 里还是 %s" % (dirty, db.get("p:2")))
cache2 = FlakyCache()
cache2.fail_flush = True
try:
    cache2.flush(dirty)
except IOError as e:
    print("写回失败: %s -> 若此刻进程崩溃, p:2 的写入永久丢失" % e)
print("结论: 可丢数据才用纯写回, 要保数据配预写日志, 或直接退回写穿透")
