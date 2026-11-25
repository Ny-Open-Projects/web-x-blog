---
title: [H5-397] Android X5 内核特有坑清单与绕过方案
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 适配]
type: 面试题
---

## H5-397：Android X5 内核特有坑清单与绕过方案

**答**：
- 视频层级：X5 内核 video 默认接管为原生层（层级最高盖住 DOM），加 `x5-video-player-type="h5"` 走同层渲染；竖屏全屏要 x5-video-orientation
- 内核版本不确定：X5 版本由 App/腾讯服务下发，同一台设备可能突然升级——特性检测不能写死版本号，注意 X5 老版本的 ES 语法缺口
- 渲染差异：部分动画在 X5 上出现掉帧/错位（老版本 chromium 66 级），避免依赖最新 CSS 特性；border-radius + overflow hidden 组合易穿帮
- 下载与文件：X5 的下载行为有时不触发 blob 下载，用 a[download] + 服务端 Content-Disposition 双保险
- UA 与调试：X5 UA 带特定标识便于归因；真机调试用 X5 内核调试开关（debugx5.qq.com）开 TBS 调试

```html
<video x5-video-player-type="h5" x5-video-orientation="portrait"
       x5-playsinline playsinline webkit-playsinline></video>
```

```javascript
// X5 检测与降级
const isX5 = /MQQBrowser|TBS\/|X5/.test(navigator.userAgent);
if (isX5) {
  // 降级: 复杂动画用视频替代 / 关闭 backdrop-filter / 关键布局用稳态 CSS
  document.documentElement.classList.add('x5');
}
```
