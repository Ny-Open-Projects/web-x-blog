---
title: [OPT-105] SVG 怎么优化？内联和外链怎么决策？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-105：SVG 怎么优化？内联和外链怎么决策？

**答**：
- 工具链：SVGO 去元数据/注释/空组、合并路径、压缩坐标精度，平均省 30-60%；但要**禁用过度移除**（removeViewBox、collapseGroups 可能破坏样式作用域）。
- 内联 vs 外链决策：**图标复用且需换色/悬停动画** -> 内联或 SVG sprite（CSS 可控）；**插画/大图一次出现** -> 外链 `<img>`（浏览器可缓存、不污染 DOM、可懒加载）。
- 内联的隐性成本：每个内联 SVG 都进 DOM 参与 style 计算，几百个内联图标会拖慢渲染；sprite + `<use>` 是折中（同文档引用、可换色、只占一个定义）。
- 动态色需求用 `currentColor` + CSS 变量，避免为换色生成多份文件。

```bash
# 一一对应：SVGO 优化流水线与配置
npm i -D svgo
# 单文件优化，保留 viewBox，精度 2 位（视觉无差，体积骤降）
npx svgo icon.svg -o icon.opt.svg \
  --precision=2 \
  --disable=removeViewBox \      # 保 viewBox：响应式缩放依赖它
  --enable=collapseGroups,mergePaths

# 构建期批量 + 产物报告：
# svgo -f assets/icons -o dist/icons --config svgo.config.js --multipass
```

```javascript
// svgo.config.js —— 白名单式插件配置（默认全开会破坏样式）
module.exports = {
  multipass: true, // 反复优化直到不再变小
  plugins: [
    'preset-default',
    { name: 'preset-default', params: {
      overrides: {
        removeViewBox: false,        // 关键保命项
        collapseGroups: false,       // 有 CSS 作用域依赖的组不合并
      },
    } },
    'convertStyleToAttrs',
    { name: 'removeAttrs', params: { attrs: '(data-name)' } },
  ],
};
```

```html
<!-- 一一对应：内联/外链/sprite 三种引用方式决策 -->
<!-- 决策 1：需要 CSS 换色的功能图标 -> sprite + use，只定义一份 -->
<svg style="display:none">
  <symbol id="i-heart" viewBox="0 0 24 24">
    <path d="M12 21c-5-4-9-7-9-11a5 5 0 0 1 9-3 5 5 0 0 1 9 3c0 4-4 7-9 11z" />
  </symbol>
</svg>
<svg class="icon"><use href="#i-heart" /></svg>

<!-- 决策 2：营销插画（大、一次性、无需交互）-> 外链 img，可缓存可懒加载 -->
<img src="illustration.svg" alt="活动插画" loading="lazy" decoding="async" />

<!-- 决策 3：首屏关键小图标（logo）-> 内联，省一次请求且随 DOM 渲染 -->
<svg class="logo" width="32" height="32" aria-hidden="true"><path fill="currentColor" d="..." /></svg>
<!-- 换色统一走 currentColor，不生成多份文件 -->
<style>
  .icon { color: #666; }
  .icon:hover { color: #1890ff; } /* sprite + currentColor：一次定义全局换色 */
</style>
```
