---
title: [H5-093] Vibration API 的能力边界与模式语法是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-093：Vibration API 的能力边界与模式语法是什么？
**答**：
- `navigator.vibrate(pattern)`：数字为振动毫秒数，数组 `[震, 停, 震, 停...]` 交替循环；传 0 或空数组停止。
- 仅 Android 系浏览器支持，**iOS Safari 完全不支持**（iOS 无网页振动通道）；桌面端无效。
- 调用需要用户已与页面交互（部分浏览器在无手势时静默失败）；返回布尔值，但 false 不能区分"不支持"与"被策略拦"。
- 先用 `'vibrate' in navigator` 特性检测，做静默降级——震动只是增强反馈，绝不能作为唯一信号通道。
- 长震动会打断系统级交互，克制使用：成功/失败/新消息等短模式即可。

```javascript
// 1) 特性检测 + 兼容封装
const buzz = (pattern) => {
  if ('vibrate' in navigator) {
    try { return navigator.vibrate(pattern); } catch { return false; }
  }
  return false;
};

// 2) 常用模式
buzz(30);                        // 轻点按反馈
buzz([40, 60, 40]);              // 双击确认感：震40停60震40
buzz([100, 50, 100, 50, 300]);   // 错误提示：两次短震 + 长震
buzz(0);                         // 立即停止

// 3) 业务接线：表单提交结果
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const ok = await submit(form);
  ok ? buzz(30) : buzz([80, 60, 80, 60, 200]);
});

// 4) 游戏手感：受击时短震
player.onHit = () => buzz([60, 40, 60]);
```
