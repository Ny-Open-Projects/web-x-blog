---
title: [WCN-985] 编译式模板 + 设计系统 token：编译时注入 token 与运行时换肤怎么取舍
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-985：编译式模板 + 设计系统 token：编译时注入 token 与运行时换肤怎么取舍

**答**：
- 结论先行：编译期把 token 内联成字面量体积最小、首屏最快，但失去运行时换肤；保留 CSS 变量可换肤但多一层解析——按「token 稳定性」分层决策。
- 分层策略：稳定 token（间距、圆角、字号、边框）编译期内联为字面量；易变 token（品牌色、主题色）保留 `var(--token)` 支持运行时换肤。
- 编译优化：编译器识别哪些 token 被标记为 dynamic（来自配置），dynamic 的输出 var()，其余内联；避免全量保留变量的开销（前文 CSS var 成本）。
- SSR 一致性：编译期注入的 token 与运行时 token 来自同一份 JSON，构建时校验版本一致，避免编译产物与实际主题漂移。
- 追问钩子：面试官问「白标客户要换 brand 色怎么办」——答：把 brand 相关 token 标 dynamic 走变量覆盖，其余稳定 token 仍内联，兼顾性能与定制。

```javascript
// 编译器按 token 稳定性决定内联 vs 变量
const tokens = { radius: '4px', primary: '#1677ff' };
const dynamic = new Set(['primary']); // 可换肤
function compile(tokenKey) {
  return dynamic.has(tokenKey) ? `var(--${tokenKey})` : JSON.stringify(tokens[tokenKey]);
}
console.log(compile('radius'));  // "4px"（内联字面量）
console.log(compile('primary')); // var(--primary)（运行时可换）
// 白标客户换 brand 色：只允许覆盖标为 dynamic 的 token
function applyOverride(k, v) {
  if (!dynamic.has(k)) throw new Error(`${k} 是静态 token，不可运行时覆盖`);
  document.documentElement.style.setProperty('--' + k, v);
}
applyOverride('primary', '#f00');
// 编译产物与运行时 token 来自同一份 JSON，构建期校验版本一致
function sameSource(buildVer, runtimeVer) {
  return buildVer === runtimeVer ? '一致' : '漂移，需重新构建';
}
console.log(sameSource('v1.2.0', 'v1.2.0'));
console.log('稳定 token 内联 + 易变 token 变量：兼顾性能与定制');
```
