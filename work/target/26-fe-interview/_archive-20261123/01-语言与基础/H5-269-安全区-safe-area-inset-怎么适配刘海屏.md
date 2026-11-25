---
title: [H5-269] 安全区 safe-area-inset 怎么适配刘海屏
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## H5-269: 安全区 safe-area-inset 怎么适配刘海屏

**答**：
- 全屏模式（standalone/fullscreen 或 viewport-fit=cover）下内容会伸进刘海/底部横条区域，需要用 safe-area 内边距避让
- 两步配置：viewport meta 加 `viewport-fit=cover` 开启全屏绘制；CSS 用 env(safe-area-inset-top/right/bottom/left)
- 兼容写法：老版本 iOS 用 constant()，先写 constant 再写 env（级联覆盖）
- 典型应用：吸底操作栏 `padding-bottom: calc(env(safe-area-inset-bottom) + 12px)`；顶部导航避让刘海
- JS 读取：`env()` 无法直接读数值，需要时用 CSS 变量 + getComputedStyle 间接获取

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```
```css
.tabbar {
  padding-bottom: constant(safe-area-inset-bottom); /* iOS < 11.2 */
  padding-bottom: env(safe-area-inset-bottom);      /* 现行标准 */
}
```
