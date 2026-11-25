---
title: [SCN-1124] IoT 设备的语音控制接入（语音指令转设备控制）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1124：IoT 设备的语音控制接入（语音指令转设备控制）

**答**：
- 链路：语音 -> 语音识别 -> 意图解析（"打开客厅灯"→ 设备+动作）-> 指令下发。
- 歧义：多设备匹配歧义（多个"灯"）→ 澄清交互（列出候选）。
- 安全：敏感指令（门锁）需二次确认。

```javascript
// 语音控制
async function voiceControl(transcript, devices) {
  const intent = parseIntent(transcript);              // { target, action }
  const candidates = devices.filter(d => matchIntent(d, intent));
  if (candidates.length > 1)
    return { clarify: candidates.map(c => c.name) };   // 澄清
  if (candidates[0].sensitive)
    return { confirm: true, device: candidates[0] };   // 二次确认
  return sendCommand(candidates[0].id, intent.action);
}
function parseIntent(t) { return { target: '灯', action: 'on' }; }
function matchIntent(d, i) { return d.name.includes(i.target); }
```
