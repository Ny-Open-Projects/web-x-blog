"""Little 定律容量估算与水位(纯标准库)。"""


def capacity_plan(qps, latency_s, peak_factor=2.0, headroom=0.3):
    avg_conc = qps * latency_s                # Little 定律 L = λ W
    peak_conc = avg_conc * peak_factor
    provision = peak_conc * (1 + headroom)
    max_qps = provision / latency_s           # 反推可扛 QPS
    return {"avg_concurrency": round(avg_conc, 1), "peak": round(peak_conc, 1),
            "provision": round(provision, 1), "max_qps": round(max_qps)}


for name, qps, lat in (("读接口", 500, 0.05), ("导出接口", 20, 2.0), ("聚合接口", 2000, 0.08)):
    print(f"{name:6s}", capacity_plan(qps, lat))
print("扩容触发线:运行并发持续超过 provision 的 75%")
