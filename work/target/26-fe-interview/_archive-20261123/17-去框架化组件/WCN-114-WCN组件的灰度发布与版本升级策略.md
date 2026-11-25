---
title: [WCN-114] WCN 组件如何做灰度发布与版本升级？CDN 分发、加载器与回滚怎么做？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-114：WCN 组件如何做灰度发布与版本升级？CDN 分发、加载器与回滚怎么做？

**答**：
- 分发形态：组件产物传 CDN（`/acme/wc/button/1.4.2/button.js`），语义化版本 + immutable 缓存；宿主用加载器按版本解析 URL。
- 灰度：加载器查询灰度配置（按用户/渠道分流）决定加载版本（v1.4.2 → 10% 用户 v1.5.0-beta）；同一 tag 不同版本共存用 tag 后缀或加载器隔离（不同 runtime 不冲突）。
- 升级兼容：attribute/事件 API 的 breaking 变化必须换 tag 或加迁移层——WC 无法运行时探测 API 版本，契约靠 manifest 版本声明。
- 回滚：加载器配置回切版本号即可（无需重新发宿主包）；组件自报错误（`window.__wcErrors` 或埋点 SDK）触发自动熔断到稳定版。
- 安全：CDN 产物加 SRI hash + CSP 白名单域名；跨域 module 需要 CORS 头。

```javascript
// 加载器：灰度 + 回滚收口
const REGISTRY = {
  'acme-button': { stable: '1.4.2', beta: '1.5.0-beta.3' },
};
async function loadWc(tag) {
  const { stable, beta } = REGISTRY[tag];
  const useBeta = await grayGate(tag, beta);       // 灰度配置中心
  const version = useBeta ? beta : stable;
  const url = `https://cdn.acme.com/acme/wc/${tag}/${version}/${tag}.js`;
  try {
    await import(url);
  } catch (e) {
    reportError(tag, version, e);
    if (version !== stable) await import(stableUrl(tag, stable)); // 熔断回滚
  }
}
```
