---
title: [VIZ-415] 3D 拾取在 shader 侧：ID 渲染 pass 的实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-415：3D 拾取在 shader 侧：ID 渲染 pass 的实现

**答**：
- ID pass：单独 program 输出实例 ID 编码色（396/377），无光照无混合。
- 与 CPU 射线取舍：静态场景 BVH（359）CPU 快；动态实例多时 GPU ID pass 简单可靠。
- 读取成本：readPixels 同步阻塞——WebGPU 用异步 buffer map；或只读 1px。

```javascript
// ID pass program
`// vs: 传 instance id
in float aInstanceId; flat out vec3 vId;
void main() { vId = unpackId(aInstanceId); ... }
// fs: 
@fragment fn fs(@location(0) id: vec3<f32>) -> @location(0) vec4<f32> {
  return vec4(id, 1.0);   // 已关闭混合与 AA
}`
// flat 插值保证 ID 不被插值污染（WGSL @interpolate(flat)）
```
