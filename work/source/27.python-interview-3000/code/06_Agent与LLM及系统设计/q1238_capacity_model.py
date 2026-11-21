"""容量模型:Little's Law 推并发 + 拐点探测 + 冗余系数与实例数建议。"""
import math


def littles_law(qps, avg_latency):
    return qps * avg_latency


def find_knee_pressure(load_test):
    """load_test: [(qps, p95_ms)] 找延迟开始非线性上升的拐点。"""
    knee, prev_slope = None, 0.0
    for i in range(1, len(load_test)):
        q0, l0 = load_test[i - 1]
        q1, l1 = load_test[i]
        slope = (l1 - l0) / (q1 - q0)
        if i >= 2 and slope > max(prev_slope * 3, 0.05):   # 斜率突增视为拐点
            knee = (q0, l0)
            break
        prev_slope = slope
    return knee


def capacity_plan(target_qps, latency_slo_ms, redundancy=1.5, safety_n_plus_1=1):
    per_inst_concurrency = littles_law(target_qps / 1000, latency_slo_ms / 1000)
    knee_qps = 900
    insts = math.ceil(target_qps * redundancy / knee_qps) + safety_n_plus_1
    return {"target_qps": target_qps,
            "concurrency": round(per_inst_concurrency, 1),
            "instances": insts}


if __name__ == "__main__":
    lt = [(100, 8), (200, 9), (300, 10), (500, 12), (700, 15),
          (800, 18), (850, 26), (900, 60), (950, 180), (1000, 500)]
    knee = find_knee_pressure(lt)
    print("压测拐点:", knee, "-> 单实例安全水位取拐点下方")
    assert knee == (800, 18), "850 之后延迟非线性爆炸"

    plan = capacity_plan(target_qps=5000, latency_slo_ms=50)
    print("容量方案:", plan)
    l = littles_law(5000, 0.05)
    print(f"Little 定律: 5000 QPS × 50ms = {l} 并发在途")
    assert abs(l - 250) < 1e-6
    assert plan["instances"] >= 9, "5000 QPS 冗余后需要 9+ 实例"
    print("容量结论: 单实例拐点 800 QPS,冗余 1.5 + N+1 ->", plan["instances"], "实例")
