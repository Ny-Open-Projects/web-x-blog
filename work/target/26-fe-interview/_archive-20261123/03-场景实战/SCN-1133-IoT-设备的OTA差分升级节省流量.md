---
title: [SCN-1133] IoT 设备的OTA差分升级（节省流量）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1133：IoT 设备的OTA差分升级（节省流量）

**答**：
- 差分：固件差分包（bsdiff）下发——新版与旧版差量（10MB→1MB），设备端合成。
- 校验：合成后 hash 校验，失败回退旧版本（不影响运行）。
- 统计：差分命中率（版本分布决定差分可行性）。

```javascript
// 差分 OTA
async function diffOTA(device, firmware) {
  const localVer = device.firmwareVersion;
  const diff = firmware.diffs?.[localVer];
  if (!diff) return { mode: 'full', url: firmware.fullUrl };
  const ok = await applyDiff(device, diff.url, firmware.hash);
  return ok ? { mode: 'diff', saved: `${(1 - diff.size / firmware.size) * 100}%` }
    : { mode: 'rollback', note: '合成失败回退' };
}
```
