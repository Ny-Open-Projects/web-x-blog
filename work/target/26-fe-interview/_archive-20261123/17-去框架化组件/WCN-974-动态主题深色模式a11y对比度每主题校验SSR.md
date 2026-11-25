---
title: [WCN-974] 动态主题下 a11y 风险：深色模式怎么保证对比度仍达标
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-974：动态主题下 a11y 风险：深色模式怎么保证对比度仍达标

**答**：
- 结论先行：主题切换会改变前景/背景组合，light 下合格的对比度在 dark 下可能不达标——a11y 校验必须按「每套主题 × 每对语义 token」分别跑，不能只测默认主题。
- 做法：把成对的语义组合（text.primary/bg.page、text.inverse/bg.brand）列为校验清单，对每个主题计算 WCAG 对比度，CI 卡门禁（前文对比度算法可复用）。
- SSR 场景：服务端根据 prefers-color-scheme 输出对应主题的 token 与 markup，首屏即是无障碍配色，不能等 hydration 后再切换导致「先亮后暗」的对比度突变。
- 用户自定义主题：允许用户覆盖 token 时，覆盖层也要过对比度校验，不合格拒绝并提示（设计系统主题市场常见）。
- 追问钩子：面试官问「渐变/图片背景怎么校验」——答：按最差色标或给背景叠加半透明蒙层保证前景对比度，或标记为需人工复核。

```javascript
// 按主题校验语义配对的对比度
const themes = {
  light: { 'text.primary': '#1f1f1f', 'bg.page': '#ffffff' },
  dark:  { 'text.primary': '#f5f5f5', 'bg.page': '#1f1f1f' },
};
function lum(hex){const c=hex.replace('#','').match(/../g).map(x=>parseInt(x,16)/255)
  .map(v=>v<=.03928?v/12.92:((v+.055)/1.055)**2.4);return .2126*c[0]+.7152*c[1]+.0722*c[2];}
function contrast(a,b){const[l1,l2]=[lum(a),lum(b)].sort((x,y)=>y-x);return +((l1+.05)/(l2+.05)).toFixed(2);}
for (const [t, v] of Object.entries(themes))
  console.log(t, contrast(v['text.primary'], v['bg.page']) >= 4.5 ? 'AA 通过' : '不达标');
// light 通过，dark 通过
```
