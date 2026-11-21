"""综合演练: 从 SLO 推导容量、实例数与限流(纯标准库)。"""
import math

SLO_P95_MS = 300
PEAK_RPS = 200
RT_MS = 80                                     # 实测单请求平均处理时长
WORKER_CONC = 20                               # 实测单实例有效并发

INSTANCE_RPS_CAP = WORKER_CONC * 1000.0 / RT_MS
NEEDED_CONC = PEAK_RPS * RT_MS / 1000.0        # Little 定律
INSTANCES = math.ceil(PEAK_RPS / INSTANCE_RPS_CAP) + 1   # N+1 冗余
LIMIT_RATE = int(PEAK_RPS * 1.5)               # 入口限流留 50% 余量

print("SLO P95 {}ms, 峰值 {} rps, 单请求 {}ms".format(SLO_P95_MS, PEAK_RPS, RT_MS))
print("Little 定律: 需要同时在处理 {:.0f} 个请求".format(NEEDED_CONC))
print("单实例上限 {:.0f} rps -> 需要 {} 实例 (N+1)".format(INSTANCE_RPS_CAP, INSTANCES))
print("入口限流设 {} rps, 超压部分交给队列与 429".format(LIMIT_RATE))
headroom = INSTANCE_RPS_CAP * INSTANCES / PEAK_RPS
single_survive = NEEDED_CONC <= WORKER_CONC * (INSTANCES - 1)
verdict = "go" if headroom >= 1.2 and single_survive else "no-go"
print("容量水位 {:.2f}x, 单实例故障可扛: {} -> 发布判定 {}".format(
    headroom, single_survive, verdict))
assert verdict == "go" and INSTANCES == 2
print("要点: SLO 定预算, Little 定并发, 实测定单机上限, N+1 定实例数, 限流把超压挡在门外; 输入变了结论要重跑")
