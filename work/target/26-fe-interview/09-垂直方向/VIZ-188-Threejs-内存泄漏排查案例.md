---
title: [VIZ-188] Three.js 内存泄漏排查案例。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-188：Three.js 内存泄漏排查案例。
**答**：**现象**——大屏运行 24h 内存涨 2GB。**排查**——① DevTools 三次堆快照对比：Texture 对象线性增长；② `renderer.info.memory.textures` 持续上涨不收敛；③ 堆快照 retainer 链指向未 dispose 的 CanvasTexture。**根因**——实时更新的告警牌每帧 `new THREE.CanvasTexture(canvas)` 未释放旧的。**修复**——纹理对象复用：同一 CanvasTexture 设置 `needsUpdate = true` 重传，或每 N 帧复用池。**防复发**——资源登记表统一 dispose、巡检断言 textures 数收敛、code review checklist 加"new 必有 dispose"。方法论：先看 renderer.info 再堆快照找 retainer。

```javascript
// 泄漏修复：纹理复用代替反复 new
// 反面模式：每帧 new CanvasTexture -> GPU 纹理堆积
// 正确模式：一块纹理反复更新
const labelCanvas = document.createElement('canvas');
labelCanvas.width = 256; labelCanvas.height = 64;
const labelTex = new THREE.CanvasTexture(labelCanvas);   // 只创建一次
function updateLabel(text) {
  const ctx = labelCanvas.getContext('2d');
  ctx.clearRect(0, 0, 256, 64);
  ctx.fillText(text, 8, 40);
  labelTex.needsUpdate = true;          // 重传同一纹理，无新 GPU 资源
}
// 巡检断言：纹理数应收敛
setInterval(() => {
  if (renderer.info.memory.textures > BASELINE_TEXTURES + 10)
    report('texture_leak_suspect', renderer.info.memory);
}, 60_000);
```
