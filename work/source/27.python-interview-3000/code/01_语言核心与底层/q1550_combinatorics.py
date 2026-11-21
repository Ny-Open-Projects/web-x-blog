import math
from itertools import combinations, permutations, product

CONFIG = {"env": ("dev", "prod"), "pool": (4, 8), "tls": (True, False)}


def sweep_size(config):
    size = 1
    for values in config.values():
        size *= len(values)
    return size


if __name__ == "__main__":
    cases = list(product(*CONFIG.values()))
    print("sweep", sweep_size(CONFIG), "cases:")
    for i, combo in enumerate(cases, 1):
        print("  case", i, dict(zip(CONFIG.keys(), combo)))

    pool = list(range(5))
    print("combinations C(5,2):", len(list(combinations(pool, 2))),
          "expected", math.comb(5, 2))
    print("permutations P(4)  :", len(list(permutations(range(4)))),
          "expected", math.factorial(4))
    print("powerset size      :", sum(math.comb(5, k) for k in range(6)))

    dup = [1, 1, 2]
    print("combinations on dup:", list(combinations(dup, 2)),
          "按位置产生, 含重复值")
    print("value-dedup first  :", list(combinations(sorted(set(dup)), 2)))

    print("product with repeat:", list(product((0, 1), repeat=2)))
