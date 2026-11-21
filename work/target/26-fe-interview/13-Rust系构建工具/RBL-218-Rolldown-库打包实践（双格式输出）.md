---
title: [RBL-218] Rolldown 做库打包（ESM/CJS/类型）实践
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-218：Rolldown 做库打包（ESM/CJS/类型）实践

**答**:
- 输出：ESM + CJS 双格式（output 数组多 target）、dts 用 rolldown-plugin-dts（或 tsc 单独跑）、externals 处理 peerDependencies
- package.json exports 映射：`"." : { "import": "./dist/index.mjs", "require": "./dist/index.cjs", "types": "./dist/index.d.ts" }`
- 注意点：保留 live binding（CJS 输出用 getter 导出）、CSS 副作用（sideEffects 标注）、banner/license 注释保留
- 验证：publint/arethetypeswrong 检查类型与导出正确性，进 CI 门禁

```javascript
export default [{
  input: 'src/index.ts',
  external: [/^react($|\/)/],
  output: [{ file: 'dist/index.mjs', format: 'es' }, { file: 'dist/index.cjs', format: 'cjs' }],
  plugins: [dts()],
}]
```
