---
title: [TST-015] 测试环境 jsdom / happy-dom / node 怎么选？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-015：测试环境 jsdom / happy-dom / node 怎么选？
**答**：
- node：纯逻辑、工具函数、Node/BFF 代码、服务端测试，最快也最稳定；没有 document/window。
- jsdom：组件测试默认选择（RTL 官方示例基座），DOM/CSSOM 实现最全、兼容性最好，但慢、且大量 Web API（ResizeObserver、IntersectionObserver、canvas）未实现。
- happy-dom：jsdom 的轻量替代，速度明显更快，API 覆盖略窄，遇到奇怪行为可切回 jsdom 排查。
- 混用：`environmentMatchGlobs`（或新版 `projects`）按文件路径区分环境——`**/*.node.test.ts` 用 node，组件测试用 jsdom。
- 追问钩子：环境是「每文件」隔离的，process/document 在文件间不共享，这正是测试并行安全的保证之一。

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    environment: 'jsdom',          // 默认：组件测试
    environmentMatchGlobs: [
      ['**/server/**/*.test.ts', 'node'],   // BFF 逻辑走 node
      ['**/utils/*.test.ts', 'node'],        // 纯函数没必要 jsdom
    ],
  },
});
// 单文件覆盖：文件内注释 // @vitest-environment happy-dom
```
