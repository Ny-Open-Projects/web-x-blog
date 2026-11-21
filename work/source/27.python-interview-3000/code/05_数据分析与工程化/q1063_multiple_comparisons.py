
ALPHA = 0.05
K = 20
family = 1 - (1 - ALPHA) ** K
print(f"{K} 个指标各按 {ALPHA} 检验,至少 1 个假阳性概率约 {family:.0%}")
print(f"Bonferroni 修正:每个指标用 alpha/{K} = {ALPHA / K:.4f}")
print("工程实践:主指标预注册,护栏只监控,固定样本量或序贯方案防 peeking")
