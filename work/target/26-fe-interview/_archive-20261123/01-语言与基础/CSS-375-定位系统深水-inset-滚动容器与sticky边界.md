---
title: [CSS-375] 定位系统深水：inset 语义、溢出裁剪与 sticky 边界
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-375：定位系统深水：inset 语义、溢出裁剪与 sticky 边界

**答**：
- inset 解析：绝对定位元素的 inset 相对包含块（最近定位祖先/transform 祖先/padding box），auto 值交还静态位置——「absolute 到底相对谁」取决于包含块判定链，一图记牢：transform > position > 初始包含块
- 溢出裁剪链：overflow: hidden 只裁「直接内容」，但定位元素的可见性取决于祖先链上第一个建立裁剪上下文的元素——下拉菜单被远祖 hidden 裁掉是常见事故（要 escape：把菜单 portal 出去）
- sticky 双边界：相对最近滚动祖先吸附 + 受父容器约束（父容器滚出就跟着走）——「sticky 不吸」三大原因：父容器 overflow 非 visible、父容器高度太短、中间有 transform 祖先
- 宽高 auto 行为：absolute + inset 双向约束（left/right 都设）会拉伸元素（配合 margin:auto 居中）——经典居中法；相对尺寸百分比基于包含块
- 诊断流程：DevTools 悬停元素看 containing block 高亮；滚动吸顶失效按「包含块→overflow→高度」三步排查

```css
/* 居中法: 双向 inset + auto margin */
.center { position: absolute; inset: 0; margin: auto; width: 200px; height: 100px; }
/* sticky 失效修复 */
.scroll-area { overflow: auto; }             /* 滚动祖先 */
.sticky-head { position: sticky; top: 0; }   /* 父级不能是 overflow:hidden */
```
