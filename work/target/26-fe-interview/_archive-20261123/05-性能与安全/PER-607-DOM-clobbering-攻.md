---
title: [PER-607] DOM clobbering 攻击是什么？如何利用命名 id 覆盖脚本逻辑？怎么防？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-607：DOM clobbering 攻击是什么？如何利用命名 id 覆盖脚本逻辑？怎么防？

**答**：
- DOM clobbering：HTML 元素带 `id`/`name` 会自动成为 `window` 与表单/锚点链的属性，攻击者注入 `<img id="config">` 之类的无害标签，就能**覆盖 JS 依赖的全局对象**（如 `window.config`），把配置值换成恶意 URL 或对象。
- 放大技巧：`<form id="x"><input name="y">` 形成 `x.y` 链式访问、`name` 属性覆盖集合类型（HTMLCollection）、配合 `DOMPurify` 默认白名单里的 `id/name` 属性即可注入——因为它不是脚本，能过很多净化器。
- 防御：净化器剥除 `id`/`name`（或仅允许业务确认过的白名单 id）；业务代码不直接读 `window.xxx` 可疑全局（用 `Object.prototype.hasOwnProperty` 或显式定义）；关键全局用 `const config = ...` 模块作用域声明遮蔽；CSP 无用，这不是脚本执行。
- 检测：扫描业务代码中先判空再用的隐式全局引用（`if (config.url)` 而未在本文件定义 config）。

```javascript

// 攻击面演示：注入 <img id="config" src="//evil.com"> 后
// 业务脚本里的 if (window.config?.cdn) 会读到 <img> 元素而非期望配置
function hardenClobber() {
  // 1) 净化器剥除 id/name（DOMPurify: SANITIZE_DOM 配置或钩子）
  DOMPurify.addHook('uponSanitizeAttribute', (node, data) => {
    if (['id', 'name'].includes(data.attrName) && !ALLOWED_IDS.has(data.attrValue)) {
      data.keepAttr = false;                                 // 非白名单 id 一律剥除
    }
  });
  // 2) 业务侧显式遮蔽关键全局，拒绝隐式依赖
  const config = Object.freeze({ cdn: 'https://cdn.example.com' });  // 模块作用域
  return { config };
}
const ALLOWED_IDS = new Set(['app', 'root']);                // 业务确认过的锚点 id
// 3) 检测：扫描未在本文件定义却直接引用的全局标识符
```
