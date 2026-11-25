---
title: [MFW-692] Service Worker 缓存与 Data Cache 的冲突协调
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-692：SW 缓存与 Data Cache 协调

**答**:
- 缓存的冲突面：SW 的预缓存（RBL-707）与 Next 的 Data Cache（服务端）是两层不同缓存——冲突场景：1) **SW 缓存的 RSC payload 过期**（SW 缓存 payload → Data Cache 已更新——client 拿旧 payload（SW 屏蔽新数据 RBL-581 的 SW 版）；2) **SW 缓存策略与 Server 渲染模式冲突**（页面 ISR 60s + SW cacheFirst = SW 永不更新（cacheFirst 吞掉所有请求））。
- 协调原则：1) **HTML/payload 走 network-first**（永远拿最新——SW 不缓存可变内容 RBL-618）；2) **静态资产走 cacheFirst**（hash 文件名——immutable 安全）；3) SW 的缓存边界（SW 缓存「不可变产物」、Data Cache 管「可变数据」——角色分离）；「SW 的 cacheFirst × 动态内容」= 反模式。
- SW 版本与构建版本的同步：SW 更新（RBL-708 清单 diff）——Data Cache 的失效不触发 SW 更新（两层独立失效——「SW 层的失效」= SW 自身更新周期）；「SW 的失效延迟」= 用户看到新内容的额外延迟（SW 更新 + 重新加载——SW 的 TTL 语义）。
- 追问钩子：为什么「SW 缓存 RSC payload」是反模式？——payload 含个性化数据（cookie/session——用户相关）；SW 缓存 = 跨用户/跨会话复用（数据泄漏——用户 A 的 payload 被用户 B 拿到）；且 payload 过期 = 静默旧数据（Data Cache 已更新但 SW 缓存屏蔽）；「SW 缓存的角色」：immutable 产物（hash 资产）是安全的——可变内容（HTML/payload/API）必须 network-first——SW 的缓存边界 = 可变性判断（RBL-618 的 SW 层）。

```typescript
// SW 的缓存策略分层
const CACHE_STRATEGIES = [
  { match: /\.(js|css|woff2)$/, strategy: 'cacheFirst', maxAge: 31536000 },     // immutable
  { match: /\/_next\/data\/.*\.json$/, strategy: 'networkFirst' },             // payload：network first
  { match: /\/api\//, strategy: 'networkOnly' },                               // API：不缓存
  { match: /\.html$|^\/$/, strategy: 'networkFirst' },                          // HTML：network first
];
// SW 缓存的可变性判断
function isImmutable(url) {
  return /[\w]-[a-f0-9]{8,}\.\w+$/.test(url);            // hash 文件名 = 内容寻址 = immutable
}
// SW 更新与 Data Cache 失效的独立性
// revalidateTag('products') → Data Cache 失效
// SW 的 payload 缓存需要 SW 自身更新才刷新——两层不同步是延迟源
// 解法：payload 不进 SW 缓存（networkFirst）→ SW 只缓存 immutable → 无冲突
```
