"""哨兵 vs 集群: 两种高可用模型的职责差异"""
import zlib

def slot(key):
    return zlib.crc32(key.encode()) % 16384   # 真实 Redis 用 CRC16, 此处示意

for k in ("user:1", "user:2", "order:100", "user:1:profile"):
    print(k, "-> 槽", slot(k))
print("hash tag user:{1}:x 可强制同槽, 支撑多 key 命令")
print("哨兵: 不分片, 容量上限 = 单机, 提供故障转移")
print("集群: 分片 + 高可用, 写入水平扩展, 但多 key 命令受槽约束")
