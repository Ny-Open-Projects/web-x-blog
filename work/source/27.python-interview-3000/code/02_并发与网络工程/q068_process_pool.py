import math
from concurrent.futures import ProcessPoolExecutor


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(limit: int) -> int:
    return sum(1 for n in range(limit) if is_prime(n))


if __name__ == "__main__":
    limits = [100_000, 150_000, 200_000, 250_000]
    with ProcessPoolExecutor(max_workers=4) as pool:
        for limit, count in zip(limits, pool.map(count_primes, limits)):
            print(f"<{limit} 的素数个数: {count}")
