"""压测中的思考时间建模: 并发数、响应时间与思考时间的关系(纯标准库)。"""


def closed_loop_rate(concurrency, rt_ms, think_ms):
    """闭环模型: 每个虚拟用户的周期 = 响应 + 思考。"""
    cycle = rt_ms + think_ms
    return concurrency * 1000.0 / cycle, cycle


def needed_concurrency(target_rps, rt_ms, think_ms):
    """从目标吞吐反推虚拟用户数: Little 定律含思考时间。"""
    return target_rps * (rt_ms + think_ms) / 1000.0


for rt, think in [(200, 0), (200, 3000)]:
    rps, cycle = closed_loop_rate(50, rt, think)
    print("50 用户 RT={}ms 思考={}ms -> 周期 {:5d}ms 吞吐 {:6.1f} rps".format(
        rt, think, int(cycle), rps))
need = needed_concurrency(100, 200, 3000)
print("目标 100 rps RT=200ms 思考=3000ms -> 需要 {} 个虚拟用户".format(round(need)))
assert closed_loop_rate(50, 200, 3000)[0] < closed_loop_rate(50, 200, 0)[0]
print("要点: 吞吐 = 并发 / (RT + 思考); 无思考时间的压测高估压力、误导扩容, 应从访问日志拟合分布")
