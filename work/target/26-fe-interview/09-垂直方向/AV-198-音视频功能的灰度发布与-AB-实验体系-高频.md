---
title: [AV-198] 音视频功能的灰度发布与 AB 实验体系。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-198：音视频功能的灰度发布与 AB 实验体系。（高频）
**答**：
- 特殊性：核心指标有长期累积属性（卡顿率/留存），实验周期要长（≥2 周），看分位数不是均值。
- 分层实验：传输层（协议/CDN/编码参数）与体验层（UI/交互）分开实验，避免互相污染。
- 灰度维度：按用户/地域/机型/网络多维圈量；新编码参数先灰度自有测试房间再放量。
- 守护熔断：设置自动熔断（秒开劣化 > 2% 自动暂停放量），避免坏实验伤及大盘。
- 证据留存：实验报告带置信区间与维度下钻（"弱网用户受影响更大"这类发现最值钱）。

```typescript
// 实验分流与守护熔断
interface Experiment {
  key: string;
  layers: string[];
  traffic: number;                       // 0-1
  guard: { metric: string; threshold: number };
}
function assign(userId: string, exp: Experiment): 'control' | 'treatment' {
  const h = hash(`${exp.key}:${userId}`) % 10000 / 10000;
  return h < exp.traffic ? 'treatment' : 'control';
}
class GuardMonitor {
  check(current: number, baseline: number, exp: Experiment): 'ok' | 'pause' {
    // 例: 秒开率基线92% treatment 降到89% → 劣化3.3% 超阈值熔断
    const degrade = (baseline - current) / baseline;
    if (degrade > exp.guard.threshold) {
      this.pauseAndAlert(exp.key, { current, baseline });
      return 'pause';
    }
    return 'ok';
  }
  private pauseAndAlert(key: string, data: object) { /* 暂停放量并告警 */ }
}
```
