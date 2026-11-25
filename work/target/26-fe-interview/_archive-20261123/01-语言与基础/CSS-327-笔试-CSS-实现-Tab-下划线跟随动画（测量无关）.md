---
title: [CSS-327] 笔试：Tab 下划线跟随动画（不测量）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-327：笔试：Tab 下划线跟随动画（不测量宽度）

**题目**：Tab 栏选中态下划线平滑滑动到新 Tab：不用 JS 测量 offsetLeft/width（Tab 宽度不等时也要正确）。给两种方案。

**答**：
```css
/* 方案一：下划线放在每个 label 上，用「当前项的 ::after 从 0 过渡到 1」
   ——交叉淡入代替滑动（宽度不等时最稳） */
.tab label { position: relative; padding: 12px 20px; }
.tab label::after {
  content: '';
  position: absolute; bottom: 0; left: 20%; right: 20%;
  height: 2px; background: #4285f4;
  transform: scaleX(0); transform-origin: center;
  transition: transform .25s;
}
.tab input:nth-child(1):checked ~ nav [for='t1']::after { transform: scaleX(1); }
.tab input:nth-child(2):checked ~ nav [for='t2']::after { transform: scaleX(1); }
.tab input:nth-child(3):checked ~ nav [for='t3']::after { transform: scaleX(1); }

/* 方案二：独立滑块 + 按索引 translate（需要等宽或分档宽度） */
.tabs { position: relative; }
.indicator {
  position: absolute; bottom: 0; left: 0;
  height: 2px; background: #4285f4;
  transition: transform .3s, width .3s;
}
.tab input:nth-child(1):checked ~ .indicator { transform: translateX(0);   width: 60px; }
.tab input:nth-child(2):checked ~ .indicator { transform: translateX(60px); width: 80px; }
```

**评分点**：
- 认识到「滑块位移方案」要求已知各 Tab 宽度——不等宽时的误差
- scaleX 交叉淡入方案与宽度无关（通用解）
- transform-origin 对 scaleX 滑入方向的影响
- 方案二里 width 与 transform 同步过渡
