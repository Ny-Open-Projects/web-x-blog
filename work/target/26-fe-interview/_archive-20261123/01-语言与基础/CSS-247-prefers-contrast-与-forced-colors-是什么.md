---
title: [CSS-247] prefers-contrast 与 forced-colors 是什么
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 可访问性]
type: 面试题
---

## CSS-247：prefers-contrast 与 forced-colors

**答**：
- prefers-contrast: more/less/custom：用户要求更高/更低对比度——高对比模式下增强边框、加深文字
- forced-colors: active：系统强制色彩模式（Windows 高对比度），浏览器把颜色替换为系统配色——自定义颜色全部失效
- forced-colors 适配要点：颜色交给系统，但「视觉层次」要自己保——用 border/backdrop 等结构手段；forced-color-adjust: none 例外保留品牌色（如状态色）
- 两者常一起适配：高对比与强制色彩都是低视力用户的场景
- 检测清单：表单控件图标（系统模式下背景色消失，图标可能不可见）、状态指示不要只靠颜色

```css
@media (forced-colors: active) {
  .btn {
    border: 1px solid ButtonText;    /* 用系统语义色 */
    forced-color-adjust: none;        /* 品牌状态色保留 */
  }
}
@media (prefers-contrast: more) {
  .text-muted { color: #444; }        /* 减弱灰阶 */
}
```
