---
title: [WCN-214] attribute 只能是字符串——复杂类型的设计模式（序列化协议）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-214：attribute 只能是字符串——复杂类型的设计模式（序列化协议）？
**答**：
- 模式 1：property 为主（复杂对象），attribute 仅为「声明式静态场景」服务（SSR/HTML 书写）。
- 序列化协议：JSON attribute（parse 失败容错 + 控制台告警），命名 data-* 约定。
- 反射（reflect）谨慎：复杂对象反射到 attribute 会产生巨字符串——只 reflect 原始值。
- 文档契约：每个 prop 标注 attr/prop/both 与序列化格式。

```javascript
static get observedAttributes() { return ['sku', 'config']; }
attributeChangedCallback(n, _o, v) {
  if (n === 'config') {
    try { this._config = JSON.parse(v); }
    catch { console.warn('[goods-card] config attribute 非法 JSON，忽略'); }
  }
}
set config(v) { this._config = v; }  // property 主通道（不 reflect）
r
```
