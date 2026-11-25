---
title: [ENG-205] monorepo 远程缓存怎么设计与治理？缓存污染怎么办？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-205：远程缓存怎么设计与治理？
**答**：
- 缓存键设计：输入 hash（源码 + 依赖 + 环境变量声明 + 任务定义）→ 输出产物键值存储；关键在「输入完整性」——漏了 env 或 codegen 输入就会命中脏缓存。
- 治理规则：只有 CI 机器可写缓存（开发者本地只读或受信写），防止本地脏环境污染团队缓存；签名校验产物完整性。
- 缓存污染处置：检测到脏缓存（产物与源码不符）→ 按 hash 前缀批量失效 + 输入声明补全（把漏掉的 env/codegen 加进 hash 输入）。
- 命中率度量：按任务类型统计命中率（build/test/lint），命中率突降通常对应「输入声明变更」——比事故更快发现。
- 追问钩子：为什么 test 任务缓存有争议——test 结果依赖时间/网络/随机数，缓存命中率假象会掩盖 flaky；原则：确定性任务（build/lint/typecheck）放心缓存，test 缓存要快照输入完全声明或干脆不缓存。

```jsonc
// turbo.json —— 输入完整性声明
{ "globalEnv": ["NODE_ENV", "API_MOCK"],
  "tasks": {
    "build": { "inputs": ["$TURBO_DEFAULT$", "!**/*.test.ts"], "outputs": ["dist/**"] },
    "codegen": { "inputs": ["schema.graphql"], "outputs": ["src/generated/**"] } } }
// 治理：CI 写缓存（TURBO_REMOTE_CACHE_SIGNER=true），本地只读
```
