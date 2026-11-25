---
title: [H5-176] 屏幕阅读器测试怎么做？VoiceOver/NVDA 实操要点？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-176：屏幕阅读器测试怎么做？VoiceOver/NVDA 实操要点？
**答**：
- 工具：macOS **VoiceOver**（Cmd+F5 开启，VO+方向键逐元素导航，VO+A 全页朗读，VO+U 转子跳地标/标题/表单控件）；Windows **NVDA**（免费标准，Insert+方向键，NVDA+F7 元素列表）。
- 测试脚本：核心流程"**纯键盘 + 闭眼**"走一遍——能否知道焦点在哪、操作结果被播报了吗、错误提示能听到吗。
- 高频听感问题：图标按钮只读出"图形 147"、弹窗打开后焦点还在背景、动态内容无 aria-live 播报、装饰图读出文件名。
- 自动化只能覆盖 30~40% 静态问题（对比度/标签缺失），朗读体验必须真机听；文档化"读屏走查清单"纳入上线前检查。

```html
<!-- 无障碍自检清单 + 运行时自检桩：自动化查 30%，剩余靠真实读屏走查 -->
<img src="/chart.png"
     alt="2024 各季度销售额柱状图 Q1 120 万 Q2 150 万 Q3 130 万 Q4 180 万">
<!-- 坑 1：装饰图必须 alt=""，否则读屏读出文件名 -->

<label for="q">搜索</label><input id="q" type="search">
<!-- 坑 2：placeholder 不是 label；label 必须显式关联 -->

<div role="status" aria-live="polite" id="live"></div>
<!-- 坑 3：动态结果要 aria-live 播报，否则读屏用户不知道页面变了 -->

<script>
// 实操方法（答题主线）：
// 1) VoiceOver（macOS）：Cmd+F5 开启；VO+←/→ 逐元素导航；VO+A 连续朗读全页；
//    转子（VO+U）按地标/标题/表单控件跳转 —— 用来验证地标结构是否可用
// 2) NVDA（Windows 免费标准）：Insert+方向键；NVDA+F7 列出地标/标题/链接；
//    表单模式与浏览模式自动切换（focus 模式）
// 3) 测试脚本：核心流程"纯键盘 + 闭眼"走一遍，记录听感问题清单
// 4) 高频听感缺陷：图标按钮无 aria-label、弹窗焦点不进入、错误提示不播报

// 运行时快速自检（覆盖率有限，只是第一道网）
const issues = [];
document.querySelectorAll('img').forEach((img) => {
  if (!img.hasAttribute('alt')) issues.push({ type: 'img-alt', html: img.outerHTML });
});
document.querySelectorAll('input,select,textarea').forEach((el) => {
  const labeled = el.labels?.length || el.getAttribute('aria-label') ||
    el.getAttribute('aria-labelledby');
  if (!labeled) issues.push({ type: 'missing-label', html: el.outerHTML });
});
console.table(issues);
// 严谨方案见 H5-178：axe-core 规则引擎跑全量 WCAG 规则
</script>
```
