---
title: [WEB-130] WebGPU 与 WebTransport 代表怎样的未来方向？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-130：WebGPU 与 WebTransport 代表怎样的未来方向？
**答**：
- WebGPU：替代 WebGL 的下一代图形/计算 API，映射到 Vulkan/Metal/D3D12，暴露计算着色器（GPU 通用计算），前端可做端侧推理与大规模并行处理。
- WebTransport：基于 QUIC 的客户端-服务器传输，同一连接里同时提供可靠流（streams）与不可载数据报（datagrams），规避 TCP 队头阻塞，填补 WebSocket（只可靠有序）与裸 UDP 之间的空白。
- 组合想象：云游戏（WebTransport 传帧 + WebGPU 渲染）、实时协作（datagrams 传光标/低可靠状态）。
- 现状：WebGPU 已在主流 Chromium 与新版 Safari 落地；WebTransport 在 Chromium 可用，生态仍在演进。

```javascript
// WebGPU：申请适配器与设备，走计算管线
const adapter = await navigator.gpu.requestAdapter();
const device = await adapter.requestDevice();
const module = device.createShaderModule({
  code: `
    @compute @workgroup_size(64)
    fn main(@builtin(global_invocation_id) id: vec3u) {
      // 并行计算任务写在这里
    }`,
});
device.createComputePipeline({ layout: 'auto', compute: { module, entryPoint: 'main' } });

// WebTransport：可靠流与不可靠数据报共用一条 QUIC 连接
const wt = new WebTransport('https://transport.example.com:4433');
await wt.ready;
// 不可靠低延迟：游戏状态、实时光标
const dg = wt.datagrams.writable.getWriter();
dg.write(new TextEncoder().encode(JSON.stringify({ t: 'cursor', x: 1, y: 2 })));
// 可靠有序：聊天消息、配置下发
const stream = await wt.createSendStream();
const sw = stream.getWriter();
sw.write(new TextEncoder().encode('reliable message'));
```

## 二十二、DNS 深入
