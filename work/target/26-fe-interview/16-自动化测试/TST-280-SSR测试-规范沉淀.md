---
title: [TST-280] 「SSR 测试规范」应包含哪些强制条目？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-280：「SSR 测试规范」应包含哪些强制条目？
**答**：
- 新页面必须带：SSR 快照 + 双端一致性 + hydration mismatch 检查（dev 模式开着）。
- 动态内容（时间/随机/UA 分支）必须走规范化封装，禁止裸写。
- 缓存与 SEO 断言进 PR 门禁（关键页 checklist）。
- 错误路径：数据失败/流中错误/水合错误三类降级用例模板强制套用。

```javascript
<!-- ssr-testing-standard.md 摘要 -->
1. 每页三件套：SSR 快照 / 双端一致 / hydration 检查
2. 动态值统一 safeValue() 封装，裸 Date.now()/Math.random() lint 禁止
3. 缓存键、SEO meta、爬虫可读性进 PR checklist
4. 三类降级用例模板（数据失败/流中错误/水合错误）强制
r
```
