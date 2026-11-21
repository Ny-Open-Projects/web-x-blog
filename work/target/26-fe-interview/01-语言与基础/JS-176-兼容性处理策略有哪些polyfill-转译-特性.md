---
title: [JS-176] 兼容性处理策略有哪些？polyfill、转译、特性检测如何决策？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-176：兼容性处理策略有哪些？polyfill、转译、特性检测如何决策？

**答**：
- 决策顺序：先特性检测 → 能 polyfill 的 API 按需 polyfill → 语法差异交给构建期转译 → 无法补的能力做功能降级。
- 语法层（箭头函数/可选链/类字段）：与运行时无关，Babel/SWC + browserslist 在构建期转译掉。
- API 层（Promise.allSettled 等）：core-js 按需注入（`useBuiltIns: 'usage'`），避免全量 polyfill 拖体积。
- 能力层（IntersectionObserver/clipboard 等）：无法 polyfill 的写降级路径，检测结果缓存复用。
- 铁律：能力判断用特性检测，永远不用 UA 嗅探；UA 只用于统计归因。

```javascript
// 1. 特性检测 + 降级（运行时决策）
function copyText(text) {
  if (navigator.clipboard?.writeText) {
    return navigator.clipboard.writeText(text);     // 现代路径
  }
  // 降级：隐藏 textarea + execCommand（已废弃但仍是兜底手段）
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.cssText = 'position:fixed;opacity:0';
  document.body.appendChild(ta);
  ta.select();
  const ok = document.execCommand('copy');
  ta.remove();
  return ok ? Promise.resolve() : Promise.reject(new Error('copy failed'));
}

// 2. 检测结果缓存，避免重复探测
const supports = Object.freeze({
  intersectionObserver: 'IntersectionObserver' in window,
  webShare: typeof navigator.share === 'function',
  broadcastChannel: 'BroadcastChannel' in window,
});
// if (supports.intersectionObserver) 懒加载 v2 else 滚动监听降级

// 3. 构建期配置（browserslist + core-js 按需）
// package.json:
// "browserslist": ["> 0.5%", "last 2 versions", "not dead"]
// babel.config.js:
// presets: [['@babel/preset-env', { useBuiltIns: 'usage', corejs: 3 }]]

// 4. 决策树：语法问题 → 转译；缺 API → polyfill；
//           缺能力 → 特性检测 + 降级实现；整站太老 → 提示升级浏览器
```
