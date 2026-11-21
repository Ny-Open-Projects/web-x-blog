import random
from datetime import datetime


def discount_at(now: datetime) -> int:
    # 时间作为参数注入,而不是内部调用 datetime.now
    if now.weekday() >= 5:
        return 20
    return 10


def random_pick(rng: random.Random, items: list[str]) -> str:
    return rng.choice(items)


def test_weekend_discount():
    sat = datetime(2024, 1, 6)
    assert discount_at(sat) == 20

def test_weekday_discount():
    wed = datetime(2024, 1, 3)
    assert discount_at(wed) == 10

def test_random_seeded():
    rng = random.Random(42)
    seq1 = [random_pick(rng, ["a", "b"]) for _ in range(5)]
    rng2 = random.Random(42)
    seq2 = [random_pick(rng2, ["a", "b"]) for _ in range(5)]
    assert seq1 == seq2
