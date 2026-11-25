---
title: [SCN-681] UE 像素流推流的延迟与成本怎么权衡？输入回传怎么做？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-681：UE 像素流推流怎么权衡？
**答**：
- 链路与延迟：UE 服务端渲染 → WebRTC 编码推流 → 浏览器解码；延迟构成 = 渲染帧时间 + 编码 + 网络 + 解码，局域网典型 100~200ms——交互（拖拽相机）必须做本地预测/插值缓冲否则「跟手感差」。
- 输入回传：键盘/鼠标事件序列化经 DataChannel 发给 UE，高频事件（鼠标移动）合并发送；触屏要映射为虚拟摇杆。
- 成本模型：单 GPU 4 路并发 → N 块屏需 N/4 卡 + 会话调度（空闲大屏释放会话，交互时再分配）。
- 降级预案：GPU 集群满载时排队或降级到 Web-GL 低模版本（前端保留两套渲染实现的开关）。
- 追问钩子：为什么大屏（只看不操作）适合推流而交互端不适合——只看不操作对延迟不敏感，可以多路复用一帧画面（组播思路），成本大幅摊薄。

```javascript
// 输入回传（合并高频事件）
const input = {
  buffer: [], flushScheduled: false,
  push(evt) {
    this.buffer.push(serialize(evt));
    if (!this.flushScheduled) {
      this.flushScheduled = true;
      setTimeout(() => {
        dc.send(JSON.stringify({ batch: this.buffer }));   // DataChannel 低延迟通道
        this.buffer = []; this.flushScheduled = false;
      }, 33);                                               // 30Hz 合并
    }
  },
};
// 会话调度：空闲屏释放
session.on('idle', (screenId) => session.release(screenId, { keepWarm: false }));
session.on('interact', (screenId) => session.allocate(screenId, { gpu: leastLoaded() }));
```
