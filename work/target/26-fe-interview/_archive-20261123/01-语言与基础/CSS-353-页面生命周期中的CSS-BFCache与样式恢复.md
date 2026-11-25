---
title: [CSS-353] 页面生命周期中的 CSS：bfcache 恢复与样式时序
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-353：页面生命周期中的 CSS：bfcache 恢复与样式时序

**答**：
- bfcache（往返缓存）：后退返回时整页快照直接恢复（不重新解析 CSS/执行 JS）——样式状态、滚动位置原样回来；unload 监听/某些 header 会禁用 bfcache
- pageshow 事件：e.persisted === true 表示来自 bfcache，此时要重连断开的资源（WebSocket 早已断）、刷新时效数据（token 可能过期）——但 DOM/CSS 状态不用重建
- 样式时序陷阱：FOUC 防护（关键 CSS 内联）与 bfcache 无冲突，但「首帧前 JS 改主题」在 bfcache 恢复时不会重跑——主题切换若只靠 JS 启动时设置，往返返回可能错主题（要用持久化 data-theme 而非内存变量）
- 与 SW 的组合：SW 控制页面的导航响应策略影响 bfcache 可用性（cache-first 返回的页面可能不进 bfcache）——核心页面导航要允许 bfcache（响应带正确缓存头）
- 验证方法：Chrome DevTools Back/Forward Cache 面板可测「页面能否被缓存」及阻塞原因清单

```javascript
addEventListener('pageshow', (e) => {
  if (e.persisted) {
    reconnectWebSocket();               // 长连接已死
    refreshThemeFromStorage();          // 主题对齐持久化值
    refreshCountdown();                 // 计时类重校准
  }
});
```
