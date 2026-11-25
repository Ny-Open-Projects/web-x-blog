---
title: [WCN-701] 组件库拆成多个 npm 包发布时，peerDependencies 冲突与版本锁定怎么处理？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-701：组件库拆成多个 npm 包发布时，peerDependencies 冲突与版本锁定怎么处理？

**答**：
- 结论：把 react/vue 等宿主框架声明为 peerDependencies 而非 dependencies，避免多份实例；内部共享包用 workspace:`*` 协议，由发布工具在 publish 时替换为实际版本。
- 用 `peerDependenciesMeta` 标记可选 peer；用 `overrides`/`resolutions` 在根工程收敛传递依赖版本；CI 里跑 `npm ls` 检查重复实例。
- 追问钩子：当宿主 React 18 与组件库 peer 要求 React 17 时怎么办？考察是否理解「放宽 peer 范围 + 兼容性测试」而非硬锁版本。

```javascript
// package.json 关键片段（组件库）
{
  "name": "@corp/ds-button",
  "peerDependencies": { "react": ">=17 <20" },
  "peerDependenciesMeta": { "react": { "optional": false } },
  "dependencies": { "@corp/ds-core": "workspace:*" }
}
// 发布脚本：把 workspace:* 替换为实际语义化版本
function resolveWorkspace(pkg, versions) {
  for (const [k, v] of Object.entries(pkg.dependencies || {})) {
    if (v === 'workspace:*') pkg.dependencies[k] = versions[k];
  }
  return pkg;
}
console.log(resolveWorkspace(
  { dependencies: { '@corp/ds-core': 'workspace:*' } },
  { '@corp/ds-core': '^2.3.0' }
));
```
