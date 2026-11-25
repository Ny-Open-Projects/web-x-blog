---
title: [WCN-613] 笔试：实现 Shadow DOM 内第三方库（如 Monaco/CodeMirror）样式的注入与作用域收敛
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-613：笔试：实现 Shadow DOM 内第三方库（如 Monaco/CodeMirror）样式的注入与作用域收敛

**答**：
- 需求：第三方库样式是全局 CSS 字符串，需注入到 WC 的 shadowRoot 且不泄漏到主文档；支持多实例共享一份样式表。
- 思路：用 CSSStyleSheet + replaceSync 生成共享表，adoptedStyleSheets 复用；三方库初始化目标改为 shadowRoot 内的挂载点。
- 边界：replaceSync 失败要容错；非 constructable 环境降级为 <style>；多实例 adopt 顺序保持一致。

```javascript
const sheetCache = new Map();
function getSheet(id, css) {
  if (sheetCache.has(id)) return sheetCache.get(id);
  const s = new CSSStyleSheet();
  try { s.replaceSync(css); }
  catch (e) { console.warn('[css] 解析失败', e); }
  sheetCache.set(id, s);
  return s;
}
function injectThirdParty(host, id, css, init) {
  const root = host.shadowRoot || host.attachShadow({ mode: 'open' });
  const sheet = getSheet(id, css);
  if ('adoptedStyleSheets' in root) root.adoptedStyleSheets = [sheet];
  else { const st = document.createElement('style'); st.textContent = css; root.appendChild(st); }
  const mount = document.createElement('div');
  root.appendChild(mount);
  return init(mount);
}
// injectThirdParty(el, 'monaco', globalCss, monaco.editor.create)
```

**评分点**：
- 用 CSSStyleSheet 共享缓存，多实例复用一份实例。
- replaceSync 失败容错，不抛异常中断渲染。
- 降级路径（非 constructable → <style>）完整。
- 三方库挂载点指向 shadowRoot 内节点，而非 document。
