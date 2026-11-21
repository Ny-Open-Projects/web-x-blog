"""慢命令治理: O(N) 命令的一次性阻塞与分批切分"""
import time

big = {f"key{i}": i for i in range(20000)}

t0 = time.perf_counter()
all_keys = list(big.keys())            # 等价 KEYS: 一次性构造 2 万元素
t1 = time.perf_counter()

def scan_batches(d, count=500):
    ks = list(d)
    batches = 0
    for i in range(0, len(ks), count):
        ks[i:i + count]                # 每批只构造 500 元素, 单次阻塞极短
        batches += 1
    return batches

t2 = time.perf_counter()
batches = scan_batches(big)
t3 = time.perf_counter()
total1 = (t1 - t0) * 1000
print(f"KEYS 式一次完成: 总 {total1:.1f} ms, 单次阻塞 {total1:.1f} ms")
print(f"SCAN 式分批: {batches} 批, 单次阻塞约 {(t3 - t2) * 1000 / batches:.3f} ms")
print("治理: 高危命令上黑名单与审计, 客户端一律分批游标读取")
