---
title: [WCN-602] 笔试：实现微前端场景的自定义元素沙箱隔离器（样式作用域 + 全局副作用回收）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-602：笔试：实现微前端场景的自定义元素沙箱隔离器（样式作用域 + 全局副作用回收）

**答**：
- 需求：多个子应用各自注册同名 <ds-modal>，要求样式互不污染、window 全局副作用在卸载时完整回收。
- 思路：作用域用 data-wc-scope 属性 + 注入带属性选择器的 style；全局副作用用 snapshot 记录原始值，dispose 时回滚。
- 边界：重复 mount 幂等、style 只注入一次、snapshot 只记录首次值，避免嵌套恢复把中间态当原值。

```javascript
class ScopedSandbox {
  constructor(scopeId) {
    this.scopeId = scopeId;
    this.originals = new Map();
    this.style = document.createElement('style');
    this.style.textContent =
      `[data-wc-scope="${scopeId}"]{all:revert}`;
    this.injected = false;
  }
  mount(el) {
    if (!el || this.injected) return;
    el.setAttribute('data-wc-scope', this.scopeId);
    document.head.appendChild(this.style);
    this.injected = true;
  }
  captureGlobal(key) {
    if (!this.originals.has(key)) {
      this.originals.set(key, window[key]);
    }
  }
  dispose() {
    this.style.remove();
    this.originals.forEach((v, k) => { window[k] = v; });
    this.originals.clear();
    this.injected = false;
  }
}
const sb = new ScopedSandbox('team-a');
sb.captureGlobal('fetch');
sb.mount(document.createElement('div'));
sb.dispose(); // 全局 fetch 与样式均恢复
```

**评分点**：
- 作用域选择器用属性隔离，而非裸标签选择器（避免跨子应用污染）。
- 全局副作用 snapshot 只记录首次原值，dispose 完整回滚。
- mount 幂等 + style 只注入一次（重复调用不重复插入）。
- dispose 后状态清空，可再次 mount（可复用性）。
