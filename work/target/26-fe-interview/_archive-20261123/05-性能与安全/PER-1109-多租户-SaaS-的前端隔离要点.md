---
title: [PER-1109] 多租户 SaaS 的前端隔离要点
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1109：多租户 SaaS 的前端隔离要点

**答**：
- 数据隔离：接口按租户上下文（token 内含 tenant），前端缓存键必须含租户 ID 防串数据。
- 主题隔离：租户定制（logo/配色）加载来自租户配置域，防恶意租户注入脚本（CSS-only 定制，禁止自定义 JS）。
- 资源隔离：租户上传文件分桶 + 访问签名，前端直传用临时凭证（STS）限定路径前缀。
- 审计：跨租户操作（如平台管理员）单独留痕与提示。

```javascript
// 租户感知的缓存键
function cacheKey(tenant, key) { return `${tenant}:${key}`; }
function tenantGet(tenant, key, fetcher) {
  return apiCache.get(cacheKey(tenant.key, key), fetcher);
}
// 租户自定义主题：仅允许 CSS 变量与静态资源 URL 白名单
function applyTenantTheme(cfg) {
  const SAFE = /^https:\/\/static\.example\.com\//;
  if (!SAFE.test(cfg.logo)) throw new Error('非法资源地址');
  document.documentElement.style.setProperty('--logo', `url(${cfg.logo})`);
  for (const [k, v] of Object.entries(cfg.colors))
    document.documentElement.style.setProperty(k, v);   // CSS 变量注入安全
}
```
