---
title: [PER-770] 移动端 H5 游戏页（Canvas/WebGL）的性能预算与降级：帧率、内存与发热的三角平衡
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-770：移动端 H5 游戏页（Canvas/WebGL）的性能预算与降级：帧率、内存与发热的三角平衡

**答**：
- 预算分配：游戏循环总预算 16.6ms（60fps）——JS 逻辑 < 5ms、渲染提交 < 8ms、GC 余量；低端机降到 30fps（预算翻倍）。
- 三角平衡：**帧率**（固定步长逻辑 + 可变渲染）、**内存**（纹理压缩格式 ASTC/对象池/及时 destroyUnusedTextures）、**发热**（发热导致 thermal 降频的恶性循环——检测到持续降频主动降帧率而不是硬扛）。
- 手段：离屏预渲染静态背景（一张大图一次绘制）、粒子池、按需绘制（静止画面跳过渲染帧）、WebGL 纹理按需 mipmap。
- 度量：帧耗时分布（JS vs GL 提交）、纹理内存、thermal 事件（容器侧回调）频次。

```javascript

const gamePerfBudget = {
  frame: { total: '16.6ms @60fps', js: '< 5ms', glSubmit: '< 8ms', lowEnd: '30fps 预算翻倍' },
  triangle: { fps: '固定步长逻辑+可变渲染', mem: 'ASTC 纹理压缩+对象池+destroyUnusedTextures',
    thermal: '检测持续降频 -> 主动降帧率，防恶性循环' },
  tricks: ['静态背景离屏预渲染', '粒子池', '静止画面跳过渲染帧'],
};
// 固定步长示例
function gameLoop(t) {
  acc += t - last; last = t;
  while (acc >= STEP) { update(STEP); acc -= STEP; }             // 逻辑固定步长
  if (dirty || moving) render();                                 // 静止跳过渲染
  requestAnimationFrame(gameLoop);
}
```
