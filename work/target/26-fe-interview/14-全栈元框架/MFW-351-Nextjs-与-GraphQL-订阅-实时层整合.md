---
title: [MFW-351] 元框架与 GraphQL 订阅实时层整合
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-351：GraphQL 订阅实时层整合

**答**:
- 形态判定：订阅走独立 GraphQL WS 端点（Next 不承载——MFW-251 同约束），RSC 页面用「订阅桥接组件」（client 包 useSubscription → setQueryData/局部 state）——订阅是数据通道不是渲染通道
- 与 RSC 失效协同：订阅事件含 domain/id → 客户端既更新本地缓存又可触发 router.refresh（按数据分级：展示型直更、权限相关走服务端重验）
- 规模守则：订阅按页面生命周期建立销毁（路由卸载必 unsubscribe——泄漏即连接数爆炸）；订阅合并（同页多订阅共用一条 WS 多路复用）
- 降级：WS 不可用回退 Action 轮询（频率降级链）——实时层也要有降级矩阵

```javascript
'use client'
useEffect(() => {
  const unsub = gqlSub(ORDER_SUB, { id }, (data) => {
    qc.setQueryData(['order', id], merge)               // 汇入统一缓存
    if (data.needsAuthz) router.refresh()               // 权限敏感走服务端重验
  })
  return unsub                                          // 路由卸载必退订
}, [id])
```
