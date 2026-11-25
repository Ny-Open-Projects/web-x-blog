---
title: [NODE-778] 笔试题——实现降级框架完整版（策略库 + 开关矩阵 + 观测）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-778：手写降级框架

**需求与边界**：
- 需求：统一降级框架（SCN-NODE-690）——① 策略库（cache/default/trim/static——组合声明）；② 开关矩阵（手动 L1-L4 + 自动熔断触发——SCN-OPS-329）；③ 降级标记（响应头 + body——SCN-NODE-690）；④ 降级率看板数据（按接口/原因聚合）。
- 边界：① 降级策略链（首选缓存 → 失败试默认 → 最终静态——策略级联）；② 手动降级的生效检查（开关变更后验证降级路径真的工作——SCN-OPS-861 演练）；③ 降级数据的可信标注（TTL/来源——前端展示依据）。

**答**：
```javascript
const strategies = {
  cache: async (key) => ({ data: await staleCache.get(key), ttl: staleTtl(key), source: 'cache' }),
  default: (d) => ({ data: d, source: 'default' }),
  static: (s) => ({ data: s, source: 'static' }),
};
function degradeMiddleware(routes) {
  return async (req, res, next) => {
    const level = degradeMatrix.current();             // SCN-OPS-329 开关矩阵
    const route = routes[req.route?.path];
    if (route?.levels?.includes(level)) {              // 该接口该档位降级
      let out = null;
      for (const s of route.strategyChain) {           // 策略级联（cache→default→static）
        try { out = await strategies[s](route.args); break; } catch { continue; }
      }
      res.setHeader('X-Degraded', `${level}:${route.strategyChain[0]}`);
      telemetry.push({ type: 'DEGRADED', path: req.route.path, level });
      return res.json({ ...out, degraded: true });     // 降级标记（SCN-NODE-690）
    }
    next();
  };
}
// 降级率看板数据（SCN-NODE-690）
telemetry.aggregate('DEGRADED', { by: ['path', 'level'] });
```

**评分点**:
- 策略级联（cache→default→static——链式降级）。
- 开关矩阵 + 熔断双触发（手动 L1-L4 + 自动——SCN-OPS-329）。
- 降级标记双通道（header + body——SCN-NODE-690）。
- 降级率聚合（按接口/原因——可观测）。
