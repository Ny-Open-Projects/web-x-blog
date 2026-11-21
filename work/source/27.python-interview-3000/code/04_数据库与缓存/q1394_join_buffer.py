"""无索引 JOIN 的两条路: 块嵌套循环 BNL 与 hash join 的比较量对比"""
import random

random.seed(4)
N_L, N_R, BUF = 500, 5000, 100
left = [{"uid": i} for i in range(N_L)]
right = [{"uid": random.randrange(N_L)} for _ in range(N_R)]

def bnl_cost(l, r, buf):
    cmp = 0
    for i in range(0, len(l), buf):
        block = l[i:i + buf]
        for row in r:
            for b in block:
                cmp += 1
                if b["uid"] == row["uid"]:
                    pass
    return cmp

def hash_join_cost(l, r):
    ht = {}
    for row in l:
        ht.setdefault(row["uid"], []).append(row)
    return len(r)              # 内表逐行探测哈希表, 每次 O(1)

c1 = bnl_cost(left, right, BUF)
c2 = bnl_cost(left, right, N_L)
c3 = hash_join_cost(left, right)
print(f"join buffer=100: 约 {c1} 次比较")
print(f"join buffer=全表: 约 {c2} 次比较, 用内存换内表扫描遍数")
print(f"hash join: {c3} 次探测, MySQL 8.0.18 起等值 join 默认取代 BNL")
