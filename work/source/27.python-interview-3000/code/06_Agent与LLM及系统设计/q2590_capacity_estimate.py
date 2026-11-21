"""Q2590 供应商降级的容量预估:降配后到底还接得住多少量。

主供应商挂掉切备用前,先算清备用容量扛不扛得住当前负载:
离散时间排队模拟,每秒到达减服务,积压线性增长,得出峰值积压
与最大等待,再按安全系数算出降级期接入上限。
"""


def simulate(arrival_rate, service_rate, seconds):
    """离散时间排队:每秒到达 arrival_rate 个,服务 service_rate 个。"""
    backlog = 0.0
    peak = 0.0
    max_wait = 0.0
    for _ in range(int(seconds)):
        backlog += arrival_rate
        served = min(backlog, service_rate)
        backlog -= served
        peak = max(peak, backlog)
        max_wait = max(max_wait, backlog / max(service_rate, 1e-9))
    return {"peak_backlog": round(peak, 1), "max_wait_s": round(max_wait, 1)}


def main():
    load = 60.0
    primary = simulate(load, 100.0, 60)
    degraded = simulate(load, 40.0, 60)
    assert primary == {"peak_backlog": 0.0, "max_wait_s": 0.0}, primary
    assert degraded["peak_backlog"] == 1200.0, degraded
    assert degraded["max_wait_s"] == 30.0
    safe = round(40.0 * 0.7 * 0.9, 1)  # 七折再留一成余量
    assert safe == 25.2 and safe < load
    print("主供 100rps 扛 60rps:", primary)
    print("降级 40rps 扛 60rps:", degraded, "← 必须同步限流")
    print("降级期安全接入上限约", safe, "rps,超出部分要排队或拒绝")


if __name__ == "__main__":
    main()
