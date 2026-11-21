"""碎片率计算与 activedefrag 决策模拟"""

def frag_ratio(rss_bytes, used_bytes):
    return rss_bytes / used_bytes

def advise(ratio, swapped=False):
    if swapped or ratio < 1.0:
        return "严重: 疑似 swap, 立即扩容/重启, 检查 maxmemory 与宿主内存"
    if ratio <= 1.1:
        return "健康"
    if ratio <= 1.5:
        return "观察: 记录趋势, 检查是否有大 key 反复增删"
    return "治理: 开启 activedefrag, UNLINK 删大 key, 评估扩容"

if __name__ == "__main__":
    cases = [(1.2e9, 1.0e9), (1.6e9, 1.0e9), (0.8e9, 1.0e9)]
    for rss, used in cases:
        r = frag_ratio(rss, used)
        print(f"rss={rss / 1e9:.1f}GB used={used / 1e9:.1f}GB "
              f"ratio={r:.2f} -> {advise(r)}")
    print("注意: used_memory_peak 高峰回落期 ratio 偏高属正常, 看趋势不看单点")
