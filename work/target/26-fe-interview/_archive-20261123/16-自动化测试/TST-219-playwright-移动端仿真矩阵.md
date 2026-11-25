---
title: [TST-219] 移动端仿真（viewport/UA/触摸）在测试矩阵中如何组织？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-219：移动端仿真（viewport/UA/触摸）在测试矩阵中如何组织？
**答**：
- 用 devices 描述符（iPhone 14/Pixel 7）统一 viewport+UA+触摸+DPR。
- 矩阵按业务：核心购物链路覆盖移动+桌面，桌面专属功能只桌面矩阵。
- 触摸与 hover 差异是移动端断言的高频坑（hover 菜单在触摸端不可用）。
- 真机云（BrowserStack）用于仿真覆盖不了的（推送/相机/真机性能），成本高按需用。

```javascript
import { devices } from '@playwright/test';
export default defineConfig({
  projects: [
    { name: 'mobile-safari', use: { ...devices['iPhone 14'] } },
    { name: 'desktop-chrome', use: { ...devices['Desktop Chrome'] } },
  ],
});
r
```
