---
title: [SCN-936] 政务大厅的现场服务终端（自助机）UI 设计
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-936：政务大厅的现场服务终端（自助机）UI 设计

**答**：
- 终端：触屏大字体、简化层级（3 步内到办事）、身份证刷卡登录。
- 输入：扫码/刷卡替代打字（身份证 OCR/扫一扫）、语音辅助输入。
- 超时：无操作 60s 自动回到首页（防止占机）。

```javascript
// 自助机超时
function kioskIdleGuard({ idleMs = 60_000 } = {}) {
  let last = Date.now();
  ['touchstart', 'click'].forEach(e => document.addEventListener(e,
    () => last = Date.now(), { passive: true }));
  const timer = setInterval(() => {
    if (Date.now() - last > idleMs) {
      resetToHome();
      last = Date.now();
    }
  }, 5000);
  return () => clearInterval(timer);
}
```
