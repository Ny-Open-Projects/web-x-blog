---
title: [H5-155] visualViewport 如何解决软键盘遮挡输入框？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-155：visualViewport 如何解决软键盘遮挡输入框？
**答**：
- `window.visualViewport` 暴露"可见视口"的 `offsetTop/height/scale` 及 `resize/scroll` 事件；键盘弹出时 layout viewport 不变（iOS）但可见视口变小。
- 键盘高度近似 = `window.innerHeight - vv.height`；把输入区用 transform 平移到可见视口底部，同时处理 `vv.offsetTop`（页面在可视窗口内滚动）。
- iOS 键盘不改变 layout viewport，`position: fixed` 元素会被遮——这是与安卓最大的差异；安卓多数会 resize layout viewport。
- 两个防御：`vv.scale > 1`（双指缩放）时跳过调整避免误判；事件防抖。兜底方案：focus 时 `scrollIntoView({block:'center'})`。

```html
<div class="input-bar" id="bar"><input placeholder="聊一句…"></div>
<style>
  .input-bar { position: fixed; left: 0; right: 0; bottom: 0;
               background: #fff; padding: 8px; border-top: 1px solid #eee; }
</style>
<script>
// visualViewport：键盘弹出后"真正可见"的区域
const vv = window.visualViewport;
const bar = document.getElementById('bar');

function layout() {
  if (!vv) return;
  if (vv.scale > 1) return;                 // 双指缩放时跳过，避免误判键盘
  // 键盘高度 ≈ layout viewport 高度 - 可见视口高度
  const keyboard = Math.max(0, window.innerHeight - vv.height);
  // iOS：fixed 元素相对 layout viewport，会被键盘盖住 → 平移补偿
  bar.style.transform =
    `translateY(${-(keyboard + vv.offsetTop)}px)`;
}
vv?.addEventListener('resize', layout);     // 键盘弹收
vv?.addEventListener('scroll', layout);     // 页面在可视窗口内滚动
window.addEventListener('resize', layout);  // 兜底：安卓上 window 也变
layout();

// 平台差异（答题要点）：
// 1) iOS 键盘不改变 window.innerHeight / layout viewport → position:fixed 被遮
// 2) Android 多数会 resize layout viewport → window resize 就能处理
// 3) visualViewport 是统一答案，但要同时监听 resize/scroll 且防抖
// 兜底方案：输入框 focus 时 scrollIntoView({ block: 'center' })，简单可靠
</script>
```
