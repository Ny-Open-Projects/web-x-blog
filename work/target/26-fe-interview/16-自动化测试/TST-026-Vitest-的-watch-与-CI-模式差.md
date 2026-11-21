---
title: [TST-026] Vitest 的 watch 模式与 CI（run）模式有什么差异？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-026：Vitest 的 watch 模式与 CI（run）模式有什么差异？
**答**：
- 默认行为：`vitest`（TTY 下）进入 watch，只跑「改动文件 + 相关性图里受影响的文件」；`vitest run` 单次全量跑完即退出，CI 必须用 run。
- 相关性缓存：watch 利用 Vite 模块图做受影响分析——改一个 util 只跑 import 它的测试，本地反馈快。
- CI 差异项：`--ci` 下快照更新被禁止（missing snapshot 直接失败）、`--allowOnly=false`（only 用例视为错误）、无 TTY 时默认 watch 关闭。
- 实践：package.json 里 `test: "vitest run"` + `test:watch: "vitest"`，CI 调 run；本地 IDE/终端用 watch。
- 追问钩子：CI 上还常用 `--changed=origin/main` 只跑受本次变更影响的测试，配合覆盖率变更门禁。

```json
// package.json
{
  "scripts": {
    "test": "vitest run --ci --allowOnly=false",
    "test:watch": "vitest",
    "test:changed": "vitest run --changed=origin/main"
  }
}
```
