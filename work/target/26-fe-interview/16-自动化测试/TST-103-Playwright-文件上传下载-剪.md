---
title: [TST-103] Playwright 怎么测文件上传、下载、剪贴板和拖拽？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-103：Playwright 怎么测文件上传、下载、剪贴板和拖拽？
**答**：
- 上传：`setInputFiles` 直接给 input 赋文件（路径/File bafer/多个文件），不走真实文件选择框——因为 `<input type=file>` 是隐藏的原生控件，代码赋值即可；动态创建的 File 对象（前端解析后上传）也能用 `filePayload` 构造。大文件上传注意 mock 上传接口测进度条。
- 下载：监听 `page.waitForEvent('download')`，`download.path()` 拿临时文件、`saveAs` 存盘后断言内容/大小；配置 `acceptDownloads: true`。
- 剪贴板：授权 `grantPermissions: ['clipboard-read', 'clipboard-write']`，`page.evaluate(() => navigator.clipboard.readText())` 读取断言。
- 拖拽：三种姿势——`locator.dragTo(target)`（最简）、手动 `mouse.move/down/move/up`（自定义轨迹，测排序插到中间）、HTML5 DnD 需要注入 DataTransfer 事件（原生 API 不触发 dragstart 时）。
- 追问钩子：文件导入解析失败怎么测？——上传一个内容非法的文件，断言错误提示与正确行数解析。

```javascript
test('上传 → 下载 → 复制 全链路', async ({ page, browserName }) => {
  await page.goto('/material');

  // 1) 上传：赋值隐藏 input
  await page.setInputFiles('input[type=file]', {
    name: 'report.csv', mimeType: 'text/csv', buffer: Buffer.from('id,name\n1,A'),
  });
  await expect(page.getByText('导入成功 1 条')).toBeVisible();

  // 2) 下载：监听事件再点击
  const downloadPromise = page.waitForEvent('download');
  await page.getByRole('button', { name: '导出' }).click();
  const download = await downloadPromise;
  const path = await download.path();
  expect(require('fs').statSync(path).size).toBeGreaterThan(0);

  // 3) 复制 + 剪贴板断言
  await page.getByTestId('copy-link').click();
  const text = await page.evaluate(() => navigator.clipboard.readText());
  expect(text).toContain('https://');
});
```
