"""模糊匹配: 带截断的编辑距离 + 先裁候选集再算距离"""
import random
import sqlite3

def edit_distance_bounded(a, b, cutoff):
    """超过 cutoff 返回 cutoff+1, 提前终止不做完整 DP"""
    if abs(len(a) - len(b)) > cutoff:
        return cutoff + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        best = i
        for j, cb in enumerate(b, 1):
            v = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb))
            cur.append(v)
            if v < best:
                best = v
        if best > cutoff:          # 当前行最小值已超限, 后面只增不减
            return cutoff + 1
        prev = cur
    return prev[-1]

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE dict (w TEXT PRIMARY KEY)")
random.seed(7)
words = set()
while len(words) < 3000:
    words.add("".join(random.choice("abcdefgh") for _ in range(random.randint(4, 8))))
c.executemany("INSERT INTO dict VALUES(?)", [(w,) for w in sorted(words)])
all_words = [r[0] for r in c.execute("SELECT w FROM dict")]

def search(q, cutoff=2, top=3, prune=True):
    computations = [0]
    scored = []
    for w in all_words:
        if prune and abs(len(w) - len(q)) > cutoff:
            continue
        computations[0] += 1
        d = edit_distance_bounded(q, w, cutoff)
        if d <= cutoff:
            scored.append((d, w))
    scored.sort()
    return scored[:top], computations[0]

queries = ["abcedf", "hgfedcb", "abcabcx", "ddccaa", "ghefab"]
full_total = prune_total = 0
for q in queries:
    top_full, n_full = search(q, prune=False)
    top_prune, n_prune = search(q, prune=True)
    assert top_full == top_prune, "裁剪不得改变结果"
    full_total += n_full
    prune_total += n_prune
    print("%s -> %s" % (q, top_prune))
print("距离计算次数: 全量 %d 次, 长度带裁剪后 %d 次 (省 %.0f%%), 结果完全一致"
      % (full_total, prune_total, (1 - prune_total / full_total) * 100))
