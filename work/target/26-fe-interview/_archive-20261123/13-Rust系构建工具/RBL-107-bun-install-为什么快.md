---
title: [RBL-107] bun install 为什么快？主要机制有哪些？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-107：bun install 为什么快？主要机制有哪些？
**答**：
- 并行网络：HTTP 请求全并行（Zig 实现的异步 IO），下载 tarball 并发度远高于 npm 的串行队列设计。
- 全局缓存 + 硬链接：包内容存全局缓存（内容寻址），项目 node_modules 用硬链接/Copy-on-Write 复用，重复安装几乎零 IO——与 pnpm 类似但实现层在系统调用级更省。
- 二进制 lockfile：bun.lockb 用二进制格式（新版也支持文本 bun.lock），读写快且带校验。
- 无 JS 运行时开销：安装器不是跑在 Node 上的 JS 程序，冷启动即原生速度。
- 缓存命中数据：CI 里二次安装通常从数十秒降到 1-3 秒；首次安装也比 npm 快数倍。
- 追问钩子：快之外要关注兼容性——postinstall 脚本、平台二进制包（esbuild/swc 的 optionalDependencies）在 bun 下的解析要与 npm 行为核对。

```bash
# 对比量级（中型项目，缓存热）
# npm install   : ~40s
# pnpm install  : ~8s
# bun install   : ~2s
bun install --frozen-lockfile   # CI 推荐：lockfile 严格校验
bun pm cache                    # 查看全局缓存位置
```
