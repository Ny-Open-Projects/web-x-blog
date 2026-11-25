---
title: [H5-260] 加桌面快捷方式与 Web App 的显示模式
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-260：加桌面快捷方式与 Web App 的显示模式

**答**：
- display 四档：browser（普通网页）→ minimal-ui（去地址栏）→ standalone（像独立 App，最常用）→ fullscreen（全屏，游戏/视频）
- 运行时检测：`display-mode: standalone` 媒体查询判断「是否以 App 形态运行」，用于隐藏浏览器专属 UI 或调整导航逻辑
- iOS 特殊：Safari 添加到主屏幕走 apple-* meta 标签（apple-mobile-web-app-capable），不支持完整 manifest display
- 窗口控制：desktop PWA 的 `window-controls-overlay` 显示模式让 PWA 占据标题栏区域，配合 CSS env 变量排版
- 坑：standalone 模式没有浏览器导航，站内必须自建「返回」逻辑，外链要 `target="_blank"` 或引导到系统浏览器

```css
@media (display-mode: standalone) {
  .browser-only-banner { display: none; } /* App 形态下隐藏提示 */
}
```
```javascript
const isStandalone = matchMedia('(display-mode: standalone)').matches;
report({ installed: isStandalone });
```
