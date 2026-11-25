---
title: [RBL-803] 场景题：内部数据看板的 SSR 产物策略——权限敏感数据与构建边界
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-803：场景题：内部数据看板的 SSR 产物策略——权限敏感数据与构建边界

**答**:
- 内部看板（权限敏感数据）的 SSR 构建要点：1) **数据不出产物**——预渲染（SSG）对权限数据是禁区（预渲染 HTML 含具体数据 = 泄漏给未授权用户）；产物只含「渲染框架 + 组件」，数据全部请求时获取；2) SSR 数据获取的权限检查在 server bundle（session 校验），client bundle 不含权限逻辑（RBL-780 边界审查）。
- 缓存策略的构建配合：看板页面不可 CDN 缓存（每用户数据不同）——产物 manifest 标记 dynamic 角色（RBL-618 缓存策略生成器的 no-store 类）；但「壳资源」（框架 JS/CSS）仍可长缓存——「数据动态、壳静态」的分层缓存。
- SSR bundle 的 external 策略（RBL-604）：node_modules 全外置 + 镜像瘦身（RBL-681）——看板服务是常驻进程，启动速度依赖 external 策略（node 直接 require 比 bundle 解析快）。
- 安全审计的专项：看板 SSR 产物审计「SQL/查询语句模板泄漏」（server bundle 里硬编码的查询可以被错误日志带出）——诊断级别 warn + 建议参数化。
- 追问钩子：为什么「预渲染 + 权限」的组合是 SSR 的经典事故？——SSG 在构建时以「某个身份」执行数据获取（构建机的 session），产出的 HTML 是那个视角的数据；发布后所有用户（包括未授权的）拿到这份 HTML——数据越权不需要攻击，打开页面就发生；构建期数据内联进产物是权限系统的大忌。

```javascript
// 看板构建配置
export default {
  ssr: {
    external: 'all-node',                                // node_modules 外置（RBL-604）
    noPrerender: true,                                   // 权限数据禁止预渲染
  },
  cache: {
    html: { policy: 'no-store' },                        // 页面 HTML 不缓存
    assets: { policy: 'immutable' },                     // 壳资源长缓存
  },
};
// SSR 数据获取（server bundle 内）
export async function loader(req) {
  const session = await auth(req);                       // 权限检查在 server 侧
  if (!session.canView('revenue'))
    return new Response('Forbidden', { status: 403 });
  return fetchDashboardData(session);                    // 数据按权限裁剪
}
// 构建期审计
auditRSCBoundary(graph);                                  // 密钥/权限逻辑不进 client（RBL-780）
```
