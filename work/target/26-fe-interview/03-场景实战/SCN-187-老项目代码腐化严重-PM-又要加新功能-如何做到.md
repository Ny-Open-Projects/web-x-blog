---
title: [SCN-187] 老项目代码腐化严重，PM 又要加新功能，如何做到"新功能不背旧债"？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-187：老项目代码腐化严重，PM 又要加新功能，如何做到"新功能不背旧债"？
**答**：
- 隔离优先：新功能以独立模块/挂载点接入老页面，不 import 老代码（老代码只通过明确的接口暴露数据），防止新代码被旧风格感染。
- 全局污染防护：新模块用 Shadow DOM 或 CSS Modules + 命名空间，不依赖也不修改老页面的全局变量与样式；router/store 各用各的实例。
- 数据契约显式化：老页面 → 新模块只传 props，新模块 → 老页面只发事件，双向都不直接摸对方内部状态。
- 把"隔离"变成可度量约定：lint 禁止新目录 import 旧目录，CI 里新模块的依赖关系图单向。

```javascript
// 老页面加新功能：挂载点隔离 + 事件通信 + 依赖单向
// 老页面（遗留代码，不改动）：只预留一个挂载点与基础数据
// legacy.html: <div id="loyalty-widget"></div>

// 新功能模块（全新目录 src/features/loyalty/）：不 import 任何旧代码
export function mountLoyaltyWidget(hostEl, { getUserInfo, subscribeEvent }) {
  // 样式隔离：Shadow DOM，老页面全局样式进不来，新样式也不外泄
  const shadow = hostEl.attachShadow({ mode: 'open' });
  shadow.innerHTML = `
    <style>/* 组件自有样式，与老页面完全隔离 */ .card { border-radius: 8px; }</style>
    <div class="card" id="root"></div>`;

  // 数据通过显式契约进入，不直接读老页面全局变量
  getUserInfo().then(u => render(shadow.getElementById('root'), u));

  // 对外只发事件，老页面决定要不要响应
  emit(hostEl, 'loyalty:exchange', { points: 500 });

  return {
    // 老页面事件通过订阅进入新模块，数据流向始终单向
    destroy: () => { unsubscribe(); hostEl.shadowRoot?.replaceChildren(); },
  };
}
function emit(el, type, detail) { el.dispatchEvent(new CustomEvent(type, { detail, bubbles: true })); }

// 桥接层（唯一允许接触两边代码的文件，控制在一个文件内）
// src/bridges/loyalty-bridge.js
import { mountLoyaltyWidget } from '@/features/loyalty';
export function initLegacyLoyalty() {
  const host = document.getElementById('loyalty-widget');   // 老页面挂载点
  const widget = mountLoyaltyWidget(host, {
    getUserInfo: () => window.__LEGACY_API__.fetchUser(),   // 老系统 API 经契约暴露
    subscribeEvent: window.__LEGACY_BUS__.on,
  });
  host.addEventListener('loyalty:exchange', e => window.__LEGACY_BUS__.emit('openExchange', e.detail));
  return widget;
}
// CI 约束：features/** 禁止 import legacy/**，bridge 目录白名单放行
```
