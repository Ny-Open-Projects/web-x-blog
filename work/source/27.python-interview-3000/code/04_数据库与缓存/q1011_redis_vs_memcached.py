"""两种缓存的能力矩阵对照"""
MATRIX = """
能力            Redis            Memcached
数据结构        string/hash/list/zset/stream   仅 string
持久化          RDB/AOF/混合      无
高可用          哨兵/集群/复制    客户端一致性哈希
原子脚本        Lua               无(仅 cas)
内存模型        按需分配+淘汰     slab 预分配
多线程          6.0 io 多线程     多线程工作线程
适用            结构化+高级语义   纯 KV 大内存池缓存
"""
if __name__ == "__main__":
    print(MATRIX)
    print("选型: 要结构/持久化/锁 -> Redis; 纯 string 缓存要极致多核 -> Memcached")
