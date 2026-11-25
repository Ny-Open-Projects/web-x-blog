---
title: [CSS-222] anchor positioning 锚点定位是什么：弹层新方案
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 组件]
type: 面试题
---

## CSS-222：anchor positioning 锚点定位是什么：弹层新方案

**答**：
- CSS Anchor Positioning：声明式「把 A 定位到 B 旁边」——tooltip/popover/下拉的定位不再需要 JS 计算
- 三步：锚点元素 `anchor-name: --anchor`；弹层 `position-anchor: --anchor`；位置 `position: anchor(--anchor bottom)` 或 inset-area（九宫格区域）
- 自动翻转：`position-try-fallbacks: flip-block, flip-inline`——空间不足自动换方向，替代 JS 的 flip 逻辑
- 与 Popover API 天然组合：popover 进 top layer 后仍锚定触发按钮
- 兼容：Chromium 125+，Safari/Firefox 推进中；JS 库（floating-ui）仍是兼容兜底

```css
.btn { anchor-name: --btn; }
.tip {
  position: fixed;
  position-anchor: --btn;
  bottom: anchor(top);        /* 贴锚点上方 */
  left: anchor(center);
  position-try-fallbacks: flip-block; /* 上方没空间自动翻到下方 */
}
```
