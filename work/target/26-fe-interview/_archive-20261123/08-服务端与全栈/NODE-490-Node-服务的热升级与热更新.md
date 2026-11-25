---
title: [NODE-490] Node 服务的热更新（不停服变更）边界与实现如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-490：热更新边界与实现
**答**:
- 边界判定：什么值得热更——配置/开关/规则/文案（变更频繁、不涉代码逻辑）用配置中心热更（NODE-388）；代码级变更走发布（优雅滚动重启已足够快，代码热替换的风险远大于收益——默认不做代码热更）。
- 热更实现（配置类）：快照原子切换 + 订阅回调（NODE-388）——缓存策略/限流参数/降级开关即时生效；状态ful 组件重建（连接池参数变更 → 优雅重建：新建池 → 迁移 → 废弃旧池）。
- 类热更场景的替代：插件/规则热加载（规则引擎规则从 DB/配置拉取执行 ARC-452——"逻辑热更"用数据驱动实现而非代码替换）、Worker 池内滚动替换（NODE-348：worker 按需重建加载新代码——隔离进程内热替换的风险）。
- 风险控制：热更项白名单（只有登记过的配置键可热更——防任意热更）、热更演练（NODE-470：每次热更进观测窗口）、热更与发布语义区分（热更不走发布单但要走变更单 NODE-478）。
- 验证：热更生效验证接口（运行时可查询当前生效配置快照版本——确认变更真的生效，防"改了没生效"排障）。
```javascript
// 热更白名单 + 生效验证
const hotKeys = new Set(['rateLimit', 'degrade', 'timeout', 'copy']);
configCenter.on('change', (k, v) => {
  if (!hotKeys.has(k)) return requireApproval(k);                // 非白名单走发布
  apply(k, v); log.info({ hotReload: k, version: v.v });         // 进观测
});
ops.get('/ops/config/effective', (ctx) => ctx.body = currentSnapshot()); // 生效快照可查
```
