"""漏斗窗口宽度的扫描: 窗口越宽转化越高, 但口径也随之漂移"""
from datetime import datetime, timedelta

STEPS = ["曝光", "点击", "加购", "支付"]
BASE = datetime(2026, 3, 1, 10, 0)


def make_events(n_users):
    """确定性生成: 部分用户缺步, 部分用户间隔极长"""
    events = []
    for i in range(n_users):
        u = f"u{i:02d}"
        t0 = BASE + timedelta(minutes=i * 3)
        events.append((u, "曝光", t0))
        events.append((u, "点击", t0 + timedelta(minutes=1 + (i * 7) % 90)))
        if i % 7 != 3:
            events.append((u, "加购", t0 + timedelta(minutes=5 + (i * 37) % 4000)))
        if i % 9 != 0:
            events.append((u, "支付", t0 + timedelta(minutes=5 + (i * 91) % 9000)))
    return events


def funnel_by_span(events, span_minutes):
    """有序匹配四步, 仅约束曝光到支付的总跨度"""
    idx = {}
    for u, s, ts in events:
        idx.setdefault(u, {}).setdefault(s, []).append(ts)
    n_pay = 0
    for u, per in idx.items():
        cur, ok = None, True
        for s in STEPS:
            cands = sorted(ts for ts in per.get(s, []) if cur is None or ts >= cur)
            if not cands:
                ok = False
                break
            cur = cands[0]
        if ok and (cur - per["曝光"][0]) <= timedelta(minutes=span_minutes):
            n_pay += 1
    return n_pay, len(idx)


if __name__ == "__main__":
    events = make_events(40)
    spans = [("30 分钟", 30), ("6 小时", 360), ("24 小时", 1440),
             ("72 小时", 4320), ("7 天", 10080)]
    prev = None
    rates = []
    for name, w in spans:
        pay, total = funnel_by_span(events, w)
        rate = pay / total
        rates.append(rate)
        print(f"总窗口 {name:>7}: 支付 {pay:2d}/{total}, 转化率 {rate:.1%}")
        if prev is not None:
            assert rate >= prev, "窗口放宽后转化率不应下降"
        prev = rate
    assert rates[-1] - rates[0] > 0.1, "窗口从 30 分钟放到 7 天应有明显口径漂移"
    # 分步独立时限口径, 等价于每步窗口的组合约束
    print(f"口径提醒: 同一批数据, 30 分钟窗转化 {rates[0]:.1%}, 7 天窗 {rates[-1]:.1%}, 相差 {rates[-1] - rates[0]:.0%}")
    print("要点: 窗口宽度是口径的一部分, 跨报表比较必须先确认窗口一致, 否则差异只是口径漂移")
