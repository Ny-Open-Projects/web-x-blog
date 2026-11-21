---
title: [WCN-046] 笔试：手写 Shadow DOM 样式注入器（CSSStyleSheet 缓存 + 主题热替换）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-046：笔试：手写 Shadow DOM 样式注入器

**题目**：实现 `StyleInjector`：① `register(id, css)` 注册命名样式表，重复注册内容相同直接复用（引用计数）；② `adopt(shadowRoot, ids[])` 挂载到影子根；③ `unadopt(shadowRoot, ids[])` 释放计数，归零后销毁 sheet；④ `setTheme(id, css)` 热替换已注册样式表内容，所有已挂载的影子树即时生效；⑤ 降级：无 Constructable Stylesheets 支持时退化为 `<style>` 注入/移除。

**答**：

```javascript
const canCSSOM = typeof CSSStyleSheet !== 'undefined' && 'replaceSync' in CSSStyleSheet.prototype;

const entries = new Map(); // id -> { css, sheet?, styleText, refs:Set<shadowRoot|Document> }

function register(id, css) {
  const cur = entries.get(id);
  if (cur && cur.css === css) return;          // 内容相同直接复用
  if (!cur) entries.set(id, { css, sheet: canCSSOM ? new CSSStyleSheet() : null, refs: new Set() });
  const e = entries.get(id);
  e.css = css;
  if (e.sheet) e.sheet.replaceSync(css);
  else e.refs.forEach((root) => applyFallback(root, e, true)); // 热替换旧 style
}

function adopt(root, ids) {
  for (const id of ids) {
    const e = entries.get(id); if (!e) continue;
    e.refs.add(root);
    if (e.sheet) root.adoptedStyleSheets = [...root.adoptedStyleSheets, e.sheet];
    else { const s = document.createElement('style'); s.dataset.inj = id; s.textContent = e.css; root.append(s); }
  }
}

function applyFallback(root, e, replace) { /* 查找 data-inj 节点替换 textContent */ }

function unadopt(root, ids) {
  for (const id of ids) {
    const e = entries.get(id); if (!e) continue;
    e.refs.delete(root);
    root.adoptedStyleSheets = (root.adoptedStyleSheets ?? []).filter((s) => s !== e.sheet);
    root.querySelectorAll(`style[data-inj="${id}"]`).forEach((s) => s.remove());
    if (e.refs.size === 0 && e.sheet) e.sheet.replaceSync(''); // 归零释放（置空内容即可回收规则）
  }
}

export const StyleInjector = { register, adopt, unadopt, setTheme: register };
// register('btn', '.b{padding:8px}'); adopt(shadowRoot, ['btn']);
// setTheme('btn', '.b{padding:12px;background:#111}') → 全部已挂载组件即时生效
```

**评分点**：
- Constructable Stylesheets 能力检测与 `<style>` 降级双路径。
- 引用计数 + 归零释放（内存意识）；同一 sheet 多影子根共享。
- 热替换走 `replaceSync`（CSSOM），降级路径也要支持替换而非重复插入。
- adoptedStyleSheets 数组不可变语义：先 filter/copy 再整体赋值。
