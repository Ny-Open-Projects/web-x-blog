"""心跳分级判定与防抖: 连续两个采样才确认状态翻转"""

INTERVAL = 10       # 正常周期 10 分钟


def band(delay):
    """延迟分级: ok <=1x, warn 1-3x, dead >3x"""
    if delay <= INTERVAL:
        return "ok"
    return "warn" if delay <= INTERVAL * 3 else "dead"


SAMPLES = [5, 8, 20, 20, 40, 40, 35, 5, 5]


def observe(samples):
    events, confirmed, pending, count = [], "ok", None, 0
    for delay in samples:
        b = band(delay)
        if b == confirmed:
            pending, count = None, 0
            continue
        if b == pending:
            count += 1
        else:
            pending, count = b, 1
        if count >= 2:
            confirmed = b
            events.append(("进入降级" if b == "warn" else "进入断流") if b != "ok" else "恢复")
    return events


if __name__ == "__main__":
    events = observe(SAMPLES)
    print(f"采样序列 {SAMPLES} -> 状态事件 {events}")
    assert events == ["进入降级", "进入断流", "恢复"], "应只有三次状态确认"
    print("9 个采样只发 3 个事件: 单点毛刺不告警, 状态翻转需连续两拍确认, 恢复同样要确认")
    print("要点: 分级阈值按周期倍数定, 防抖消掉'一跳正常一跳异常'的抖动告警, 值班才不会麻")
