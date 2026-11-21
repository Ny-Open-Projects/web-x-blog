"""布隆过滤器参数计算: 内存与哈希数"""
import math

def bloom_params(n, p):
    m = -n * math.log(p) / (math.log(2) ** 2)      # 位数
    k = (m / n) * math.log(2)                      # 哈希函数数
    return m, k

if __name__ == "__main__":
    for n, p in [(10**6, 0.01), (10**8, 0.01), (10**8, 0.001), (10**8, 0.1)]:
        m, k = bloom_params(n, p)
        print(f"n={n:>9.0e} 期望误判 {p:.3f} -> "
              f"{m / 8 / 1024 / 1024:8.1f} MB, k={k:.1f}")
    print("对照: 1 亿 key 存 set 约需数 GB, 布隆 1% 误判约 114MB")
    print("预留增长: 按 2 倍 n 估内存, 或布满后换种子重建")
