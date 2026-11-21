---
title: [OPT-109] 3D 场景的 LOD（细节层次）与降级策略怎么设计？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-109：3D 场景的 LOD（细节层次）与降级策略怎么设计？

**答**：
- LOD 思想：同一物体按"与相机距离/屏幕占比"切换不同精度模型（高模近看/低模远看/极远处 billboarad 贴图），顶点数差 10-100 倍而视觉几乎无差。
- 降级阶梯设计（从高到低）：实时阴影 -> 烘焙光照、抗锯齿 MSAA -> 关闭、粒子减半、贴图 2048 -> 1024、像素比 `min(devicePixelRatio, 2) -> 1`。
- 自适应实现：**运行时动态降档**——监控帧率滑动窗口，连续低于 45fps 自动降一档，比一次性按机型判断更稳。
- 极端兜底：WebGL 不可用/上下文丢失 -> 渲染静态截图（服务端预渲染一张全景图），体验降级但功能可用。

```javascript
// 一一对应：帧率自适应 LOD 降档控制器
class AdaptiveQuality {
  constructor(renderer, scene) {
    this.renderer = renderer;       // three.js 渲染器
    this.scene = scene;
    this.level = 2;                 // 2 高 / 1 中 / 0 低
    this.frameTimes = [];
    this._bind();
  }
  onFrame(dtMs) {
    this.frameTimes.push(dtMs);
    if (this.frameTimes.length < 60) return; // 约 1 秒窗口
    const avg = this.frameTimes.reduce((a, b) => a + b) / this.frameTimes.length;
    this.frameTimes.length = 0;
    if (avg > 22 && this.level > 0) this.setLevel(this.level - 1);      // <45fps 降档
    else if (avg < 15 && this.level < 2) this.setLevel(this.level + 1); // >66fps 升档
  }
  setLevel(lv) {
    this.level = lv;
    const presets = {
      2: { pixelRatio: Math.min(devicePixelRatio, 2), shadows: true, particles: 2000, drawDistance: 500 },
      1: { pixelRatio: Math.min(devicePixelRatio, 1.5), shadows: false, particles: 800, drawDistance: 300 },
      0: { pixelRatio: 1, shadows: false, particles: 0, drawDistance: 150 },
    }[lv];
    this.renderer.setPixelRatio(presets.pixelRatio); // 像素比是移动端最大开销源
    this.renderer.shadowMap.enabled = presets.shadows;
    scene.fog.far = presets.drawDistance;            // 视距裁剪配合雾
    // LOD 模型切换：近处高模、远处低模（three.js 内建 LOD）
    // const lod = new THREE.LOD();
    // lod.addLevel(highPolyMesh, 0);      // 0~50m
    // lod.addLevel(lowPolyMesh, 50);      // 50~200m
    // lod.addLevel(billboardSprite, 200); // 200m 外一张贴图
  }
  _bind() {
    this.renderer.setAnimationLoop((t, frame) => this.onFrame(frame.getDeltaTime?.() * 1000 || 16.7));
  }
}
// 极端兜底：WebGL 不可用时展示服务端预渲染全景图 + 文字内容，核心信息不丢
```

## 十八、端与平台特定
