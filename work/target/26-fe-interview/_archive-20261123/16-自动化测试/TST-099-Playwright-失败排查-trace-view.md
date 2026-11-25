---
title: [TST-099] Playwright 用例在 CI 失败了，你怎么排查？trace viewer 讲一下
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-099：Playwright 用例在 CI 失败了，你怎么排查？trace viewer 讲一下
**答**：
- 核心工具：trace viewer。配置 `trace: 'on-first-retry'`（首次重试才录制，省磁盘），失败后 `npx playwright show-trace trace.zip` 打开时间线：每一步操作、DOM 快照、网络请求、console 日志、点击位置可视化回放，本地就能完整还原 CI 现场，不需要再跑一遍。
- 排查流程：① 看失败截图 + 错误信息（TimeoutError 会写明卡在 visible/stable/enabled 哪一项）；② 开 trace 看那一步之前页面发生了什么（弹窗遮挡？接口 4xx？跳转了？）；③ 查网络面板确认 mock 是否命中、接口是否被 abort；④ 用 `page.pause()` / `npx playwright test --debug` 本地复现调试。
- 报告：`reporter: [['html', { open: 'never' }]]`，CI 产出 HTML 报告（含截图/trace 链接）作为 artifact 上传，在 PR 里贴链接。
- 常见根因排序：数据变化（后端造数没了）、时序（动画/异步）、环境差异（时区/分辨率/字体）、选择器命中了新元素。
- 追问钩子：怎么防复发？——失败即录 trace + 用例级重试 + 把 flaky 用例隔离到独立 job 跑并统计重试率。

```javascript
// playwright.config.ts
import { defineConfig } from '@playwright/test';
export default defineConfig({
  retries: 2,
  use: {
    trace: 'on-first-retry',   // 重试时录制 trace.zip
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    actionTimeout: 10_000,
  },
  reporter: [['html', { open: 'never' }], ['github']],
});
// CI 失败后：npx playwright show-trace test-results/.../trace.zip
```
