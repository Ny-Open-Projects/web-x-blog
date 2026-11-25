---
title: [MFW-525] 软导航的 payload diff：段级传输与布局复用
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-525：软导航的 payload diff：段级传输优化

**答**:
- 软导航（客户端导航）的传输优化：payload 按段传输——目标路由与当前路由共享的 layout 段不重传（客户端已有）；「diff 的粒度 = 段」：只有变化的段（新页面的叶子段 + 变更的 layout）走网络。
- diff 的实现：Router 对比两棵段树（当前段树 vs 目标段树）——共同前缀段复用（App Router 的 layout 嵌套结构天然提供公共前缀）；请求参数（仅请求缺失段的 RSC payload）。
- 与预取的配合：prefetch 拉取「目标路由的完整段树」或「只到叶子段的 diff」（Next 优化：共享 layout 的段复用客户端已有）——预取流量的节省。
- 回退场景：段树结构变化（layout 重构）→ diff 退化全量——「公共前缀越长 diff 收益越大」的架构含义（layout 设计影响传输量）。
- 追问钩子：为什么「layout 深度设计」直接影响软导航流量？——共享 layout 是 diff 的公共前缀：所有页面共享根 layout（navbar 等不重传）；若每个页面自带完整布局（不用共享 layout）→ diff 无公共前缀 → 每次导航全量传；「传输优化不由构建器优化，由树结构决定」——组件树的形态是传输协议的语义来源（Flight 段树 = diff 单元）。

```javascript
// 段树 diff 概念
function diffSegments(current, target) {
  // 段树：{ segment, payload, children }
  const shared = []; let i = 0;
  while (i < current.length && i < target.length && current[i].segment === target[i].segment) {
    shared.push(current[i]); i++;                        // 公共前缀复用
  }
  return { reuse: shared.map(s => s.segment),            // 不重传
           fetch: target.slice(i).map(s => s.segment) }; // 需要拉取
}
// /shop 和 /shop/123 共享 [root, shop] 前缀
// 导航只 fetch [123] 段 payload → 传输量 = 叶子段
// prefetch 也走 diff：只预取叶子段
<Link href="/shop/123" prefetch>   // 预取 [123] 段而非全树
```
