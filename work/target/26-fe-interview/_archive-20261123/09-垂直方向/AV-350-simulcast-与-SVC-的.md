---
title: [AV-350]  simulcast 与 SVC 的分层编码差异
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-350： simulcast 与 SVC 的分层编码差异

**答**：
- Simulcast：同一内容编多份独立流（360p/720p/1080p），订阅端选一份——编码 N 份成本高但独立可靠。
- SVC：一层编码内部分层（时间/空间/质量层），解码端按层解——节省编码成本但依赖层间依赖（丢 I 层全崩）。
- 选型：SFU 场景 simulcast 主流（转码简单容错好）；SVC 适合带宽紧张（AV1 SVC 前沿）。

```javascript
// 分层策略
function layerStrategy({ encoders = 2, bandwidthPerUser }) {
  if (encoders >= 2)
    return { mode: 'simulcast',
      layers: [{ h: 180, kbps: 150 }, { h: 360, kbps: 400 }],
      note: '按订阅者带宽选层' };
  return { mode: 'svc', temporal: 2, spatial: 1,
    note: '单编码器分层，丢增强层不致命' };
}
```
