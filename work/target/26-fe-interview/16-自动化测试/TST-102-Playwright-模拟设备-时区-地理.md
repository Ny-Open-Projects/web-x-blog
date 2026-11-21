---
title: [TST-102] Playwright 怎么模拟移动设备、时区、地理位置、语言？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-102：Playwright 怎么模拟移动设备、时区、地理位置、语言？
**答**：
- 设备模拟：`devices` 内置描述文件（iPhone 14、Pixel 7 等），一键带齐 viewport/UA/DPR/touch/移动端特性；`use: { ...devices['iPhone 14'] }`。触屏点击用 `tap()` 而不是 `click()` 才走 touch 事件。
- 时区与 locale：context 级 `timezoneId: 'Asia/Tokyo'`、`locale: 'ja-JP'`，影响 `Intl`、`Date` 解析、`navigator.language`——测国际化、汇率展示、跨时区"今日"边界的必备手段。
- 地理位置：`geolocation: { latitude, longitude }` + `grantPermissions: ['geolocation']`，测"附近门店"推荐；`isOffline: true` 测离线兜底；`colorScheme: 'dark'` 测暗色模式。
- 硬件传感器之外的模拟：`page.emulateMedia({ reducedMotion: 'reduce' })` 测无障碍偏好；`clock` API（1.45+）可快进时间测会员过期、定时刷新。
- 追问钩子：为什么不用系统代理改时区？——context 级模拟是每用例独立的，且精度到 Intl 层，Docker 里改系统时区会全局污染。

```javascript
import { test, devices } from '@playwright/test';

test.use({
  ...devices['iPhone 14'],              // 移动端全套
  locale: 'ja-JP',                      // 日文环境
  timezoneId: 'Asia/Tokyo',             // 东九区
  geolocation: { latitude: 35.68, longitude: 139.76 }, // 东京
  permissions: ['geolocation'],
  colorScheme: 'dark',
});

test('移动端附近门店（东京）', async ({ page }) => {
  await page.goto('https://m.example.com/stores');
  await page.getByRole('button', { name: '定位' }).tap(); // 触屏 tap
  await expect(page.getByText('新宿店')).toBeVisible();
  await expect(page.getByText('营业中')).toBeVisible();   // 东京时区判断
});
```
