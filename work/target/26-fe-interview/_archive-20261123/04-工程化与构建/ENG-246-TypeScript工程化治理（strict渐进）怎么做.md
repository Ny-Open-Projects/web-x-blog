---
title: [ENG-246] TypeScript 工程化治理（strict 渐进/类型债）怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-246：TS 工程化治理怎么做？
**答**：
- 渐进 strict：strict 按开关逐个开启（noImplicitAny 先行），配合 error-count Ratchet（存量豁免清单 + 只减不增）——一次性 strict 会让存量项目瘫痪。
- 类型债管理：any 用量统计与门禁（新增 any 需注释理由）、@ts-ignore 密度治理（同 ESLint-disable）、类型覆盖率报表。
- 公共类型单源：API 类型由 schema 生成（codegen）单源，手写类型与生成类型冲突以生成为准。
- 编译速度：project references 分包编译 + incremental + 类型缓存（ENG-205 接入构建图）。
- 追问钩子：为什么「error-count Ratchet」是存量项目上 strict 的唯一可行路径——存量数千个类型错误一次性清零不现实；Ratchet 把存量冻结为上限、新增代码必须零错误，类型债随时间单调递减。

```jsonc
// tsconfig 渐进
{ "strict": false, "noImplicitAny": true, "noUncheckedIndexedAccess": false }
```
```bash
# Ratchet 门禁
current=$(tsc --noEmit 2>&1 | grep -c error)
budget=$(cat .ts-error-budget)      # 存量豁免清单
[ $current -gt $budget ] && fail "类型错误增加 $current > $budget"
```
