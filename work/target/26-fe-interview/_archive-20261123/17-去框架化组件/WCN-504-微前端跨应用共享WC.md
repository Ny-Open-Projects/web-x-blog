---
title: [WCN-504] 京东微前端：qiankun 子应用间共享一套 WCN 元素时，如何避免重复 define 与样式冲突？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-504：京东微前端：qiankun 子应用间共享一套 WCN 元素时，如何避免重复 define 与样式冲突？

**答**：
- 结论：元素库由主应用以「运行时单例」加载，子应用通过 importmap 指向同一 URL，禁止各自打包。
- define 守卫：注册前检查 customElements.get(tag)，已存在则比较版本，绝不二次 define。
- 共享 constructable stylesheet 单例（全局池），子应用只引用不注入，避免样式重复与顺序冲突。
- 追问：两个子应用需要不同大版本怎么办？（答：命名空间隔离 tag 前缀，物理隔离而非共享）

```javascript
const defined = new Map();
function defineOnce(tag, Cls, version) {
  const cur = customElements.get(tag);
  if (cur) { defined.set(tag, cur.__version || 'unknown'); return cur; }
  Cls.__version = version; customElements.define(tag, Cls); defined.set(tag, version); return Cls;
}
// 主应用挂载时注入 importmap：{"imports":{"@ds/core":"https://cdn/ds/v3/core.js"}}

// 边界：子应用卸载时仅需移除 DOM，元素定义保留在单例中
window.removeEventListener('beforeunload', cleanup);
```
