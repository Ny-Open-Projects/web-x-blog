"""A/B 对比:用户稳定分桶 + bootstrap 置信区间 + 护栏指标联合决策。"""
import hashlib, random, statistics


def assign(user_id, seed="exp-1"):
    # hash() 对字符串加盐,跨进程/重启会漂移;必须用稳定摘要保证用户级稳定归属
    digest = hashlib.sha256(f"{seed}:{user_id}".encode("utf-8")).digest()
    return "A" if (digest[0] % 2 == 0) else "B"


def bootstrap_diff(a, b, iters=2000, seed=7):
    rng = random.Random(seed)
    diffs = []
    for _ in range(iters):
        sa = [a[rng.randrange(len(a))] for _ in a]
        sb = [b[rng.randrange(len(b))] for _ in b]
        diffs.append(statistics.mean(sb) - statistics.mean(sa))
    diffs.sort()
    lo, hi = diffs[int(iters * 0.025)], diffs[int(iters * 0.975)]
    return lo, hi


if __name__ == "__main__":
    random.seed(11)
    users = [f"u{i}" for i in range(600)]
    groups = {u: assign(u) for u in users}
    # 真实差异 +0.03,B 更好
    scores = {u: 0.70 + (0.03 if groups[u] == "B" else 0) + random.gauss(0, 0.15)
              for u in users}
    a = [scores[u] for u in users if groups[u] == "A"]
    b = [scores[u] for u in users if groups[u] == "B"]
    lo, hi = bootstrap_diff(a, b)
    print(f"A 均值 {statistics.mean(a):.3f}  B 均值 {statistics.mean(b):.3f}")
    print(f"差值 95% CI = [{lo:+.3f}, {hi:+.3f}]")
    sig = lo > 0
    print("统计显著(置信区间不含 0):", sig)

    guardrails = {"p95_latency_ms": (420, 400), "cost_per_req": (0.021, 0.020)}
    ok_guard = all(new <= old for old, new in guardrails.values())
    decision = "上线 B" if sig and ok_guard else "继续观察或回滚"
    print("护栏:", guardrails, "->", decision)
    assert isinstance(sig, bool) and lo < hi, "置信区间顺序合理"
