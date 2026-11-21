"""纯逻辑实现 nested loop 与 hash join, 对比操作次数"""
from itertools import product

def nested_loop(a, b):
    ops = 0
    out = []
    for ra in a:
        for rb in b:
            ops += 1
            if ra["k"] == rb["k"]:
                out.append((ra, rb))
    return out, ops

def hash_join(a, b):
    ops = 0
    table = {}
    for rb in b:                      # build: 内表建哈希
        table.setdefault(rb["k"], []).append(rb)
    out = []
    for ra in a:                      # probe: 外表探测
        ops += 1
        for rb in table.get(ra["k"], ()):
            out.append((ra, rb))
    return out, ops

if __name__ == "__main__":
    A = [{"k": i % 100, "v": i} for i in range(1000)]
    B = [{"k": i % 100, "v": i} for i in range(1000)]
    _, ops1 = nested_loop(A, B)
    _, ops2 = hash_join(A, B)
    print(f"nested loop 比较 {ops1} 次, hash join {ops2} 次")
    print("MySQL 对照: 内表无索引的等值 JOIN 在 8.0.18 起用 hash join 替代 BNL")
