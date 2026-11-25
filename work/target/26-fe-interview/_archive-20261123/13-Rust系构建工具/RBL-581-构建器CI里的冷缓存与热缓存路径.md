---
title: [RBL-581] CI 与本地的缓存路径差异：为什么 CI 上构建工具经常「比本地还慢」
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-581：CI 与本地的缓存路径差异：为什么 CI 上构建工具经常「比本地还慢」

**答**：
- 本地构建快靠三套热缓存：OS page cache（文件读）、构建器增量缓存（上次产物）、依赖预构建缓存（node_modules/.vite）；CI 每次全新容器，三套全冷——所以「本地 3 秒、CI 90 秒」不是工具问题而是缓存拓扑问题。
- CI 补偿策略逐层对应：1) page cache 层——依赖安装走远程包缓存（pnpm store 缓存 / turbo remote cache 恢复 node_modules）；2) 构建器增量缓存——把 .cache 目录纳入 CI cache 但**必须验证键**（git hash + 配置 hash + 依赖版本），错误复用缓存比不用更危险；3) 预构建产物——直接缓存 node_modules/.vite / .rspack 目录。
- 更根本的解法：**任务级远程缓存**（turbo/nx/bazel）——CI 不依赖「目录级」缓存搬运，而是按任务指纹直接取产物，恢复 O(秒级)；指纹要素：源码 hash、依赖闭包、配置、环境变量白名单、工具版本（缺一都会错缓存）。
- 反模式清单：CI 里关缓存图省事（每次全量）；缓存 key 用时间戳（永远 miss）；缓存目录不校验直接用（污染产物）；多分支共享缓存但没隔离 experimental 分支（脏产物回主流）。
- 追问钩子：为什么构建器的模块级增量缓存在 CI 上基本无效？——模块缓存的价值前提是「图大部分不变」，CI 场景首次全量构建时图全新，模块缓存无从复用；CI 的正确目标是「任务级复用」（整个 build 跳过），两者键域不同。

```javascript
// CI 缓存键的正确构成（GitHub Actions 概念）
const cacheKey = [
  'rolldown-build',
  hashFiles('src/**', 'package.json', 'pnpm-lock.yaml', 'rolldown.config.*'),
  process.env.NODE_VERSION,          // 工具链版本参与键
].join('-');
// actions/cache@v4: key = cacheKey, restore-keys = 'rolldown-build-'（前缀回退，部分命中）

// 防脏缓存：缓存恢复后校验
if (fs.existsSync('.rolldown-cache/MANIFEST')) {
  const m = JSON.parse(fs.readFileSync('.rolldown-cache/MANIFEST'));
  if (m.key !== cacheKey) { fs.rmSync('.rolldown-cache', { recursive: true }); } // 键不符即弃
}

// 最优解：任务级远程缓存
// turbo build --api=internal —— 指纹命中直接下载 dist/，构建器根本不启动
```
