---
title: [ENG-262] 依赖 fork 策略（patch 上游/fork 维护）怎么治理？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-262：fork 策略怎么治理？
**答**：
- fork 决策门槛：优先级排序——上游 PR 合入（最优）> patch-package（小补丁，随 lockfile）> 带 fork 的私有发布（中期）> 完全接管维护（沉重）——fork 是负债，必须先穷尽上游路径。
- fork 治理：fork 仓库记录「与上游的 divergence 清单」（每个 patch 为什么存在），上游发版时自动 rebase 检查——无 divergence 台账的 fork 会烂掉。
- patch-package 纪律：patch 文件必须带原因注释 + 上游 issue 链接；CI 校验 patch 仍可应用（上游更新导致 patch 失效即失败）。
- 退出策略：每个 fork 声明「何时可以退出」（上游合入 PR/需求消失），fork 清单定期评审砍量。
- 追问钩子：为什么 patch 失效要在 CI 报错而不是静默跳过——上游更新改变了被 patch 的代码时，patch 可能应用失败或应用错位；静默跳过等于补丁悄悄失效，bug 复现却查不到原因；CI 强校验让 patch 与上游保持显式同步。

```jsonc
// patch 注释纪律
// patches/moment+2.29.4.patch
// 原因: 上游未修的 DST 偏移 bug (upstream issue #5948)
// 退出条件: 上游合入后移除
```
```bash
# CI patch 校验
patch-package --error-on-fail    # patch 应用失败即构建失败
```
