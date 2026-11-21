---
title: [TST-031] Vitest UI 模式怎么用？测试失败怎么断点调试？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-031：Vitest UI 模式怎么用？测试失败怎么断点调试？
**答**：
- UI 模式：`vitest --ui` 启动基于 Vite DevTools 的可视化面板（需装 @vitest/ui），看用例树、耗时、错误 diff、快照对比，点击即重跑单条。
- 断点调试：VSCode 里配 launch.json 以 Node 附加方式启动 `vitest run --no-file-parallelism`，用 `--testNamePattern` 只跑目标用例，断点直接命中。
- 轻量方案：不用 UI 也能排查——`vitest run path/to/x.test.ts -t "用例名"` 精确定位；`--reporter=verbose` 看每条用例输出；console.log 在 verbose 下可见。
- 隔离排查：偶发失败先 `--sequence.shuffle` + 单文件重复跑（`vitest run --retry=0 path`），确认是不是顺序依赖或并发踩踏。
- 追问钩子：UI 面板里可以直接 diff inline 快照并一键更新，是迁移 Jest（jetbrains/终端）体验的最大提升点之一。

```json
// .vscode/launch.json —— Vitest 断点调试
{
  "type": "node",
  "request": "launch",
  "name": "Debug Vitest (current file)",
  "runtimeExecutable": "npx",
  "runtimeArgs": ["vitest", "run", "${relativeFile}", "--no-file-parallelism"],
  "console": "integratedTerminal",
  "skipFiles": ["<node_internals>/**", "node_modules/**"]
}
```
