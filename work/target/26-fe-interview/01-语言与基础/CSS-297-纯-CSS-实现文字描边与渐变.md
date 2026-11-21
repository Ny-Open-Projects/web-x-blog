---
title: [CSS-297] 纯 CSS 文字描边与渐变
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 效果]
type: 笔试题
---

## CSS-297：纯 CSS 文字描边与渐变

**题目**：实现：① 描边文字（外描边、填充色不变）② 描边镂空文字（透明填充）③ 渐变描边。说明各方案的兼容性。

**答**：
```css
/* 方案一：-webkit-text-stroke（描边居中于字形边缘，加粗视觉变细） */
.stroke {
  -webkit-text-stroke: 2px #333;          /* 描边 */
  color: #fff;                             /* 填充色 */
}
/* 镂空：填充透明 */
.hollow {
  -webkit-text-stroke: 2px #4285f4;
  color: transparent;
}

/* 方案二：text-shadow 多向堆叠（兼容性最好，描边在外侧） */
.stroke-shadow {
  color: #fff;
  text-shadow:
    2px 0 0 #333, -2px 0 0 #333,
    0 2px 0 #333, 0 -2px 0 #333,
    2px 2px 0 #333, -2px 2px 0 #333,
    2px -2px 0 #333, -2px -2px 0 #333;
}

/* 方案三：渐变描边（双层，背景剪裁+父层填充） */
.gradient-stroke { position: relative; color: #fff; }
.gradient-stroke::before {
  content: attr(data-text);
  position: absolute; inset: 0;
  -webkit-text-stroke: 4px transparent;
  background: linear-gradient(90deg, #4285f4, #ea4335);
  -webkit-background-clip: text;
  color: transparent;
  z-index: -1;
}
```

**评分点**：
- text-stroke 是「中心描边」（线宽一半吃进字形），text-shadow 是「外描边」——语义差异
- 镂空 = stroke + transparent 填充
- 渐变描边的双层结构（::before 用 background-clip: text 做彩色描边）
- 兼容性陈述：text-stroke 全主流（带前缀）、shadow 万能但代码多
