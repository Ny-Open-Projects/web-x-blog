---
title: [087] Turbopack 的函数级增量计算缓存是怎么工作的
date: 2026-11-17
categories: [Rust系构建工具]
tags: [前端面试, 面试题, Turbopack, 增量编译]
type: 面试题
---

## RBL-087：Turbopack 的函数级增量计算缓存是怎么工作的？

**答**：
- Turbopack 把每次转换（模块转译、TS 类型剥离、CSS 处理）都建模为「纯函数调用」，输入 hash + 函数版本决定是否可复用结果，粒度比 webpack 的模块级缓存更细。
- 依赖追踪是自动的：执行期间读到的文件、环境变量都会被记录为该函数的输入，下次只需校验这些输入的指纹，改动未波及的函数直接命中缓存。
- 缓存持久化到磁盘（`.turbo`），冷启动时跳过未变化部分的全部计算，这是「秒开大项目」的关键。
- 追问钩子：为什么不用 webpack 的 watch + dirty 标记？因为函数级缓存可以让「回滚一个文件」也只重算受影响的极少数函数。

```javascript
// 概念模拟：函数级增量缓存的核心思路
const cache = new Map(); // key: fnName + inputHash

function memoTask(name, deps, fn) {
  const fingerprint = deps.map(f => stat(f).mtimeMs + hash(read(f))).join('|');
  const key = name + ':' + fingerprint;
  if (cache.has(key)) return cache.get(key); // 输入没变，直接复用
  const result = fn(deps.map(read));
  cache.set(key, result);
  return result;
}

// 改动 a.ts 时，只有依赖 a.ts 的转译任务指纹变化
// import 链上游的 loader 调用全部命中缓存，跳过执行
memoTask('transpile:a.ts', ['src/a.ts'], compileTs);
memoTask('transpile:App.tsx', ['src/App.tsx'], compileTsx);
```
