"""开环与闭环压测模型: 谁能暴露排队雪崩(纯标准库)。"""


def simulate(arrival_per_step, service_per_step, steps=100, max_inflight=None):
    """每步到达 arrival 个、服务 service 个。
    max_inflight 为 None 表示开环, 到达不受积压影响; 设值表示闭环的并发上限。"""
    queue, peak, done = 0.0, 0.0, 0.0
    for _ in range(steps):
        queue += arrival_per_step
        if max_inflight is not None:
            queue = min(queue, max_inflight)        # 闭环: 用户数固定, 超出发不出来
        served = min(queue, service_per_step)
        queue -= served
        done += served
        peak = max(peak, queue)
    return peak, done


open_peak, open_done = simulate(0.8, 0.5)                      # 开环 8rps, 容量 5rps
closed_peak, closed_done = simulate(0.8, 0.5, max_inflight=10)  # 闭环 10 用户
print("开环: 队列峰值 {:.0f}, 完成 {} —— 积压随时间线性上涨".format(open_peak, open_done))
print("闭环: 队列峰值 {:.0f}, 完成 {} —— 用户被响应时间自然限速".format(closed_peak, closed_done))
assert open_peak > closed_peak
print("要点: 测容量上限用闭环爬坡, 测过载雪崩与超时预算必须开环; 报告要写清模型, 结论才可复现")
