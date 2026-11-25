---
title: [H5-106] ARIA 规则总纲是什么？无障碍树如何由 DOM 计算而来？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-106：ARIA 规则总纲是什么？无障碍树如何由 DOM 计算而来？
**答**：
- 无障碍树（Accessibility Tree）= 浏览器把 DOM + CSS 显示状态（display:none 剔除、visibility:hidden 部分保留语义）翻译成读屏可用的"角色-名称-状态"树；ARIA 是人工修正这棵树的手段。
- 第一规则：**能用原生元素就不用 ARIA**——原生 button 自带 role/键盘/焦点语义，`<div role="button" tabindex="0">` 要手工补齐所有行为。
- 五大规则：role 不改变原生语义的场合别乱用（li 上加 role 破坏列表）；所有交互组件必须有可编程的名称（aria-label/labelledby）；状态用 aria-expanded/pressed/current 动态维护；可见性变化必须让读屏感知（focus/live region）；不要用 aria-hidden 藏可聚焦元素。
- 命名优先级：`aria-labelledby` > `aria-label` > 原生 label > 内容文本；`aria-hidden="true"` 只对无障碍树隐藏，仍可被聚焦（所以必须配合 tabindex=-1）。
- 验证工具：DevTools 无障碍面板、axe、Lighthouse，最终以真实读屏（VoiceOver/NVDA）走查为准。

```html
<!-- 反例：div 假按钮，读屏不知道它可点击、Tab 键够不到 -->
<div class="btn" onclick="save()">保存</div>

<!-- 正例：原生 button 一行顶三行 -->
<button onclick="save()">保存</button>

<!-- 确需 ARIA 的场景：自绘开关组件，补齐角色-状态-名称-键盘 -->
<div role="switch"
     class="switch"
     tabindex="0"
     aria-checked="false"
     aria-label="接收营销邮件"
     data-on="false">
  <span class="knob"></span>
</div>

<script>
  const sw = document.querySelector('.switch');
  function toggle() {
    const on = sw.getAttribute('aria-checked') === 'true';
    sw.setAttribute('aria-checked', String(!on));   // 状态进无障碍树
    sw.dataset.on = String(!on);
  }
  sw.addEventListener('click', toggle);
  sw.addEventListener('keydown', (e) => {           // ARIA 只补语义，行为要自己写
    if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); toggle(); }
  });
</script>

<script>
  // 用 JS 观察无障碍树变化（Chromium DevTools 协议示意）：
  // aria-hidden 藏装饰图标，避免读屏噪音
  document.querySelectorAll('.icon-decorative')
    .forEach(el => el.setAttribute('aria-hidden', 'true'));
</script>
```
