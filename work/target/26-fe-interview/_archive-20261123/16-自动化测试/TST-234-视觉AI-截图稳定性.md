---
title: [TST-234] toHaveScreenshot 的「稳定性清单」——保证两次截图一致的必备项？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-234：toHaveScreenshot 的「稳定性清单」——保证两次截图一致的必备项？
**答**：
- 冻结时钟（page.clock.install 固定时间）、禁动画、等字体图片、固定 locale与时区。
- deviceScaleFactor 固定（Retina 截图尺寸差异）。
- 滚动位置归零 + 关闭光标（caret: 'hide'）。
- 清单固化为测试工具函数（stableShot(page, name)），全仓统一，不逐用例散写。

```javascript
export async function stableShot(page: Page, name: string, opts = {}) {
  await page.clock.install({ time: new Date('2026-01-01T00:00:00Z') });
  await page.addStyleTag({ content: '*{animation:none!important;transition:none!important}' });
  await page.evaluate(() => document.fonts.ready);
  await expect(page).toHaveScreenshot(name,
    { caret: 'hide', animations: 'disabled', ...opts });
}
r
```
