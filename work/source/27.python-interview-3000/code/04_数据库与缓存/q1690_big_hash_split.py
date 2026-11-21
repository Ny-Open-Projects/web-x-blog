"""大 hash 分段: 单 key 过大的拆分路由与聚合读取"""
import hashlib

FIELDS = 100000

def bucket_of(field, n_bucket=16):
    h = int(hashlib.md5(field.encode()).hexdigest(), 16)
    return h % n_bucket

# 拆分前: 一个 hash 10 万 field, HGETALL 会阻塞整个实例
big = {f"item:{i}": i * 2 for i in range(FIELDS)}
print(f"拆分前: 1 个 key, {FIELDS} 个 field")

# 拆分后: 按 field 哈希路由到 16 个桶
shards = [dict() for _ in range(16)]
for k, v in big.items():
    shards[bucket_of(k)][k] = v
print("拆分后各桶 field 数:", [len(s) for s in shards])

def hget(field):
    return shards[bucket_of(field)].get(field)

def hgetall():
    out = {}
    for s in shards:
        out.update(s)
    return out

print("点查路由正确:", hget("item:12345") == big["item:12345"])
print("聚合全量 field 数:", len(hgetall()))
print("工程要点: 桶数固定可预估; 批量读按桶分组再 pipeline; 删 key 要遍历所有桶;")
print("          路由函数一旦上线不可更换, 换桶数等于全量迁移; 桶内仍大可二次拆分")
