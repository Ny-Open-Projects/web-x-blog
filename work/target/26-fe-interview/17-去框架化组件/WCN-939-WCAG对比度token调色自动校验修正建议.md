---
title: [WCN-939] WCAG 对比度约束下 token 调色：自动校验并给出修正建议
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-939：WCAG 对比度约束下 token 调色：自动校验并给出修正建议

**答**：
- 结论先行：token 里的前景/背景组合要满足 WCAG——正文 ≥4.5:1、大字 ≥3:1；靠人工目测不可靠，应在提交 token 时用算法自动算对比度并卡门禁。
- 算法：把 sRGB 转线性亮度（每个通道 /255 后做 gamma 反变换），对比度 = (L亮+0.05)/(L暗+0.05)。
- 修正建议：不合格时固定背景、沿 HSL 亮度轴逐步调暗前景直到达标，或反过来提亮背景；给出达标的最近色值供设计师选择。
- 结合语义：不是所有 token 都要互配——只校验语义上成对的组合（text.primary over bg.page、text.inverse over brand），避免组合爆炸。
- 追问钩子：面试官问「透明色/渐变背景怎么算」——答：rgba 要先与预期底色合成得到实际色再算；渐变按最差色标校验，或标记人工复核。

```javascript
// WCAG 对比度计算 + 修正建议
function lum(hex) {
  const c = hex.replace('#', '').match(/../g).map(x => parseInt(x, 16) / 255)
    .map(v => v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4);
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
}
function contrast(a, b) {
  const [l1, l2] = [lum(a), lum(b)].sort((x, y) => y - x);
  return +((l1 + 0.05) / (l2 + 0.05)).toFixed(2);
}
console.log(contrast('#1f1f1f', '#ffffff')); // 约 16.5（AA 通过）
console.log(contrast('#888888', '#ffffff')); // 约 3.5（正文不通过）
function check(fg, bg, need = 4.5) {
  const r = contrast(fg, bg);
  return r >= need ? { ok: true, ratio: r } : { ok: false, ratio: r, hint: '需调暗前景或提亮背景' };
}
console.log(check('#888', '#fff'));
```
