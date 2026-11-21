"""水平分片路由: hash 取模 2 库 x 4 表"""
DB_COUNT, TABLE_PER_DB = 2, 4


def route(user_id: int) -> tuple:
    """返回 库名 与 表名"""
    shard = user_id % (DB_COUNT * TABLE_PER_DB)      # 全局槽位
    db = shard // TABLE_PER_DB
    table = shard % TABLE_PER_DB
    return f"db{db}", f"orders_{table:03d}"


if __name__ == "__main__":
    samples = [1, 2, 7, 8, 9999, 123456]
    for uid in samples:
        db, table = route(uid)
        print(f"user_id={uid} -> {db}.{table}")

    # 验证分布均匀性
    from collections import Counter
    dist = Counter(route(u)[0] for u in range(100_000))
    print("10 万用户分布:", dict(dist))
    # 扩容: 2 库扩 4 库需按新模数迁移, 一致性 hash 或 预分槽(如 1024 槽)可缓解
