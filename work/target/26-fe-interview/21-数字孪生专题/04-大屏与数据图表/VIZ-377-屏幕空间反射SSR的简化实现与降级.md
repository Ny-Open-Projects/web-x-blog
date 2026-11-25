---
title: [VIZ-377] 屏幕空间反射（SSR）的简化实现与降级
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-377：屏幕空间反射（SSR）的简化实现与降级

**答**：
- SSR：对屏幕空间深度做 ray march（步进 + 二分细化），命中则采样屏幕颜色。
- 限制：只能反射屏幕内内容（出屏缺失用环境贴图兜底）、粗糙表面走预模糊 mip。
- 降级矩阵：低端机关 SSR 用环境贴图；中端半分辨率；高端全分辨率 + 二分细化。

```javascript
// SSR ray march
function ssr(color, depth, uv, normalVS, viewDirVS, { steps = 16 } = {}) {
  let pos = viewPos(uv, depth);
  const rd = reflect(viewDirVS, normalVS);
  for (let i = 0; i < steps; i++) {
    pos = pos.map((v, j) => v + rd[j] * stepSize(i));
    const sUV = projectToScreen(pos);
    if (sUV[0] < 0 || sUV[0] > 1) return sampleEnv(rd);      // 出屏兜底
    const d = depth.at(sUV);
    if (pos[2] >= d) {                                       // 命中近似
      return sampleColor(sUV);
    }
  }
  return sampleEnv(rd);
}
function reflect(I, N) { const d = dot(I,N); return I.map((v,i)=>v-2*d*N[i]); }
function dot(a,b){return a[0]*b[0]+a[1]*b[1]+a[2]*b[2];}
```
