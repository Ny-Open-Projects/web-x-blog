---
title: [H5-250] PWA 的安装条件，beforeinstallprompt 怎么接
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-250：PWA 的安装条件，beforeinstallprompt 怎么接

**答**：
- 浏览器判定「可安装」后发 beforeinstallprompt 事件，JS 拦截后自己决定何时展示「安装到桌面」按钮（替代浏览器默认弹条）
- 触发条件：HTTPS + 合法 manifest（含 name/icons/start_url/display）+ 注册了带 fetch handler 的 SW；且用户没装过、近期没拒绝
- 引导流程：保存 deferredPrompt → 业务时机（如完成首单）调 `prompt()` → 监听 appinstalled 事件确认安装成功
- iOS 没有 beforeinstallprompt：只能提示用户「分享 → 添加到主屏幕」，需检测 iOS 单独引导
- 数据价值：prompt 结果（accepted/dismissed）与 appinstalled 都要上报，评估安装转化率

```javascript
let deferredPrompt;
addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  showInstallBtn(); // 自己控制展示时机
});
installBtn.onclick = async () => {
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  report({ install: outcome }); // accepted / dismissed
  deferredPrompt = null;
};
```
