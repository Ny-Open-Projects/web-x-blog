---
title: [MP-136] miniprogram-automator 自动化测试如何实战？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-136：miniprogram-automator 自动化测试如何实战？
**答**：
- 两个角色：脚本侧 `automator.launch`（拉起开发者工具）或 `automator.connect`（连接已打开的工具），页面侧获得 `miniProgram.pageStack/element`。
- 能力：导航、元素查询（选择器 `selector`）、`tap/input/trigger` 事件、取 `data`/`wxml`、调用 `wx.mockWxMethod` mock API。
- 实践：核心链路（登录→加购→下单）写成用例跑 CI（`miniprogram-ci` 起工具 headless），断言页面数据与关键 UI 文本。
- 限制：只能跑开发者工具环境（真机自动化另行方案），原生组件部分操作受限。

```javascript
// test/e2e/login-order.test.js
const automator = require('miniprogram-automator')
describe('下单链路', () => {
  let miniProgram
  beforeAll(async () => {
    miniProgram = await automator.launch({
      cliPath: '/Applications/wechatwebdevtools.app/Contents/MacOS/cli',
      projectPath: '/path/to/project'
    })
    await miniProgram.mockWxMethod('requestPayment', { errMsg: 'requestPayment:ok' }) // mock 支付
  }, 60000)
  it('加购并下单成功', async () => {
    const page = await miniProgram.reLaunch('/pages/goods/detail?id=1001')
    await page.$('.buy-btn').then(btn => btn.tap())
    await page.waitFor(500)
    const data = await page.data()
    expect(data.cartCount).toBe(1)
  })
  afterAll(() => miniProgram.close())
})
```
