---
title: [SCN-1147] IoT 设备的固件版本分布与兼容矩阵
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1147：IoT 设备的固件版本分布与兼容矩阵

**答**：
- 分布：设备固件版本分布饼图（旧版本占比），升级建议（安全补丁版本强制）。
- 兼容：新旧固件 API 兼容矩阵（旧版本设备新指令支持降级）。
- 策略：强制升级（安全漏洞版本）与可选升级分开展示。

```javascript
// 固件分布
function firmwareDistribution(devices) {
  const dist = groupBy(devices, d => d.firmwareVersion);
  return Object.entries(dist).map(([ver, list]) => ({
    version: ver, count: list.length,
    pct: +(list.length / devices.length * 100).toFixed(1) + '%',
    mustUpgrade: KNOWN_VULNS.has(ver),                 // 漏洞版本强制升级
    supportsNewCmd: SEMVER_GTE(ver, '2.0.0'),
  }));
}
function SEMVER_GTE(a, b) { return a >= b; }
function groupBy(arr, fn) { const m = {}; arr.forEach(x => { const k = fn(x); (m[k] ??= []).push(x); }); return m; }
```
