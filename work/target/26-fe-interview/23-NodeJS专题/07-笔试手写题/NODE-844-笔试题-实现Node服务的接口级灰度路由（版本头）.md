---
title: [NODE-844] 笔试题——实现接口级灰度路由（接口版本 + 用户分组）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-844：手写接口灰度

**需求与边界**：
- 需求：接口级灰度（SCN-NODE-668/694）——① 接口级版本路由（部分接口走新版本——per 接口配置，SCN-OPS-254 分片语义）；② 用户分组路由（稳定哈希——SCN-ENG-296）；③ 版本兼容（新接口数据旧接口消费——SCN-OPS-205）；④ 接口级回滚（单接口回滚——不影响其他，SCN-OPS-254 分片）。
- 边界：① 接口级灰度的配置（路由表声明——SCN-NODE-843 配置中心）；② 接口间依赖（A 接口新版本依赖 B 新版本——依赖声明，SCN-NODE-740 DAG）；③ 灰度完成后的收敛（SCN-OPS-224）。

**答**：
```javascript
// 接口级灰度路由表（配置中心——SCN-NODE-843）
const apiGray = {
  '/order/v2/create': { pct: 10, stable: createV1, canary: createV2 },
  '/order/v2/detail': { pct: 10, stable: detailV1, canary: detailV2,
    depends: ['/order/v2/create'] },                   // 依赖声明（SCN-NODE-740 DAG）
};
function routeGray(req) {
  const cfg = apiGray[req.route.path];
  if (!cfg) return stableHandler(req);                 // 无灰度配置走 stable
  const hit = graySplit(req.user, { layer: `api:${req.route.path}` });   // 稳定哈希（SCN-ENG-296）
  const depsReady = (cfg.depends ?? []).every(d => apiGray[d]?.canaryActive);
  if (!depsReady) return cfg.stable(req);              // 依赖未就绪 → stable（SCN-NODE-740 DAG 约束）
  return hit ? cfg.canary(req) : cfg.stable(req);
}
```

**评分点**:
- 接口级灰度路由表（per 接口配置——SCN-OPS-254 分片语义）。
- 依赖声明约束（DAG——SCN-NODE-740）。
- 稳定哈希分流（SCN-ENG-296）。
- 接口级回滚（单接口——不影响其他——SCN-OPS-254）。
