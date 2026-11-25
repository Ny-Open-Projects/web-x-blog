---
title: [NODE-099] 大促/高峰期的容量保障预案怎么做？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-099：大促/高峰期的容量保障预案怎么做？
**答**：
- 三阶段：**事前**（容量评估：历史峰值 × 增长系数 → 压测验证 → 扩容到位；预案分级：可降级接口清单、限流阈值预置）、**事中**（监控大盘：QPS/错误率/P99/下游水位；一键降级/扩容开关；值班响应 SLA）、**事后**（复盘：超预期点、预案有效性、改进项）。
- BFF 特有关注：**下游保护**——BFF 是流量入口，必须先于下游饱和时主动降级（非核心依赖熔断，NODE-052）；**缓存预热**——大促开始前把热点数据预载入多级缓存；**读服务优先**——大促流量 95% 是读，缓存命中率是生命线。
- 预案必须**演练**：季度性全链路压测 + 故障注入（拔 Redis、下游超时），验证降级真的能降。

```yaml
# 预案配置示例：降级矩阵与限流分级（配置中心热更新，NODE-089）
emergency:
  level_1:                # 流量超预期 50%
    actions:
      - disable: [recommend-feed, hot-search]      # 非核心接口直接关
      - cache_ttl: { home_page: 300 }              # 缓存 TTL 拉长
  level_2:                # 流量超预期 100%
    actions:
      - rate_limit: { uid_qps: 2, global_qps: 50000 }
      - degrade: [comment-submit, profile-edit]    # 写接口降级只读
      - static_fallback: true                      # 部分页面回退 CDN 缓存旧版
  level_3:                # 核心依赖不可用
    actions:
      - serve_stale: 3600                          # 允许返回 1h 内旧缓存
      - read_only_mode: true
      - alert: ops-oncall
```

```javascript
// 一键预案执行器：读取配置中心预案并生效
class EmergencyExecutor {
  constructor(configClient) { this.config = configClient; }

  apply(level) {
    const plan = this.config.get(`emergency.level_${level}`);
    if (!plan) return;
    log.warn({ event: 'emergency_applied', level, actions: plan.actions });

    for (const action of plan.actions) {
      if (action.disable) action.disable.forEach((k) => killSwitch.disable(k));
      if (action.rate_limit) rateLimiter.override(action.rate_limit);       // 临时收紧限流
      if (action.degrade) action.degrade.forEach((k) => degradeRegistry.enable(k));
      if (action.serve_stale) cachePolicy.allowStale(action.serve_stale);   // 允许旧缓存
    }
  }
}

// 缓存预热：大促前 30 分钟执行
async function warmUp() {
  const hotItems = await db.query(
    'SELECT id FROM items ORDER BY sales_7d DESC LIMIT 10000');   // 热销 top1w
  const limit = pLimit(50);
  await Promise.all(hotItems.map((it) => limit(async () => {
    const data = await fetchProduct(it.id);
    await redis.setex(`product:${it.id}:zh:${APP_VER}`, 3600, JSON.stringify(data));
  })));
  log.info({ event: 'cache_warmed', count: hotItems.length });
}
```
