---
title: [OPT-106] CSS 动画和 JS 动画怎么选型？WAAPI 的位置在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-106：CSS 动画和 JS 动画怎么选型？WAAPI 的位置在哪？

**答**：
- 选型三问：要不要**中途交互**（暂停/变速/反向）？要不要**复杂时间轴**？要不要**逐帧计算**？——都不需要选 CSS（声明式、可合成、主线程阻塞时不掉帧）；需要精细控制选 WAAPI；需要逐帧逻辑（物理模拟）才用 rAF + JS。
- CSS 动画本质也在合成器上跑（transform/opacity 时），且 `animation-play-state`/CSS 变量能满足大部分"控制"需求，别低估它。
- WAAPI（Element.animate）是两者的桥：JS 编排 + 浏览器原生插值 + 可 `commitStyles`/`persist`，比 CSS 类切换好调试（有 Promise finish）。
- 通用原则：优先 CSS，复杂编排用 WAAPI，rAF 是最后手段——每帧 JS 回调是三者中最贵的。

```javascript
// 一一对应：三种动画方式的选型实现对照
// 选型 1：进场淡入 + 上移 —— CSS 即可（合成器执行，最便宜）
// .card { animation: fade-in .3s ease both; }
// @keyframes fade-in { from { opacity: 0; transform: translateY(12px); } }

// 选型 2：需要"完成后链式触发 + 可取消重播" —— WAAPI
function popIn(el) {
  const anim = el.animate(
    [
      { transform: 'scale(0.6)', opacity: 0 },
      { transform: 'scale(1)', opacity: 1 },
    ],
    { duration: 250, easing: 'cubic-bezier(0.2, 0.8, 0.2, 1)', fill: 'both' }
  );
  return anim.finished; // Promise 化：链式编排不用 setTimeout
}
// 重播与取消都是一等公民
// const a = popIn(el); a.cancel(); // 随时中断

// 选型 3：粒子跟随鼠标（逐帧物理计算）—— rAF 是唯一选项
let mouse = { x: 0, y: 0 };
document.addEventListener('pointermove', (e) => (mouse = { x: e.clientX, y: e.clientY }), { passive: true });
(function tick() {
  particles.forEach((p) => {
    p.vx += (mouse.x - p.x) * 0.001; // 物理逻辑必须每帧 JS
    p.x += p.vx;
  });
  render();
  requestAnimationFrame(tick);
})();

// 决策速查：
// 简单过渡/循环       -> CSS animation/transition
// 序列编排/等待完成    -> WAAPI（anim.finished 串接）
// 手势驱动/物理模拟    -> rAF + JS
// 反面：用 JS setInterval 改 style 做渐变 —— 全部缺点占齐
```
