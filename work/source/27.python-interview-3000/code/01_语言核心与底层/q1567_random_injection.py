import random


def pick_winners(pool, k, rng=None):
    """rng 是接缝:默认真随机,测试注入带 seed 的实例。"""
    rng = rng or random.Random()
    return rng.sample(sorted(pool), k)


def jittered_backoff(attempt, base=0.1, rng=None):
    """退避抖动:注入 rng 才能确定性测试。"""
    rng = rng or random.Random()
    return base * (2 ** attempt) * rng.uniform(0.5, 1.5)


if __name__ == "__main__":
    users = ["u%03d" % i for i in range(20)]

    a = pick_winners(users, 3, rng=random.Random(42))
    b = pick_winners(users, 3, rng=random.Random(42))
    print("seeded twice identical:", a == b, a)

    c = pick_winners(users, 3, rng=random.Random(7))
    print("different seed differs:", a != c, c)

    # 局部实例互不污染:同一 seed 推进不同步数后序列错开
    rng_a = random.Random(1)
    rng_b = random.Random(1)
    for _ in range(5):
        rng_a.random()
    print("independent streams:", rng_a.random() != rng_b.random())

    delays = [round(jittered_backoff(i, rng=random.Random(0)), 4)
              for i in range(4)]
    print("backoff series:", delays)

    # 不写 seed 的默认行为:每次不同
    print("unseeded varies:", pick_winners(users, 3) != pick_winners(users, 3))
