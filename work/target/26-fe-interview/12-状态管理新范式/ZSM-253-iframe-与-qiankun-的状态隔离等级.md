---
title: [ZSM-253] iframe 和 qiankun 的状态隔离等级差在哪
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-253：iframe 和 qiankun 的状态隔离等级差在哪

**答**：
- iframe 是硬隔离：独立 window/document/storage/JS realm，状态天然不串，localStorage 同源共享但 sessionStorage/内存态全隔离；代价是通信只能 postMessage、路由不同步
- qiankun 类是软隔离：共享 window 与 localStorage（同源），JS 沙箱（Proxy 伪造 window）只隔离全局变量写入，状态隔离要靠架构约定
- 状态层面的选择：强一致要求少 + 深度隔离（第三方嵌入、遗留系统）用 iframe；高交互频率子应用用 qiankun + 严格状态协议
- 混合现实：sessionStorage 与内存态的隔离差异是 bug 高发区——跨应用数据一律走显式通信协议，不依赖存储共享

```javascript
// iframe 通信协议（硬隔离下唯一通路）
window.addEventListener('message', (e) => {
  if (e.origin !== allowedOrigin) return        // 安装边界
  const { type, payload } = e.data              // DTO 协议
})
parent.postMessage({ type: 'ready', payload: { user } }, targetOrigin)
```
