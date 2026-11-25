---
title: [WCN-938] 大量 var() 嵌套的 token 样式重算成本怎么量化与优化
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-938：大量 var() 嵌套的 token 样式重算成本怎么量化与优化

**答**：
- 结论先行：CSS 变量的解析在样式计算阶段完成，深层嵌套（var 套 var）会放大依赖传播——改一个底层变量可能让大量元素的样式重算，成本随「引用它的元素数 × 嵌套深度」增长。
- 量化手段：用 Chrome DevTools Performance 的 Recalculate Style 看耗时，或 PerformanceObserver 观测 long task；实验室里构造 1万节点 + 多层 var 对比扁平化的耗时。
- 优化一：编译期把 alias 展开为扁平变量（少一层 var 解析），或直接内联为字面量（牺牲运行时换主题能力）。
- 优化二：缩小变量作用域——把高频变化的 token 定义在尽可能靠近使用元素的容器上，避免挂 :root 牵动全树重算（大促换肤场景）。
- 追问钩子：面试官问「内联字面量后还能动态换主题吗」——答：不能，所以按.token稳定性分层——稳定的间距/圆角内联，需换主题的颜色保留变量。

```javascript
// 量化：构造 1w 节点比较嵌套 var 与扁平 var 的样式重算（示意）
function bench(n, depth) {
  const el = document.createElement('div');
  let decl = '--c0:#1677ff;';
  for (let i = 1; i <= depth; i++) decl += `--c${i}:var(--c${i - 1});`;
  el.style.cssText = decl;
  let html = '';
  for (let i = 0; i < n; i++) html += `<span style="color:var(--c${depth})">x</span>`;
  el.innerHTML = html;
  document.body.appendChild(el);
  const t0 = performance.now();
  el.style.setProperty('--c0', '#f00');   // 触发全树依赖重算
  const cost = performance.now() - t0;
  el.remove();
  return cost;
}
console.log('嵌套5层耗时(ms):', bench(10000, 5).toFixed(2));
```
