---
title: [RBL-155] Turborepo 的缓存与远程缓存是怎么工作的
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-155：Turborepo 的缓存与远程缓存是怎么工作的

**答**：
- 任务指纹（hash）：turbo 对每个 task 计算 hash = 包源码 hash + 依赖包源码 hash + 环境变量（declare）+ 配置/lockfile + task 命令；输入不变则 hash 不变。
- 命中行为：本地缓存在 .turbo/cache，命中直接回放日志 + 恢复 outputs（配置在 turbo.json 的 outputs 数组），不执行命令；远程缓存（Vercel / 自托管）把"hash→产物包"放到中心服务，CI 之间、本地与 CI 之间共享。
- outputs 要精确声明（dist/**、coverage 等）：声明太少导致命中后产物缺失，声明太多传输慢。
- 关键约束：指纹必须覆盖全部影响产物的输入，用 envWildcards/strict env 模式防"环境变量漏进指纹导致复用错误产物"。
- 追问钩子：为什么 turbo 缓存比 CI 平台缓存更有效——粒度是"任务级"而非"整仓目录级"，且跨机器共享（同事跑过你就不必重跑）。

```json
// turbo.json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],        // 先构建上游依赖
      "inputs": ["$TURBO_DEFAULT$", "!**/*.test.*"], // 测试文件变化不失效 build
      "env": ["NODE_ENV", "NEXT_PUBLIC_*"],           // 进指纹的环境变量白名单
      "outputs": ["dist/**", ".next/**", "!.next/cache"] // 精确产物声明
    },
    "test": { "dependsOn": ["build"], "outputs": ["coverage/**"] }
  }
}
// 远程缓存登录：npx turbo login && npx turbo link
// 自托管：TURBO_API/TURBO_TOKEN/TURBO_TEAM 三个环境变量指向自建服务（兼容协议）
```
