---
title: [RBL-115] Bun、Deno、Node 三者定位对比？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-115：Bun、Deno、Node 三者定位对比？
**答**：
- Node：生态标准，最大兼容面与成熟工具链；性能与开发体验在三者中偏保守。
- Deno：Rust + V8，安全模型（默认无 IO 权限）、内置 TypeScript、Web 标准 API 优先；近年兼容 Node API 走务实路线，JSR 包管理。
- Bun：Zig + JSC，主打速度与一体化（runtime+install+build+test），兼容 npm 生态为路线，工程"快"优先。
- 共同趋势：都支持 Web 标准 API、原生 TS 运行、单文件可执行方向；差异集中在兼容策略与性能取舍。
- 选型：存量业务 → Node；安全沙箱/内部脚本 → Deno；CI/工具链提速与边缘场景 → Bun。
- 面试答法：给矩阵（引擎/语言/兼容策略/杀手锏）再给场景结论，不要背单点数字。
- 追问钩子：三者都在抢"新一代 JS 基础设施"位置，实际团队大多混合使用（CI 用 bun，生产用 node）。

```text
| 维度     | Node      | Deno        | Bun       |
| 引擎     | V8        | V8          | JSC       |
| 宿主语言 | C++/JS    | Rust        | Zig       |
| 兼容策略 | 标准      | 逐步兼容 Node | 兼容 npm 生态 |
| 杀手锏   | 生态      | 安全权限模型 | 一体化速度 |
| TS       | 需要 loader | 原生      | 原生      |
场景：存量业务 Node / 内部脚本 Deno / CI+工具链 Bun
```
