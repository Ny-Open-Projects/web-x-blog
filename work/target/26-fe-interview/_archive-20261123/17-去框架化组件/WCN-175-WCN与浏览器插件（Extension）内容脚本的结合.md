---
title: [WCN-175] WCN 与浏览器插件内容脚本的结合：如何在任意页面安全注入 UI？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-175：WCN 与浏览器插件内容脚本的结合：如何在任意页面安全注入 UI？

**答**：
- 场景：插件的浮层（划词翻译、比价条）要注入任意页面——WCN + Shadow DOM 是标准解法：DOM/样式完全隔离，不与页面样式/全局变量冲突。
- 实施要点一：宿主容器——创建独立挂载点（document.body.append 遮罩容器），全部 UI 以 WC 形式放其内；注入脚本用 `world: 'MAIN'` 与否决定能否访问页面 window（V3 manifest）。
- 要点二：样式加载——组件 CSS 打包进 content script（影子树内联），避免依赖页面允许的 CSS 域；DSD 也可用（MV3 content script 可以插 HTML）。
- 要点三：通信——组件事件 → content script → chrome.runtime.sendMessage → background/service worker；组件本身容器无关（仍走 wc-native-request 声明模式）。
- 要点四：安全与性能——SPA 页面的 DOM 变动频繁，容器监听要防页面重排冲突（z-index 管理与 body 监听节流）；页面 CSP 可能拦截外部资源——组件产物随扩展打包，不外链。

```javascript
// content-script.js
const host = document.createElement('div');
host.id = 'acme-ext-root';
document.body.append(host);
const shadow = host.attachShadow({ mode: 'open' });   // 与页面样式完全隔离
// 注入组件（产物随扩展打包）
import(chrome.runtime.getURL('acme-translate.js')).then(() => {
  const el = document.createElement('acme-translate');
  el.addEventListener('wc-native-request', (e) => {
    chrome.runtime.sendMessage(e.detail).then((r) =>
      el.dispatchEvent(new CustomEvent('wc-native-result', { detail: r })));
  });
  shadow.append(el);
});
```
