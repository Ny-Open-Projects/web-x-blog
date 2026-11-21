"""复制延迟的观测: 自报有水分, 事件时间差更真, 持续超限才告警"""
import random

random.seed(11)
n = 60
self_report = []
true_lag = []
for i in range(n):
    spike = 5.0 if 20 <= i < 23 else 0.0          # 第 20-22 个采样点一次 5 秒延迟尖峰
    true_lag.append(0.1 + spike + random.uniform(0, 0.4))
    self_report.append(0.0 if spike == 0 else 3.0)  # 自报滞后且口径保守

def percentile(data, p):
    s = sorted(data)
    k = max(0, min(len(s) - 1, int(round(p / 100.0 * (len(s) - 1)))))
    return s[k]

print("自报最大 %.1fs | 实测最大 %.1fs | 实测 P99 %.1fs (自报系统性低估)"
      % (max(self_report), max(true_lag), percentile(true_lag, 99)))

def sustained_alert(series, threshold, sustain):
    run = 0
    for v in series:
        run = run + 1 if v > threshold else 0
        if run >= sustain:
            return True
    return False

calm = [0.1 + random.uniform(0, 0.4) for _ in range(n)]
calm[10] = 2.5                                       # 平稳日一个孤立毛刺
print("平稳日孤立毛刺: 单点即告 %s, 连续 3 点才告 %s (后者不会狼来了)"
      % (sustained_alert(calm, 2.0, 1), sustained_alert(calm, 2.0, 3)))
print("真实尖峰事件: 连续 3 点告警 %s (真延迟精确命中)" % sustained_alert(true_lag, 2.0, 3))
