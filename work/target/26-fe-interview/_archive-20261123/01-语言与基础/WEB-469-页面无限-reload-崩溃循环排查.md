---
title: [WEB-469] 页面无限 reload/崩溃循环的排查
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-469：页面无限 reload/崩溃循环的排查

**答**：
- 循环来源分类：代码里 error 兜底逻辑写成 reload → 报错后再报错再 reload；SW 缓存了坏版本 → 更新循环重载；线上崩溃（OOM）后浏览器自动恢复 → 再崩再恢复
- 第一原则：任何「报错自动刷新」都要加次数上限与冷却（sessionStorage 记次数），这是止血开关
- 排查步骤：关掉 JS 逐层二分（先禁 SW → 用 URL 参数 ?nosw 绕过缓存；再禁可疑脚本）确认哪层引入循环
- SW 坏版本自救：提供 `?v=n` 或跳过 SW 的逃生 URL；SW 更新逻辑必须先 fetch 校验版本再 activate，不能盲目 skipWaiting + reload
- 观测：reload 事件上报带原因码与次数，监控面板对 reload 率突增告警

```javascript
// 带 att 熔断的自动刷新
const n = +sessionStorage.getItem('reloadN') || 0;
if (n < 2) { sessionStorage.setItem('reloadN', n + 1); location.reload(); }
else report({ fatal: 'reload-loop' }); // 超限进入降级 UI
```
