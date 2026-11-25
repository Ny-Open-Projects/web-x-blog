---
title: [NODE-776] 笔试题——实现灰度标记路由到实例（服务发现过滤）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-776：手写灰度路由

**需求与边界**：
- 需求：服务端灰度路由（SCN-NODE-668）——① 实例版本元数据（deployment 标注 version——service discovery meta）；② 按标记路由到对应版本实例（stable/canary——SCN-OPS-233 分层）；③ canary 实例不足时兜底（stable 接收——可用性优先）；④ 路由结果 header 传递（SCN-OPS-216 全链贯穿）。
- 边界：① 分流哈希稳定（SCN-ENG-296 分流器复用）；② 灰度比例可调（配置中心热更——SCN-NODE-663）；③ 实例摘流联动（canary 实例不健康 → 回 stable——SCN-NODE-706）。

**答**：
```javascript
function grayRoute(req, instances) {
  const bucket = req.headers['x-gray-bucket'] ?? computeBucket(req.user);   // 网关标记 or 计算（SCN-OPS-216）
  const canary = instances.filter(i => i.meta.version === 'canary' && i.healthy);
  const stable = instances.filter(i => i.meta.version === 'stable' && i.healthy);
  const target = grayRules.hit(bucket) && canary.length ? canary     // canary 优先
    : (canary.length ? stable : instances.filter(i => i.healthy));   // canary 不足兜底 stable
  res.setHeader('X-Served-Version', target.meta.version);   // 路由结果传递（全链）
  return target;
}
// 比例热更（SCN-NODE-663）
configCenter.on('gray', (r) => { grayRules.update(r); });   // 灰度比例热更
```

**评分点**:
- 实例版本元数据 + 过滤路由（deployment meta——SCN-NODE-668）。
- canary 不足兜底 stable（可用性优先——SCN-OPS-233）。
- 路由结果 header 传递（全链标记——SCN-OPS-216）。
- 灰度比例热更 + 哈希稳定（SCN-NODE-663/ENG-296）。
