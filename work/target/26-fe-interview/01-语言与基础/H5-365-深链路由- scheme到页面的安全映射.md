---
title: [H5-365] 深链路由：scheme/deeplink 到页面的安全映射
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 路由]
type: 面试题
---

## H5-365：深链路由：scheme/deeplink 到页面的安全映射

**答**：
- 路由注册表：App 内维护「路径模式 → 页面/动作」映射（如 app://goods/:id → 商品页），H5 侧用统一 SDK 生成深链（app 内跳原生、浏览器内跳落地页或引导装 App）
- 降级链：App 已装 → scheme/deeplink 直达；未装/未响应 → Universal Link/App Link（域名校验直达）→ 落地 H5 → 引导下载——超时探测（约 500ms visibility 判断）决定降级
- 安全校验：深链参数必须白名单（防开放重定向/伪造订单）、动作类深链（支付/删除）必须登录 + 签名 + 二次确认；scheme 是公开协议任何页面都能调
- iOS Universal Link 要点：域名 root 放 apple-app-site-association JSON、HTTPS 必须、跨域跳转限制；Android App Links 要 assetlinks.json + 签名指纹
- 埋点归因：深链到达要区分「直达成功/降级 H5/引导安装」三条路径分别统计转化

```javascript
function openApp(path, params, fallbackH5) {
  const deep = `myapp://${path}?${new URLSearchParams(params)}`;
  const start = Date.now();
  location.href = deep;                                  // 尝试唤起
  setTimeout(() => {
    if (document.visibilityState !== 'hidden' && Date.now() - start < 2000) {
      // 未被 App 接管 → 降级
      location.href = fallbackH5 || `https://m.example.com/${path}`;
    }
  }, 800);
}
```
