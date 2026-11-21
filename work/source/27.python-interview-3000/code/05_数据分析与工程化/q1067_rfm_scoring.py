
def quintile_score(values, reverse=False):
    order = sorted(range(len(values)), key=lambda i: values[i])
    n = len(values)
    scores = [0] * n
    for rank, idx in enumerate(order):
        s = min(5, rank * 5 // n + 1)
        scores[idx] = 6 - s if reverse else s   # reverse 用于 R 这类越小越好的指标
    return scores

users = ["u1", "u2", "u3", "u4", "u5"]
recency = [5, 40, 100, 12, 60]     # 天,越小越好
frequency = [20, 3, 1, 8, 2]
monetary = [5000, 800, 200, 1500, 600]
r = quintile_score(recency, reverse=True)
f = quintile_score(frequency)
m = quintile_score(monetary)
SEGMENTS = {
    (True, True): "重要价值", (True, False): "重要发展",
    (False, True): "重要挽留", (False, False): "一般流失",
}
for u, rs, fs, ms in zip(users, r, f, m):
    print(u, "R", rs, "F", fs, "M", ms, "->", SEGMENTS[(rs >= 3 and fs >= 3), rs >= 3])
