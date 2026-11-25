---
title: [WCN-328] DSD 水合时「服务端状态 → 信号」的恢复协议？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-328：DSD 水合时「服务端状态 → 信号」的恢复协议？
**答**：
- 服务端把信号初值序列化进元素属性（data-state='base64(json)'）或全局注册表。
- 水合：注册时读取 data-state → 初始化信号 → 不重渲染（DOM 已是同状态产物）。
- 校验：恢复值与 DOM 渲染内容一致性（开发模式 diff 告警——防服务端/客户端渲染函数分叉）。
- 清理：恢复后移除 data-state（防泄漏到快照/监控）。

```javascript
connectedCallback() {
  const init = this.dataset.state && JSON.parse(atob(this.dataset.state));
  if (init) { restoreSignals(init); this._hydrated = true; }
  delete this.dataset.state;
}
r
```
