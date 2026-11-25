---
title: [ARC-355] 可观测性深水区：用户会话回放（Session Replay）架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-355：可观测性深水区：用户会话回放（Session Replay）架构如何设计？
**答**：
- 技术路线：DOM 快照 + MutationObserver 增量序列化（rrweb 路线），回放端重建虚拟 DOM 渲染；不录屏，体积与清晰度都可控。
- 隐私合规是架构第一约束：录入前脱敏（input/掩码元素替换）、分级采集（普通会话只录事件流，报错会话才录 DOM）、同意管理接入。
- 触发策略：错误/崩溃/客诉工单触发"回溯录制"（滚动缓冲区保留最近 30s~2min），而不是全量录，成本差两个数量级。
- 存储：序列化数据压缩（结构相似度高，gzip/自定义字典压缩收益大），按会话分片上传，与错误事件通过 sessionId 关联。
- 应用闭环：回放 + 行为日志 + trace 三联定位，客诉处理从"猜"变成"看"。
```javascript
import { record } from 'rrweb';
const ringBuffer = [];
record({
  emit: (e) => {
    ringBuffer.push(encode(e));                // 环形缓冲
    if (ringBuffer.length > MAX_EVENTS) ringBuffer.shift();
    if (isErrorEvent(e)) flushSession();       // 出错时把缓冲整体上报
  },
  maskAllInputs: true,                          // 隐私：输入全掩码
  sampling: { mousemove: false, input: 'last' } // 降采样
});
```
