---
title: [H5-280] H5 唤起 App 的方案：URL Scheme/Universal Link/App Link
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## H5-280：H5 唤起 App 的方案：URL Scheme、Universal Link、App Link

**答**：
- URL Scheme：`myapp://page?id=1` 直接拉起，最古老；缺点——未安装时浏览器报错/无反应、iOS 已限制非 https 上下文使用
- Universal Link（iOS）/App Link（Android）：https 域名关联校验（apple-app-site-association / assetlinks.json），点链接无 App 则正常打开网页——体验最优
- 时序检测：scheme 方案下用 setTimeout 与 visibilitychange 判断「是否成功拉起」，超时跳下载页
- 实际工程：双引擎（scheme 兜底 + universal/app link 优先），配合「引导页」模式（提示打开 App 或下载）
- 面试钩子：iOS 的 universal link 要在用户与页面交互后触发才生效，iframe 自动跳已失效

```javascript
function openApp(path, fallback) {
  const start = Date.now();
  const onLeave = () => document.removeEventListener('visibilitychange', onLeave);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) onLeave(); // 成功拉起，页面隐藏
  });
  location.href = `myapp://${path}`;
  setTimeout(() => { if (!document.hidden) fallback?.(); }, 2500);
}
```
