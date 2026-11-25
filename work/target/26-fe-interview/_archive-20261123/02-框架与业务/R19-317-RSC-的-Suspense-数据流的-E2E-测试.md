---
title: [R19-317] Suspense 数据流的 E2E 测试怎么做？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-317：Suspense 数据流的 E2E 测试怎么做？
**答**：
- 等待策略：Playwright waitForSelector 针对真实内容（而非 fallback），避免偶发断言骨架。
- 网络注入：route 拦截延迟/失败特定接口，验证 fallback、错误边界、重试。
- 流式行为：慢接口时断言「主内容先出现、评论后出现」的顺序（selector 出现顺序）。
- action 流程：提交表单→断言 toast/跳转/数据变化（服务端可校验 DB）。
- 稳定性：数据响应时间波动用「内容出现即可」断言，不用固定 sleep。
