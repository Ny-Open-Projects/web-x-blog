---
title: [VIZ-217] WebGPU 错误恢复：设备丢失与上下文重建
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-217：WebGPU 错误恢复：设备丢失与上下文重建

**答**：
- 题目：WebGPU 设备丢失（驱动崩溃/标签页恢复）后可视化白屏——设计完整恢复流程：检测→重建→状态恢复→用户提示。
- 思路：device.lost.then 捕获 → 全量重建（adapter/device/所有 buffer/texture/pipeline）→ 渲染状态（相机/数据）从应用层快照恢复 → 降级提示。
- 评分点：lost 事件与重建链；资源注册表（VIZ-213）支撑重建；用户侧降级提示。

```javascript
class GPURecovery {
  constructor() { this.stateSnapshot = null; }
  arm(device, rebuildFn) {
    device.lost.then(async (info) => {                     // 丢失回调
      report('gpu-lost', { reason: info.reason });
      if (info.reason === 'destroyed') return;             // 主动销毁不重建
      showToast('渲染异常，正在恢复…');
      const device2 = await this.createDevice();           // 重建 device
      await rebuildFn(device2);                            // 注册表驱动全量重建
      this.restoreState();                                 // 相机/选区/数据快照恢复
      showToast('已恢复');
    });
  }
  snapshotState(camera, selection) {
    this.stateSnapshot = { camera: { ...camera }, selection: [...selection] };
  }
  restoreState() { Object.assign(camera, this.stateSnapshot.camera); }
}
```

## 补充：评分点与变体

**评分点**：

- 注册 device.lost 回调并区分 reason 为 destroyed 时不重建（给分）；不判断原因一律重建，主动销毁后反而白屏（扣分）。
- 重建走 adapter.requestDevice 全链路，并用资源注册表遍历重建 buffer、texture、pipeline（给分）；只重建 device 不重建资源导致空渲染（扣分）。
- 恢复前从应用层快照取相机与数据状态，重建后重放（给分）；状态丢失回到初始视角，用户视角被重置（扣分）。
- 重建失败有降级提示与重试上限（如 2 次后转静态图）（给分）；无限重试导致页面反复闪白（扣分）。

**变体与延伸**：

1. 设备丢失发生在渲染循环中间，在途 commandBuffer 怎么处理 → lost 后立即停止 rAF 并丢弃在途命令，重建完成再重启循环，避免向失效 device 提交。
2. 驱动不稳定导致反复丢失，怎么避免用户一直白屏 → 统计单位时间丢失次数，超过 3 次每分钟就降级到 Canvas2D 渲染并上报机型与驱动版本。
