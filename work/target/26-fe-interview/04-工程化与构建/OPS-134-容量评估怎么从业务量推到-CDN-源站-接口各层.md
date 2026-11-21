---
title: [OPS-134] 容量评估怎么从业务量推到 CDN/源站/接口各层？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-134：容量评估怎么从业务量推到 CDN/源站/接口各层？
**答**：
- 推导链：业务预估（DAU×人均 PV）→ 峰值 PV/s（乘峰值系数）→ 每层按自己的资源/命中特征换算：CDN 看带宽 Gbps、源站看穿透 QPS（乘 1-命中率）、接口层看 QPS × 每 PV 调用数 × 重试系数。
- 每层留安全水位：目标利用率 ≤ 60%，为扩容时间窗与流量误差留余量。
- 输出三张表：带宽扩容申请、源站副本数（= 穿透 QPS / 单机压测容量 / 0.6）、下游依赖容量（DB/缓存/第三方配额）。
- 假设要显式列出（峰值系数、命中率、人均 PV），演练/大促后用真实数据回校准。
- 容量评估与 HPA 上限、限流阈值（OPS-104/119）互相校验，形成闭环。

```bash
# 容量评估：从业务量推各层峰值（大促示例）
# 输入假设：DAU=200 万，人均 PV=8，峰值系数=5，静态资源 1.5MB/PV，每 PV 3 个接口，重试系数 1.2
DAU=2000000; PV_PER_USER=8; PEAK=5; STATIC_MB=1.5; API_PER_PV=3; RETRY=1.2

TOTAL_PV=$((DAU * PV_PER_USER))
PEAK_PV=$((TOTAL_PV * PEAK / 86400))                 # 日内峰值 PV/s（粗估口径）
echo "峰值 PV/s: $PEAK_PV"

# CDN 层：峰值带宽 Gbps = 峰值 PV/s × 资源大小 MB × 8 / 1000
echo "CDN 峰值带宽 ≈ $(echo "$PEAK_PV * $STATIC_MB * 8 / 1000" | bc) Gbps"

# 源站层：CDN 命中率 95% → 穿透 = 峰值 × 5%，副本数 = 穿透QPS / 单机容量 / 0.6
PENETRATION=$((PEAK_PV * 5 / 100))
echo "源站需承载 PV/s ≈ $PENETRATION（按 95% 命中率）"

# 接口层：峰值 QPS = 峰值 PV/s × 每 PV 接口数 × 重试系数
echo "接口峰值 QPS ≈ $(echo "$PEAK_PV * $API_PER_PV * $RETRY" | bc | cut -d. -f1)"

# 输出三张表：CDN 带宽扩容申请 / 源站副本数 / 下游依赖（DB 缓存第三方配额）容量
# 大促后用真实数据回校准：峰值系数与命中率假设逐项复核
```
