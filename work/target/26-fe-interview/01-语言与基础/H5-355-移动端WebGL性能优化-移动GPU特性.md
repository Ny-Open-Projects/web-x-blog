---
title: [H5-355] 移动端 WebGL 性能优化：移动 GPU 的特性约束
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-355：移动端 WebGL 性能优化：移动 GPU 的特性约束

**答**：
- 移动 GPU 是 tile-based 架构（TBDR）：与桌面 immediate mode 不同——频繁切换 render target（FBO）会打断 tile 流水线，清屏用 scissor 局部清除而不是整屏 clear 多次
- 精度是移动硬约束：mediump/highp 精度不足导致闪烁/花屏（老 Mali/Adreno 经典问题），shader 里显式声明精度并测试低端机
- 带宽成本高：纹理尺寸压缩（ETC2/ASTC 格式）、mipmap 必开、避免每帧大 framebuffer 拷贝（readPixels 极慢）
- drawcall 预算：移动端 <100/帧 才稳 60fps——合批（相同材质合并）、纹理图集、instancing
- 功耗与降级：帧率锁定（不跑满 120fps）、后台强制暂停（visibilitychange）、低端机检测（渲染性能 probe 前 2 秒）自动切换低配 shader

```glsl
precision mediump float;           // 显式精度, 避免默认精度差异
uniform mediump sampler2D uTex;
void main() {
  vec4 c = texture2D(uTex, vUV);
  gl_FragColor = c;                // 避免 highp 大数运算, 老芯片精度不足闪烁
}
```

```javascript
// 帧率锁定降级
let frameTimes = [];
function tick(now) {
  frameTimes.push(now); frameTimes = frameTimes.slice(-60);
  const avg = frameTimes.length > 30 && (now - frameTimes[0]) / frameTimes.length;
  if (avg > 45 && quality > 0) setQuality(--quality);  // 降到下一档
  requestAnimationFrame(tick);
}
```
