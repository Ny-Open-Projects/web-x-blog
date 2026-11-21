---
title: [ALG-176] 前端 SDK 校验回调签名时用了 `===`，安全审计指出存在时序攻击面。为什么？如何实现常数时间比较？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-176：前端 SDK 校验回调签名时用了 `===`，安全审计指出存在时序攻击面。为什么？如何实现常数时间比较？
**答**：`===` 逐字符比较且短路——第一位不同立即返回 false，攻击者通过精确测量响应耗时，可逐位爆破出正确签名（每一位平均 62 次尝试定位）。常数时间比较：无论哪一位不同，都完整遍历所有字节，用按位或累积差异 `diff |= a[i] ^ b[i]`，最后统一判断，耗时与"正确位数"无关。长度不同可直接返回（长度本身不构成秘密）。

```javascript
function timingSafeEqual(a, b) {
  const ba = new TextEncoder().encode(a);
  const bb = new TextEncoder().encode(b);
  if (ba.length !== bb.length) return false; // 长度差异不泄漏内容，可提前返回
  let diff = 0;
  for (let i = 0; i < ba.length; i++) {
    diff |= ba[i] ^ bb[i];                   // 全量遍历，绝不提前退出
  }
  return diff === 0;                         // 耗时与正确位数无关
}
// 场景：SDK 校验支付回调签名、Webhook token 预检
// 对比：a === b 在第一位就不同时几乎零耗时，攻击者按耗时逐位爆破
```

## 二十、性能度量算法

> ALG-177 ~ ALG-181：FP/FCP 采集、FPS 与掉帧率、长任务检测、曝光度量、内存趋势——性能监控 SDK 的五个核心算法。
