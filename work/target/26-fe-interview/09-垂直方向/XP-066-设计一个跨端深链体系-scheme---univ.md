---
title: [XP-066] 设计一个跨端深链体系（scheme / universal link / 小程序码）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-066：设计一个跨端深链体系（scheme / universal link / 小程序码）？
**答**：
- 目标：一条**路由表达式**（页面+参数）在三端都能正确落地——App 内跳路由、冷启动 App（scheme/Universal Link/App Link）、H5 兜底（未装 App 落 H5）、小程序码拉起小程序。
- 协议设计：统一 `example://route?path=product%2F123&src=share` 或 universal link `https://m.example.com/app/product/123`（推荐后者：iOS Universal Link + Android App Links 复用 H5 域名，未装自动落网页）。
- 各端配置：iOS `apple-app-site-association`（AASA）+ `NSUserActivity`；Android `assetlinks.json` + intent-filter autoVerify；小程序 scene 参数解析 + 二维码生成（带参小程序码）。
- 归因与容错：点击→落地全链路埋点（哪个渠道码、是否首次安装）、延迟深链（装后首启恢复意图）、参数白名单防伪造。
- 收口：所有入口（分享卡片/推送/扫码/短信）都生成统一 DeepLink 对象，禁止散落拼 URL。

```json
// iOS：https://m.example.com/.well-known/apple-app-site-association
{
  "applinks": {
    "details": [{
      "appIDs": ["TEAMID.com.example.mall"],
      "components": [
        { "/": "/app/product/*", "comment": "商品详情" },
        { "/": "/app/live/*", "?": { "roomId": "?*" } },
        { "/": "/app/*", "exclude": true, "comment": "其余路径落 H5" }
      ]
    }]
  }
}
// Android：https://m.example.com/.well-known/assetlinks.json
// { "statement": [{ "relation": ["delegate_permission/common.handle_all_urls"],
//   "target": { "app": "com.example.mall", "sha256_cert_fingerprints": ["..."] } }] }
```

```typescript
// 统一 DeepLink 构建与解析（core，全端一致）
export function buildDeeplink(r: { path: string; params?: Record<string, string>; channel: string }) {
  const q = new URLSearchParams({ ...r.params, src: r.channel, t: String(Date.now()) }).toString();
  return {
    universal: `https://m.example.com/app/${r.path}?${q}`,   // iOS UL / Android App Links 首选
    scheme: `example://open?path=${encodeURIComponent(r.path)}&${q}`, // 仅 App 内/剪贴板兜底
    weappPath: `pages/entry/index?path=${encodeURIComponent(r.path)}&${q}`, // 带参小程序码
  };
}
export function parseLaunch(raw: string): RouteIntent {        // 冷启动统一入口（各端壳调用）
  const u = new URL(raw);
  const path = u.pathname.startsWith('/app/') ? u.pathname.slice(5) : u.searchParams.get('path')!;
  validateParamsWhitelist(u.searchParams);                    // 防参数伪造：白名单键+值格式校验
  return { path, params: Object.fromEntries(u.searchParams), scene: u.searchParams.get('src') };
}
// 未装 App：H5 落地页展示内容 + 唤起按钮（计时器尝试 scheme，失败即停留）+ 延迟深链（安装后首启带 cookie 匹配恢复意图）
```
