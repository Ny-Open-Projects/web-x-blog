---
title: [MFW-526] RSC 数据缓存策略：fetch 选项全景与组合语义
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-526：RSC 数据缓存策略：fetch 选项全景

**答**:
- fetch 选项矩阵：1) `cache: 'force-cache'`（永久缓存直到 revalidate）/`'no-store'`（每请求实时）；2) `next.revalidate: N`（时间窗 TTL）；3) `next.tags`（标签失效键）；组合语义：force-cache + revalidate=60 = ISR 数据层；no-store + tags = 无效组合（no-store 无缓存可失效——静默忽略 tags 是陷阱）；4) POST 默认不缓存（fetch 语义继承）。
- 语义陷阱清单：cache:'no-store' 仍参与 Request Memoization（同请求去重保留）；revalidate 窗口内多请求共享缓存（不是每请求重取）；force-cache 的「永久」受 Full Route 层约束（路由动态化则数据层缓存仍有效但路由不静态化）。
- 策略的选择流程图：数据敏感度（价格→精确失效/标签）→ 变更频率（TTL）→ 个性化（no-store/请求级）→ 规模（tag 化管理）。
- 追问钩子：为什么「no-store 时 tags 静默失效」是设计缺陷而非文档问题？——组合语义的无效组合应「构建期报错」而非运行时静默——配置的语义校验（RBL-575 语义层校验的框架版）：无效组合 = 开发者意图矛盾（既不要缓存又要失效它）——元框架的配置体验差距就在这些「静默忽略」的陷阱清单。

```javascript
// fetch 选项矩阵与组合语义
// 1) ISR 数据层
fetch(url, { next: { revalidate: 60, tags: ['products'] } });
// 2) 实时数据（动态化整路由）
fetch(url, { cache: 'no-store' });                      // tags 静默无效！
// 3) 请求级去重（不落盘）
const u = await getUser(id);                            // 同请求内二次调用共享
// 组合陷阱自检
function auditFetchOptions(opts) {
  if (opts.cache === 'no-store' && opts.next?.tags)
    warn('no-store 下 tags 无效——改为 revalidate: 0 + tags 或接受缓存');
  if (opts.next?.revalidate != null && opts.cache === 'no-store')
    warn('no-store 覆盖 revalidate');
}
```
