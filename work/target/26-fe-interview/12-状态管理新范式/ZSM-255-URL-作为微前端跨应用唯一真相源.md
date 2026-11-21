---
title: [ZSM-255] 为什么说 URL 是微前端跨应用的唯一可靠真相源
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-255：为什么说 URL 是微前端跨应用的唯一可靠真相源

**答**:
- 生命周期错配：子应用频繁挂载卸载，内存态随卸载丢失；URL 在卸载后依然存在且新挂载应用能立即读到
- 可恢复性：刷新/新标签页/分享链接，URL 都能还原上下文；内存共享做不到
- 实践：跨应用跳转携带业务上下文（订单 id、租户 id、tab）进 query/search；应用挂载时从 URL 初始化自己的内存态
- 配套：主应用统一路由分发（single-spa routing events / qiankun 的 router 模式），子应用只改自己前缀下的路径，防止路由互踩

```javascript
// 子应用挂载时以 URL 为准初始化
export async function mount() {
  const orderId = new URLSearchParams(location.search).get('orderId')
  useOrderStore.setState({ orderId })   // URL → 内存态（单向，不反向写全局）
}
```
