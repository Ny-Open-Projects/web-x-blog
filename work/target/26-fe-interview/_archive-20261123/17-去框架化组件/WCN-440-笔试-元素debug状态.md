---
title: [WCN-440] 笔试：实现元素的开发态调试钩子（_debugState + 版本自述）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-440：笔试：实现元素的开发态调试钩子（_debugState + 版本自述）。
**题目**：`_debugState()` 返回内部状态（props/异步态/订阅数）；`el.dsInfo` 返回 tag/版本/注册时间；生产构建剔除（构建宏）。

```javascript
class GoodsCard extends HTMLElement {
  get dsInfo() {
    return { tag: 'goods-card', version: this.dataset.version,
      registeredAt: customElements.get('goods-card') && this._regAt };
  }
  _debugState() {   // 构建宏：__DEV__ 时保留，生产剔除
    return { sku: this._sku, loading: this._loading, subs: this._effectCount };
  }
}
// 构建校验：grep 生产 bundle 无 '_debugState' → 通过

```

**评分点**：
- debug 方法开发态注入（构建条件）。
- dsInfo 只读快照。
- 版本 data-version 同步。
- 生产剔除验证（bundle 扫描 _debugState 不存在）。
