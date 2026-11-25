---
title: [PER-1000] 指纹采集的红线：哪些 API 属于合规敏感
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1000：指纹采集的红线：哪些 API 属于合规敏感

**答**：
- 高敏 API：电池状态（已废弃）、字体枚举、Canvas/WebGL 指纹、AudioContext 指纹、Navigator 细粒度属性组合——用于识别个体即违规。
- 合规原则：目的限定（防欺诈可、广告画像需明示）、最小化（不采集非必要属性）、透明（隐私政策列出）。
- 技术动向：浏览器侧反指纹（Uniform Noise、剪裁 API 值），企业侧需要转向"同意后的第一方数据"。
- 工程动作：埋点 SDK 建立敏感 API 准入清单，采集前查表，新 API 引入走合规评审。

```javascript
// 敏感 API 准入清单
const PRIVACY_GATED = new Set([
  'canvas-fingerprint', 'webgl-renderer-info', 'enumerate-fonts',
  'audio-fingerprint', 'battery', 'network-info-detail',
]);
function trackAllowed(capability, consent) {
  if (PRIVACY_GATED.has(capability) && consent.level < 2) {
    report({ type: 'gated-blocked', capability });
    return false;
  }
  return true;   // 同意级别 >= 2（明示同意 analytics）才放行
}
```
