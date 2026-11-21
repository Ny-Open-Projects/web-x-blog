---
title: [CSS-197] 绘制像素级 UI（设计稿还原）的 checklist 有哪些？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-197：绘制像素级 UI（设计稿还原）的 checklist 有哪些？

**答**：
- 基准换算统一：确定设计稿宽度与换算系数（rem 基准或 vw 公式），全项目一个换算入口，禁止手算散落。
- 文字三要素逐项核对：font-size/line-height/letter-spacing 用标注值，行高不靠 padding 凑。
- 色值与阴影取 token：圆角、阴影、渐变逐档比对 token 表，禁止目测近似。
- 验收手段：DevTools 盒模型对照标注、临时 outline 描边查对齐、四档分辨率截图比对。

```css
/* 1. 换算入口唯一：375 稿，html font-size = 100 * (100vw / 375)，1rem = 100px */
/* 根字号由脚本或 vw 设置：html { font-size: 26.67vw } 并在 768px 以上钳制 */

/* 2. 文字按标注三要素 */
.title {
  font-size: 16px;
  line-height: 24px;       /* 标注 24px，不用 padding 凑 */
  letter-spacing: .2px;
}

/* 3. 视觉细节走 token，逐档核对 */
.card {
  border-radius: var(--radius-md);      /* 8px，与标注一致 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, .08);
  background: linear-gradient(180deg, #fff 0%, #fafafa 100%);
}

/* 4. 调试描边：对齐误差 1px 内可定位到具体元素 */
.debug-outline * { outline: 1px solid rgba(255, 0, 0, .2); }

/* 5. 验收分辨率档位：375 / 414 / 768 / 1280 各截一图比对 */
```
