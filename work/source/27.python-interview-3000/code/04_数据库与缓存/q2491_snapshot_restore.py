"""本地缓存的快照恢复: 重启后跳过冷重建直接热身"""
import json

class TickClock:
    def __init__(self):
        self.now = 0

cache = TickClock()
cache.now = 100
# 运行中的缓存: key -> [value, expire_at, rebuild_cost (模拟回源代价)]
cache.entries = {
    "hot:1": ["v1", 150, 50],      # 仍新鲜
    "hot:2": ["v2", 180, 30],      # 仍新鲜
    "cold:3": ["v3", 110, 80],     # 已过期, 不值得恢复
    "cold:4": ["v4", 105, 20],     # 已过期
}

def snapshot(cache, path):
    fresh = {k: [v, e] for k, (v, e, c) in cache.entries.items() if e > cache.now}
    with open(path, "w") as f:
        json.dump({"saved_at": cache.now, "entries": fresh}, f)
    return len(fresh)

def restore(path):
    with open(path) as f:
        snap = json.load(f)
    entries = {}
    skipped = 0
    for k, (v, e) in snap["entries"].items():
        if e > snap["saved_at"] + 1:               # 恢复时再校验一次新鲜度
            entries[k] = [v, e, 0]                 # 恢复的键 rebuild_cost = 0
        else:
            skipped += 1
    return entries, skipped

n = snapshot(cache, "/tmp/cache_snap.json")
entries, skipped = restore("/tmp/cache_snap.json")
cold_cost = sum(c for k, (v, e, c) in cache.entries.items() if e > cache.now)
print("停机前 %d 个键, 快照保留 %d 个新鲜键, 恢复时剔除 %d 个临界过期键"
      % (len(cache.entries), n, skipped))
print("恢复后的键: %s" % sorted(entries))
print("跳过的冷重建代价: %d 个成本单位, 相当于省掉 %d 次回源"
      % (cold_cost, cold_cost // 10))
print("结论: 本地缓存快照要带过期时间与版本一起落盘, 恢复时宁可错杀临界键;")
print("      它不是预热任务的替代, 是'计划内重启'与'热身捷径'的低成本兜底")
