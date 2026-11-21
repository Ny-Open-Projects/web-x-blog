---
title: [MFW-376→MFW-376] SSE 通知 → router.refresh 的增量刷新组合
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→376：SSE→refresh 组合

**答**:
- 轻实时范式：SSE 只推「失效信号」（{ domain, id }——不推数据本体）→ 客户端按数据分级执行（展示数据 router.refresh() 让 RSC 重算；高频数据走 WS 直更缓存 MFW-251）——服务端渲染模型不被长连接破坏
- 合并与节流：3s 窗口同域事件合并为一次 refresh（编辑风暴不抖整树）；页面不可见时（visibilitychange hidden）只记账不刷新——回前台一次补拉
- 断线与补漏：SSE 断连期间的事件丢失 → 重连握手带 lastEventId → 服务端补发窗口内摘要（或直接强制一次 refresh——简单正确优先）
- 生命周期：SSE 随路由建立销毁 + 多路复用（同页多域共用一条流按 domain 分发——MFW-351 复用）

```javascript
es.onmessage = (e) => {
  const { domain, id } = JSON.parse(e.data)
  throttleByDomain(domain, 3000, () => {
    document.visible ? matchDomain(domain, id) === 'rsc' ? router.refresh()
                     : qc.invalidateQueries({ queryKey: [domain, id] })
                     : markPending(domain, id)         // 后台记账回前台补
  })
}
// 重连：Last-Event-ID → 服务端补摘要或 forceRefresh
```
