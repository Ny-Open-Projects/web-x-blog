---
title: [PER-103] 用户会话回放的原理是什么？rrweb 如何做隐私脱敏？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-103：用户会话回放的原理是什么？rrweb 如何做隐私脱敏？

**答**：
- rrweb 原理：基于**DOM 快照 + 增量变更事件**——先序列化整棵 DOM 为 JSON，之后通过 MutationObserver 记录每帧的增删改、鼠标移动、滚动、输入，回放端按事件流重建。
- 体积控制：事件流经protobuf/压缩后几十 KB/分钟，配合采样与“触发式录制”（错误发生时回溯保留前 30 秒）。
- 隐私脱敏两条线：**录制时脱敏**（`maskAllInputs`、自定义 `maskTextFn` 把手机号密码打码，脱敏后的数据离线，合规性最强）、**回放时限制**（脱敏数据永远不可逆）。
- 合规底线：录制前用户告知或协议授权、不录制支付页与密码框、数据保留期限与删除机制。

```javascript
// rrweb 接入：录制时脱敏 + 错误触发式保留
import { record } from 'rrweb';
import { pako } from 'pako-lib';

let events = [];
const stop = record({
  emit(event) {
    events.push(event);
    if (events.length > 2000) events.shift(); // 环形缓冲，只保留最近窗口
  },
  maskAllInputs: true,                        // 所有输入框内容录制为 ******
  maskTextSelector: '.sensitive, [data-private]', // 敏感区域文本打码
  inlineStylesheet: false,                    // 不内联样式表，减小体积
  blockSelector: '#payment-form',             // 支付表整块不录
  sampling: { mousemove: 200, scroll: 150 },  // 降低高频事件采样密度
});

// 错误发生时：把环形缓冲里前 30 秒事件流压缩上报
window.addEventListener('error', () => {
  const compressed = pako.gzip(JSON.stringify(events.slice(-500)));
  navigator.sendBeacon('/api/replay', compressed);
  events = []; // 上报后清空，避免重复
});
```
