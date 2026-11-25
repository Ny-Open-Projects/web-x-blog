---
title: [VIZ-213] WebGPU 资源生命周期管理：destroy 与 GC 协作
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-213：WebGPU 资源生命周期管理：destroy 与 GC 协作

**答**：
- WebGPU 资源（buffer/texture/pipeline）不 destroy 会常驻显存——显式 destroy 时机：场景卸载/降级切换/大临时纹理用完即毁。
- GC 不能兜底（GPU 资源跨 JS 与驱动生命周期）——资源注册表（创建登记/销毁注销）+ 泄漏检测（计数对账）。
- 管线缓存：pipeline 创建昂贵，按 desc hash 缓存复用（不做重复创建）。

```javascript
class GPUResourceRegistry {
  constructor(device) { this.device = device; this.live = new Map(); }
  createBuffer(desc, owner) {
    const buf = this.device.createBuffer(desc);
    this.live.set(buf, { desc, owner, stack: new Error().stack });   // 泄漏溯源
    return buf;
  }
  destroy(buf) { buf.destroy(); this.live.delete(buf); }
  destroyByOwner(owner) {                                 // 场景卸载批量销毁
    for (const [buf, meta] of this.live)
      if (meta.owner === owner) { buf.destroy(); this.live.delete(buf); }
  }
  leakCheck() { return { live: this.live.size,
    byOwner: groupBy([...this.live.values()], m => m.owner) }; }   // 对账
}
// pipeline 缓存：pipelineCache: Map<JSON.stringify(desc), GPURenderPipeline>
```
