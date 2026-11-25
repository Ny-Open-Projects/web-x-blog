---
title: [WEB-092] will-change 怎么用才正确？滥用的后果是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-092：will-change 怎么用才正确？滥用的后果是什么？
**答**：
- 设计意图：提前告知浏览器"这个元素的某属性即将变化"，让浏览器预先分配合成层与优化路径。
- 正确用法：动画开始前加、动画结束后移除，让资源可回收；只声明将要变化的那个属性，不要 `all`。
- 滥用后果一：大量元素常驻成层，内存按层数线性膨胀；后果二：层合成与纹理上传本身有成本，层数过多反而更卡。
- 经验法则：连续两次都观察到的卡顿才值得用 will-change 修复；一次性的状态切换交给 transition/浏览器自动优化。

```html
<style>
  .card { transition: transform .3s ease; }
  .card.will-move { will-change: transform; }  /* 只声明真正会变的属性 */
</style>
<div class="card">内容</div>
<script>
  const card = document.querySelector('.card');
  card.addEventListener('mouseenter', () => {
    card.classList.add('will-move');   // 动画前提升
    card.style.transform = 'translateY(-4px)';
  });
  card.addEventListener('transitionend', () => {
    card.classList.remove('will-move'); // 结束后释放，避免常驻占内存
    card.style.transform = '';
  });
</script>
```
