"""排序规则不一致的 JOIN: 每行转换使索引失效的代价模拟"""
import time

N_A, N_B = 20000, 20000
codes_a = [f"SKU{i:06d}" for i in range(N_A)]                            # general_ci 侧
codes_b = [f"SKU{i:06d}" if i % 2 else f"sku{i:06d}" for i in range(N_B)]  # unicode_ci 侧

a_set = set(codes_a)
a_set_lower = set(c.lower() for c in codes_a)

t0 = time.perf_counter()
hits_direct = sum(1 for v in codes_b if v in a_set)
t1 = time.perf_counter()
hits_conv = sum(1 for v in codes_b if v.lower() in a_set_lower)  # 逐行转换 无法直接命中索引
t2 = time.perf_counter()

print(f"collation 一致: 命中 {hits_direct}, {(t1 - t0) * 1000:.1f} ms")
print(f"collation 不一致逐行转换: 命中 {hits_conv}, {(t2 - t1) * 1000:.1f} ms")
print("统一 charset 与 collation, 或在生成列上预转换, 比硬扛便宜得多")
