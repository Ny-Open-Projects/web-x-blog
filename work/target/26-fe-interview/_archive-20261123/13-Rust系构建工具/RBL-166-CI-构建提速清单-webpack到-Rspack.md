---
title: [RBL-166] 一个真实 CI 构建提速清单：从 webpack 到 Rspack 的全链路
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-166：一个真实 CI 构建提速清单：从 webpack 到 Rspack 的全链路

**答**：
- 阶段一（不换工具，0.5 天）：缓存 node_modules 与构建产物、test 分片、lint/test/build 三 job 并行——通常已把 30min 压到 15min。
- 阶段二（换编译内核）：babel-loader→swc-loader 或整体迁 Rspack（配置迁移见 RBL-011），构建阶段常见 3~5x；minify 换 SWC（RBL-136）。
- 阶段三（任务层）：turbo/nx 远程缓存 + affected 构建，PR 流水线只构建受影响子图，典型从 15min 到 3~5min。
- 度量闭环：每阶段记录 job 总耗时与分阶段耗时，防止"提速被新依赖安装吃掉"；上线后监控 P50/P95 防回归（RBL-171）。
- 追问钩子：能按"投入产出比"排优先级（先缓存并行这类低成本项）体现工程判断，直接答"上 Rspack"反而是减分项。

```text
实测示例（电商中台，14 包 monorepo，4C CI runner）
──────────────────────────────────────────────
基线        webpack 全量 build+test  32min
+缓存并行    node_modules 缓存/test 4 分片/3 job 并行  →  14min
+换内核      webpack→Rspack（build 阶段 8min→2min）    →  8min
+任务缓存    turbo 远程缓存 + affected                 →  3.5min
──────────────────────────────────────────────
每步收益都复测过 install/build/test 三段，防止此消彼长。
```
