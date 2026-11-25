---
title: [PER-399] 多语言站点的性能差异：字体/文本长度/RTL 布局对 CWV 的影响与分语言优化？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-399：多语言站点的性能差异：字体/文本长度/RTL 布局对 CWV 的影响？

**答**：
- 字体差异：中文/日文/韩文字体文件巨大（全字符集几 MB），必须子集化（unicode-range 按需分包）+ 度量对齐（PER-217）；阿拉伯语/泰语需要专门的渲染整形（文本整形成本高于拉丁语系）。分语言配置字体策略是必须项——用西欧策略服务 CJK 用户是 LCP/CLS 双杀。
- 文本长度差异：德语比英语长 30%+，同一布局在德语下换行/溢出 → 按语言设置布局余量（德语容器 +20% 宽度预算）；i18n key 的文案长度边界写进设计规范。
- RTL 布局：direction: rtl 的镜像布局渲染成本略高（布局方向翻转），且第三方组件（图表/日历）的 RTL 支持参差——RTL 页面单独做 CLS/LCP 验收，不假设 LTR 数据可平移。
- 度量与验收：RUM 按语言切片（Accept-Language/用户设置），各语言独立 SLO 与达标率；分语言 LCP 排行直接暴露"CJK 用户被默认策略拖累"的问题。

```javascript
// 分语言字体加载策略
const FONT_STRATEGY = {
  zh: { families: ['subset-zh'], unicodeRange: true, sizeAdjust: 1.05 },
  ar: { families: ['subset-ar'], direction: 'rtl' },
  en: { families: ['main'], systemFirst: true },        // 拉丁：系统字体优先，webfont 可选
};
const lang = navigator.language.slice(0, 2);
loadFontStrategy(FONT_STRATEGY[lang] ?? FONT_STRATEGY.en);
// RUM 按语言切片：lang × LCP p75 —— 德语 +30% 文本长度 → 布局余量校验
// RTL 页面独立 CLS 验收（direction: rtl 镜像布局的位移模式不同）
```
