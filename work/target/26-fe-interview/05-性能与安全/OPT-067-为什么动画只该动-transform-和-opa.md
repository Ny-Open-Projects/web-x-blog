---
title: [OPT-067] 为什么动画只该动 transform 和 opacity？例外情况怎么处理？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-067：为什么动画只该动 transform 和 opacity？例外情况怎么处理？

**答**：
- 渲染流水线：Layout → Paint → Composite；改 width/top 触发全流程，改 transform/opacity 只走 Composite（层已提升时），成本差一个数量级。
- transform/opacity 由 compositor 线程直接计算，**主线程卡住时动画依然流畅**，这是它们独有的优势。
- 例外场景：需要参与布局的动画（手风琴展开高度）、无法 transform 化的属性（颜色渐变是 Paint 但无 Layout）。处理方式：用 transform 近似（scaleY 模拟高度、clip-path 裁剪）或接受 Paint 成本但避免 Layout。
- 退化检查：动画期间用 Performance 面板确认没有绿色 Layout 块，有就说明属性选错了或层没建起来。

```css
/* 一一对应：布局动画改造为合成动画的常见替换 */
/* 例 1：菜单展开 height 动画（Layout+Paint）-> scaleY 近似（Composite） */
/* 反例：.menu { height: 0 -> 200px; transition: height .3s; } 每帧重排整页 */
.menu {
  transform: scaleY(0);
  transform-origin: top;
  transition: transform 0.3s;
}
.menu.open { transform: scaleY(1); }

/* 例 2：移动元素 left/top -> translate */
/* 反例：.slider { left: 0 -> 100px; } 全流程 */
.slider { transform: translateX(100px); transition: transform 0.3s ease; }

/* 例 3：无法 transform 的颜色渐变——接受 Paint，但隔离影响面 */
.badge { background: #aaa; transition: background 0.2s; } /* 无 Layout，可接受 */
.badge.active { background: #1890ff; }

/* 例外例外：scaleY 会拉伸内容，需要内容不变形时用 clip-path 裁剪显隐 */
.menu-clip {
  clip-path: inset(0 0 100% 0);
  transition: clip-path 0.3s;
}
.menu-clip.open { clip-path: inset(0 0 0% 0); } /* 同为合成属性，内容不形变 */

/* 验证方法：Performance 录制动画，Main 轨道应基本空、Frames 全绿；
   若每帧出现 Layout，回到属性清单排查 width/height/top/left/margin */
```
