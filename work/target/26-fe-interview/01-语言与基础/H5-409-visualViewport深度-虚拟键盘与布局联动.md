---
title: [H5-409] visualViewport 深度：虚拟键盘与布局联动
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 适配]
type: 面试题
---

## H5-409：visualViewport 深度：虚拟键盘与布局联动

**答**：
- visualViewport 是「实际可见视口」：键盘弹出/浏览器 UI 收缩都会改变它的 height/offsetTop/offsetLeft——比 window.innerHeight 更真实地反映用户可见区域
- 键盘高度估算：window.innerHeight - visualViewport.height ≈ 键盘高度；配合 `interactive-widget` viewport meta（Chrome 108+：resizes-content 让布局自动缩、resizes-visual 只动视觉视口）控制键盘行为
- 联动模式：fixed 底部输入栏在键盘期要用 visualViewport 坐标定位（keyboard inset），而不是 fixed bottom 0（会被键盘盖住或漂移）
- 缩放感知：用户双指缩放时 scale 变化，可视坐标换算要乘 scale——做「贴屏悬浮球」这类精细定位必须处理
- 监听节流：resize/scroll 事件高频，rAF 合并处理；iOS 上 resize 时机有时滞后，关键布局再补 focus 事件兜底

```javascript
const vv = window.visualViewport;
function placeInputBar() {
  const kbInset = window.innerHeight - vv.height;
  const y = vv.offsetTop + vv.height;              // 可视区底部坐标
  bar.style.transform = `translateY(${y - window.innerHeight}px)`;
  bar.style.bottom = `${kbInset + vv.offsetTop}px`;
}
const onVV = () => requestAnimationFrame(placeInputBar);
vv.addEventListener('resize', onVV);
vv.addEventListener('scroll', onVV);
```

```html
<!-- Chrome 键盘行为控制 -->
<meta name="viewport" content="width=device-width, interactive-widget=resizes-content">
```
