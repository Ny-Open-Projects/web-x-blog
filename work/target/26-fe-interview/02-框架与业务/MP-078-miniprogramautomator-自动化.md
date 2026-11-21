---
title: [MP-078] miniprogram-automator 自动化测试怎么用？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-078：miniprogram-automator 自动化测试怎么用？
**答**：
- automator 用脚本**控制微信开发者工具**打开项目，获取页面/元素、触发事件、断言数据，配合 jest 做 E2E。
- 能力：`miniProgram.reLaunch/navigateTo` 路由、`page.$(selector)` 查元素、`element.tap/input` 触发、`page.data()` 断言。
- 限制：需本机开发者工具（无头能力有限）、不能覆盖真机全部行为，适合冒烟与核心链路回归。

```javascript
// e2e/index.test.js（jest + automator）
const automator = require('miniprogram-automator')
test('搜索流程', async () => {
  const miniProgram = await automator.launch({ projectPath: './dist' })
  const page = await miniProgram.reLaunch('/pages/search/search')
  const input = await page.$('.search-input')
  await input.input('键盘')
  await page.waitFor(500)
  const data = await page.data()
  expect(data.list.length).toBeGreaterThan(0)
  await miniProgram.close()
})
```
