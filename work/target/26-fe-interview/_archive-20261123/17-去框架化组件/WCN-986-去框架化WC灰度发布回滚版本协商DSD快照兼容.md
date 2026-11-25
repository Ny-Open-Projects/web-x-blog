---
title: [WCN-986] 去框架化组件的灰度发布与回滚：版本协商 + DSD 快照兼容
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-986：去框架化组件的灰度发布与回滚：版本协商 + DSD 快照兼容

**答**：
- 结论先行：WC 灰度要「按版本渐进切流 + 快照向后兼容」——同页可能同时存在新旧版本组件（CDN 缓存/多子应用），协议必须保证旧快照能被新版本水合。
- 版本协商：用元素名带版本（ds-button-v2）或属性 `data-version` 区分；加载器按灰度比例决定 define 哪个版本，避免同名重复 define 报错。
- DSD 快照兼容：新版本要能水合旧版本服务端输出的 DSD（结构/属性兼容），否则回滚或灰度期间会 hydration mismatch——采用「渐进增强 + 容错解析」。
- 回滚：保留上一版本的 bundle 与快照解析能力，灰度指标异常时切回旧 define；注意已水合实例的迁移（监听版本变化重水合）。
- 追问钩子：面试官问「灰度期间两个版本样式冲突怎么办」——答：token 外置且版本独立作用域，或不同元素名隔离，避免同页两套全局样式互相覆盖。

```javascript
// 灰度：按元素名区分版本，避免同名 define 冲突
function defineVersioned(name, version, ctor) {
  const tag = version > 1 ? `${name}-v${version}` : name;
  if (!customElements.get(tag)) customElements.define(tag, ctor);
  return tag;
}
// 新版本需能水合旧 DSD：容错解析
function hydrateDSD(el) {
  const v = Number(el.dataset.version || 1);
  return v >= 2 ? hydrateV2(el) : hydrateV1Compat(el); // 旧快照兼容
}
function hydrateV2() {} function hydrateV1Compat() {}
```
