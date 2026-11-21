"""TTL 随机抖动打散过期时间"""
import random
import statistics

BASE_TTL = 3600


def ttl_with_jitter(base: int = BASE_TTL, ratio: float = 0.1) -> float:
    """在 base 上下浮动 ratio 比例, 避免同一批 key 同时失效"""
    return base * (1 + random.uniform(-ratio, ratio))


if __name__ == "__main__":
    ttls = [ttl_with_jitter() for _ in range(1000)]
    same_time = sum(1 for t in ttls if abs(t - BASE_TTL) < BASE_TTL * 0.001)
    print(f"标准差 {statistics.pstdev(ttls):.1f}s, 极接近基准点的比例 {same_time / 1000:.1%}")
    print("秒级分布样例:", sorted(int(t) for t in ttls[:5]))
    # 固定 TTL 时 1000 个 key 的到期时间完全相同 -> 雪崩
    # 加抖动后到期时间均匀散开, DB 瞬时压力被摊平
