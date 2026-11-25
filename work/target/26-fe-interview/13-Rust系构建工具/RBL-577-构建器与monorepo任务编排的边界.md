---
title: [RBL-577] 构建器与 monorepo 任务编排的边界：构建器管图、编排器管序
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-577：构建器与 monorepo 任务编排的边界：构建器管图、编排器管序

**答**：
- 职责分界：**构建器**解决单包内的模块依赖图（import 级），**编排器**（turbo/nx/bazel）解决包间任务拓扑（package 级 build→build→test 的 DAG）——混淆两层是 monorepo 构建慢的常见根因（用 webpack 解决跨包依赖，或用编排器做模块级增量）。
- 接口契约：编排器需要的构建器能力——1) 声明式输入/输出（构建器必须准确说出会读哪些路径、写哪些产物，否则 turbo 的缓存指纹失真）；2) 无副作用（不写产物目录之外的东西、不依赖网络——否则缓存命中返回错结果）；3) 可重现（同输入同输出，见 RBL-543）。
- 典型协作流：turbo 计算 `package#build` 的指纹（输入文件 hash + 依赖闭包 + 环境变量白名单）→ 命中缓存直接恢复产物目录 → 未命中才真正调 rolldown；构建器的「输出清单」（manifest：产物 + sourcemap + assets）用于缓存恢复校验与下游 test 任务的输入声明。
- 边界争议题：跨包 TS 类型引用（project references / composite）到底谁管？——推荐构建器只管 d.ts 产物生成，类型检查交给编排器调 tsc（检查是全局闭包问题，单包构建器视角不完整）；这也解释了「为什么 monorepo 里 build 快了但 typecheck 慢」。
- 追问钩子：编排器的远程缓存与构建器自身的增量缓存（RBL-526 一轮、534 键指纹）是互补还是冗余？——互补：包级缓存跨机器复用（CI 共享），模块级缓存加速本地未命中时的单包内重建；两者键域不同但都要「输入闭包完整性」否则同样出错。

```javascript
// 编排器视角的构建器契约声明（rolldown 配置片段）
export default {
  input: 'src/index.ts',
  output: [
    { dir: 'dist', format: 'es' },
  ],
  // turbo/nx 需要的元信息：输入闭包与输出清单
  inputs: ['src/**', 'package.json', 'tsconfig.json'],   // 声明读集
  manifest: true,                                        // 构建后写 dist/manifest.json
  noNetwork: true,                                       // 无副作用保证（缓存要求）
};

// dist/manifest.json 结构（缓存恢复与下游声明）
// { "outputs": ["index.js", "index.js.map", "index.d.ts"], "hash": "…", "tool": "rolldown@1.x" }

// package.json 任务声明（编排器消费）
// { "scripts": { "build": "rolldown -c" }, "turbo": { "outputs": ["dist/**"], "inputs": ["src/**"] } }
```
