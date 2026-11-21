"""缓存读放大: 一次请求 20 次往返的治理"""
import time

RTT = 0.001                                       # 模拟一次缓存往返 1 ms

def rtt(n=1):
    time.sleep(RTT * n)
    return n * RTT * 1000

# 方式一: 逐键 GET, 一次页面请求 20 次往返
fields = ["f%d" % i for i in range(20)]
t0 = time.perf_counter()
ms_naive = rtt(len(fields))
per_key_bytes = sum(30 for _ in fields)           # 每键 30 字节
print("逐键 GET:   %2d 次往返, 传输 %3d 字节, 耗时 %.1f ms" % (len(fields), per_key_bytes, ms_naive))

# 方式二: MGET 一次往返取全部键
t0 = time.perf_counter()
ms_mget = rtt(1)
print("MGET 批量:   1 次往返, 传输 %3d 字节, 耗时 %.1f ms" % (per_key_bytes, ms_mget))

# 方式三: 字段合并成一个大 hash 键, 一次往返 + 一次 HGETALL
merged_bytes = per_key_bytes + len(fields) * 8    # 字段名开销
t0 = time.perf_counter()
ms_hash = rtt(1)
print("合并大键:    1 次往返, 传输 %3d 字节, 耗时 %.1f ms" % (merged_bytes, ms_hash))

print("代价对账: 逐键方式把 20 倍 RTT 藏在了代码里; 合并键最快但制造大 key,")
print("      更新任一字段要重写整个值且失去单字段 TTL;")
print("      工程默认选 MGET, 合并键只用于字段总是整取整存的聚合对象")
