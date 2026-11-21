---
title: [WEB-456] 前端怎么防调试，DevTools 检测有必要吗
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-456：前端怎么防调试，DevTools 检测有必要吗

**答**：
- 常见手段：无限 debugger、检测窗口尺寸差（外置 DevTools）、console 对象探针、代码混淆加密
- 认清价值：只能提高逆向成本，挡不住决心；对核心算法保护，真正有效的是把逻辑搬到服务端
- 合理使用场景：风控页、答题/考试系统、付费内容——提高普通用户作弊门槛
- 副作用：无限 debugger 会误伤自家开发与崩溃定位，务必按环境开关 + 用户白名单
- 面试话术：先问业务目标（防爬/防作弊/防白嫖），再给「混淆 + 服务端逻辑 + 风控埋点」的组合拳，而不是硬杠 DevTools

```javascript
// 仅生产环境启用，且提供内部豁免
if (import.meta.env.PROD && !localStorage.getItem('__dev_exempt')) {
  setInterval(function anti() {
    const t0 = performance.now();
    debugger; // 打开 DevTools 时暂停造成明显延迟
    if (performance.now() - t0 > 100) location.reload(); // 可选：强对抗
  }, 3000);
}
```
