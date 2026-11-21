"""命中率的分母口径: 谁进分母, 谁决定你看到的百分比"""
hit, miss, bypass, expired = 300, 100, 600, 50
# hit 命中; miss 未命中回源; bypass 不该走缓存的个性化请求; expired 命中但已过期触发回源

strict = hit / (hit + miss) * 100
with_bypass = hit / (hit + miss + bypass) * 100
expired_as_hit = (hit + expired) / (hit + miss + expired) * 100
print("口径一 只算缓存层请求: %.0f%% (组件视角)" % strict)
print("口径二 bypass 也进分母: %.0f%% (业务视角)" % with_bypass)
print("口径三 过期重建算命中: %.0f%% (会高估新鲜度)" % expired_as_hit)
print("三个口径都自洽, 混用就是事故: 看板必须声明口径, 跨系统对比先对齐分母")
