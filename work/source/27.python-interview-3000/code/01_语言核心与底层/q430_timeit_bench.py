import timeit

code_a = "sum(range(1000))"
code_b = "sum([i for i in range(1000)])"     # 多一层 list 构建与临时 list

NUMBER = 2_000    # 演示规模缩小保证秒级跑完;真实基准建议调到单次 repeat > 0.2s
REPEAT = 5

def bench(stmt):
    t = timeit.Timer(stmt, globals={"sum": sum, "range": range})
    runs = t.repeat(REPEAT, NUMBER)
    ns = [r / NUMBER * 1e9 for r in runs]    # 统一换算成单次耗时 ns
    return min(ns), ns                        # 汇报取 min 而非均值

best_a, runs_a = bench(code_a)
best_b, runs_b = bench(code_b)
print(f"sum(range)      {best_a:8.0f} ns/op  all runs: {[round(r) for r in runs_a]}")
print(f"sum(listcomp)   {best_b:8.0f} ns/op  all runs: {[round(r) for r in runs_b]}")
print("ratio:", round(best_b / best_a, 2))
print("timeit 默认禁用 GC:", "gc 在 Timer 内部被关闭,避免回收打点污染")
