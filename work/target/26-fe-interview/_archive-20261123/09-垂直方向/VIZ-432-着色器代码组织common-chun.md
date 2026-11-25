---
title: [VIZ-432] 着色器代码组织：common chunk 与宏注入
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-432：着色器代码组织：common chunk 与宏注入

**答**：
- 工程化：公共函数（噪声/光照/工具）拆 chunk，构建期拼接注入；避免复制粘贴漂移。
- 宏：特性开关用 #define 注入（模板函数生成），比运行时分支快。
- 规范：chunk 命名（lighting.glsl.js/noise.glsl.js）+ 导出字符串常量。

```javascript
// chunk 组织
// noise.glsl.js
export const NOISE = `
float pcg(vec3 p) { ... }
float fbm(vec2 p, int oct) { ... }
`;
// lighting.glsl.js
export const LIGHTING = `
vec3 lighting(vec3 N, vec3 P, vec3 albedo) { ... }
`;
// program builder:
export function buildFS({ lights = true, noise = true } = {}) {
  return `precision highp float;
${noise ? NOISE : ''}${lights ? LIGHTING : ''}
void main() { ... }`;
}
```
