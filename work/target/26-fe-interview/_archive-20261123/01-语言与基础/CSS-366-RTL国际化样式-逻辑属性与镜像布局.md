---
title: [CSS-366] RTL 国际化样式：逻辑属性与镜像布局
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-366：RTL 国际化样式：逻辑属性与镜像布局

**答**：
- 逻辑属性是正解：margin-inline-start/padding-block-end/inset-inline-start 替代 left/right——direction: rtl 时自动镜像，无需 RTL 专属样式表
- 旧方案对比：物理属性 + [dir='rtl'] 逐条覆盖（维护两份）vs postcss-rtlcss 自动转换（构建期）vs 逻辑属性（源头解决）——新代码一律逻辑属性
- 方向敏感家族：文本对齐 text-align: start/end、浮动 inset-inline、定位 inset-inline-start、阴影偏移（纯物理，RTL 需手动镜像或用对称阴影）、transform 位移（物理坐标不镜像）
- 图标与素材：箭头类图标要镜像（用 transform: scaleX(-1) [dir='rtl'] 或 SVG 自带逻辑方向）、阅读类插图镜像、logo 不镜像
- 混排文本：unicode-bidi/isolate 处理中英混排与数字方向，用户输入的 URL/代码块要 bdi 包裹防整段反转

```css
.card {
  margin-inline-start: 12px;          /* RTL 自动变右侧 */
  padding-inline: 16px;
  inset-inline-start: 0;
  text-align: start;
}
[dir='rtl'] .arrow { transform: scaleX(-1); }  /* 图标镜像 */
.url-field { unicode-bidi: plaintext; }        /* 输入内容方向自适应 */
```
