---
title: [ARC-074] SaaS 多租户的前端架构如何设计（主题/域名/功能开关）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-074：SaaS 多租户的前端架构如何设计（主题/域名/功能开关）？
**答**：
- 租户识别：域名映射（tenant-a.saas.com）为主、登录路径/子路径为辅，识别结果全局注入。
- 三层隔离：主题（CSS 变量 + 品牌 Token 运行时注入）、功能（Feature Flag 服务端下发）、路由与数据（租户 id 全局上下文，服务端强校验）。
- 架构关键：租户配置要有"平台默认 + 租户覆盖"的合并机制，白标部署不重新构建。

```typescript
// 多租户运行时装配：识别 → 合并配置 → 注入应用
interface TenantConfig {
  id: string;
  theme: Partial<typeof semantic>;        // 覆盖语义 Token：品牌色/logo/字体
  features: Record<string, boolean>;       // 功能开关：报表: true, 导出: false
  routes?: { hide?: string[]; add?: RouteConfig[] };
}

// 1. 域名识别
function resolveTenant(host: string): Promise<TenantConfig> {
  const sub = host.split('.')[0];                       // tenant-a.saas.com → tenant-a
  return api.get(`/tenants/${sub}/config`);             // 未识别 → 404 页
}

// 2. 平台默认 + 租户覆盖合并（浅合并约定，避免深合并失控）
const config = { ...defaultPlatformConfig, ...tenantConfig, features: { ...defaultFeatures, ...tenantConfig.features } };

// 3. 注入
applyTheme(config.theme);                                // CSS 变量运行时注入
provide(FeaturesKey, config.features);                   // <Feature flag="reports"> 组件消费
router.setRoutes(filterRoutes(baseRoutes, config));
// 服务端配套：所有 API 以 subdomain 解析 tenantId，前端传参不可信
```

---

## 九、SDK 与插件化架构（ARC-075 ~ ARC-087）
