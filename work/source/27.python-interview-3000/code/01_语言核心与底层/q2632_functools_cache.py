"""functools.cache:无界缓存的命中、风险与 lru 对照。"""
import functools


@functools.cache
def square(n):
    hits[0] += 1
    return n * n


hits = [0]


@functools.lru_cache(maxsize=2)
def small_lru(n):
    return n * n


if __name__ == "__main__":
    square(4)
    square(4)
    square(5)
    print("实际计算次数:", hits[0], "缓存信息:", square.cache_info())

    small_lru(1); small_lru(2); small_lru(3)   # 挤掉 1
    print("lru(2) 命中:", small_lru.cache_info())
    print("1 已被淘汰,重新计算后:", small_lru(1), small_lru.cache_info())

    # 风险演示:返回可变对象,缓存会被调用方改掉
    @functools.cache
    def default_list():
        return []

    default_list().append("污染")
    print("第二次拿到:", default_list(), "(同一对象被改)")
