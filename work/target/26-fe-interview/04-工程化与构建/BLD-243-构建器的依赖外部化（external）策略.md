---
title: [BLD-243] 依赖外部化（external）策略怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-243：external 策略怎么设计？
**答**：
- external 场景：库发布（react/宿主依赖不打包——peer）、CDN 共享（多应用共用一份 react）、SSR（node_modules 由 Node 加载）——external 的语义是「引用声明而非打包」。
- external 的格式匹配：CJS external 输出 require、ESM external 输出 import——输出格式与外部化方式必须一致（CJS 输出配 ESM external 会挂）。
- 库发布的 external 清单：peerDependencies 自动外部化（rollup external: Object.keys(peerDeps)）+ 子路径外部化（lodash/fp 也要外部化）。
- 风险：external 后依赖运行环境提供——CDN 版本不可控（版本漂移）；解决方案 import maps（版本固定）。
- 追问钩子：为什么「peerDependencies 自动外部化」要包含子路径——external: ['react'] 只匹配裸名 'react'；包内 `import 'react/jsx-runtime'` 不会被外部化（被打进 bundle，产生 react 子路径双实例）——external 需要正则（/^react($|\/)/）或函数式匹配，这是库打包的经典陷阱。

```javascript
// rollup 库发布
external: (id) => /^react(-dom)?($|\/)/.test(id)     // 含子路径！
  || Object.keys(peerDeps).some(p => id === p || id.startsWith(p + '/')),
// CDN + import maps（版本固定）
{ imports: { react: 'https://cdn/react@19.0.0/esm/react.js' } }
```
