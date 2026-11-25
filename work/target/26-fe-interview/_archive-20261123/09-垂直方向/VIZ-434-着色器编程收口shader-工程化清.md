---
title: [VIZ-434] 着色器编程收口：shader 工程化清单
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-434：着色器编程收口：shader 工程化清单

**答**：
- 资产：shader 源码进 git + 构建校验（glslangValidator）+ 变体管理 + chunk 组织。
- 质量：防御式数学（407）、调试开关（430）、性能基准（414）常态化。
- 文档：每个 shader 附 uniform 表与行为说明（自足可读），避免"祖传 shader 没人敢改"。

```javascript
// shader 模块规范
export const material = {
  name: 'pbr-standard',
  uniforms: [
    { name: 'uAlbedoMap', type: 'sampler2D' },
    { name: 'uRoughness', type: 'float', range: [0, 1], default: 0.5 },
    { name: 'uLightCount', type: 'int', default: 4 },
  ],
  variants: ['USE_NORMAL_MAP', 'USE_SKINNING'],
  chunks: ['noise', 'lighting'],
};
// CI：material.uniforms 与源码声明一致性校验
```
