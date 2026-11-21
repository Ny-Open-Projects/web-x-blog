---
title: [CSS-322] 笔试：CSS 点赞爱心爆炸粒子
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-322：笔试：点赞爱心爆炸粒子

**题目**：点击爱心后：爱心放大消失，周围 8 个小粒子向四周飞散淡出。要求角度均匀分布、每次点击可重复触发（class 重置技巧）。

**答**：
```css
.like { position: relative; font-size: 32px; cursor: pointer; user-select: none; }
.like.liked { animation: pop .4s ease-out forwards; }
@keyframes pop {
  40% { transform: scale(1.3); }
  100% { transform: scale(1); }
}

.particle {
  position: absolute; top: 50%; left: 50%;
  font-size: 10px; opacity: 0;
  pointer-events: none;
}
.liked .particle { animation: fly .6s ease-out forwards; }
/* 8 个粒子均匀角度：rotate 定方向 + translate 定距离 */
.particle:nth-child(1) { --r: 0deg; }   .particle:nth-child(2) { --r: 45deg; }
.particle:nth-child(3) { --r: 90deg; }  .particle:nth-child(4) { --r: 135deg; }
.particle:nth-child(5) { --r: 180deg; } .particle:nth-child(6) { --r: 225deg; }
.particle:nth-child(7) { --r: 270deg; } .particle:nth-child(8) { --r: 315deg; }
@keyframes fly {
  0%  { opacity: 1; transform: rotate(var(--r)) translateY(0) scale(.6); }
  100%{ opacity: 0; transform: rotate(var(--r)) translateY(-48px) scale(1); }
}
```
```javascript
// 重复触发：移除 class 后强制 reflow 再加回
btn.onclick = () => {
  btn.classList.remove('liked');
  void btn.offsetWidth; // 强制 reflow，重置动画
  btn.classList.add('liked');
};
```

**评分点**：
- CSS 变量 --r 存角度，rotate + translateY 组合出「放射」轨迹
- nth-child 均匀 45° 分布
- 「reflow 重置动画」技巧（void offsetWidth）——重复触发的关键
- 两段动画（爱心 pop + 粒子 fly）时序协调
