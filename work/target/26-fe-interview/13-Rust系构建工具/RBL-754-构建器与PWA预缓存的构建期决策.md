---
title: [RBL-754] PWA 预缓存的构建期决策：哪些资源进预缓存、哪些走运行时缓存
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-754：PWA 预缓存的构建期决策：哪些资源进预缓存、哪些走运行时缓存

**答**:
- 预缓存（RBL-707）vs 运行时缓存的分工决策：预缓存 = 「本版本必需的首屏资源」（entry chunk + 关键 CSS + 核心字体，预算内贪心 RBL-625 思路）；运行时缓存 = 「按路由/用法动态到达的资源」（懒 chunk 的 CSS、图片、API 响应）——预缓存过多 = 每次更新下载量爆炸；过少 = 离线不可用。
- 构建期决策的输入：1) 资源角色（manifest 的 role/size）；2) **入口闭包预算**（首屏 chunk 链总字节 ≤ 预算，如 500KB）；3) RUM 数据回灌（上次版本哪些资源在会话中被高频使用——高频懒资源提升进预缓存候选）。构建器输出「预缓存清单 + 理由」让决策可审计。
- 版本切换成本约束：预缓存清单的变更量 = 用户更新下载量——清单稳定性优先（稳定资源优先入选，频繁变更的排除）；「更新下载量」作为预缓存策略的优化目标而非「预缓存命中率」。
- 运行时缓存策略的构建期生成：路由正则 → 缓存策略映射（页面 = networkFirst、静态资产 = cacheFirst + 过期、API = networkFirst + 短 TTL）——策略表由构建器按产物 URL 模式生成，运行时 SW 只消费。
- 追问钩子：为什么「预缓存首屏闭包」优于「预缓存全部产物」？——SW 更新语义是「新版本安装完成才激活」，全量预缓存的安装时间 = 全部产物下载时间（大应用 20MB+，弱网分钟级）；闭包预算让安装在秒级完成，未缓存的懒资源走运行时缓存（在线时）——安装速度是 SW 体验的关键指标。

```javascript
// 预缓存清单决策
function precachePlan(manifest, { budgetKB = 500, rumTop = [] } = {}) {
  const entryClosure = manifest.closureOf('entry');      // 首屏闭包（含级联 hash URL）
  const plan = []; let used = 0;
  const sorted = [...entryClosure].sort((a, b) => a.sizeKB - b.sizeKB);
  for (const f of sorted) {
    if (used + f.sizeKB > budgetKB) continue;            // 预算贪心
    plan.push(f); used += f.sizeKB;
  }
  // RUM 高频提升：会话使用率 > 0.5 的懒资源进候选（不挤占预算则纳入）
  const promoted = rumTop.filter(r => r.usage > 0.5 && used + r.sizeKB <= budgetKB);
  return { precache: [...plan, ...promoted], usedKB: used, reason: 'entry-closure + rum-promoted' };
}
// 运行时策略表（构建期生成）
const runtimeStrategy = [
  { match: /\/api\//, strategy: 'networkFirst', ttl: 60 },
  { match: /\.(js|css)$/, strategy: 'cacheFirst', maxAge: 30 * 86400 },
  { match: /\.(png|jpg|webp)$/, strategy: 'cacheFirst', maxEntries: 60 },
];
```
