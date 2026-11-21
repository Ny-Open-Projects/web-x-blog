---
title: [MFW-208] 多租户主题定制：运行时 vs 构建期两种方案
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-208：多租户主题定制方案

**答**:
- 运行时方案：租户主题（CSS 变量/logo/文案）在租户 layout 加载时下发——一套产物服务所有租户，灵活但首屏多一次主题请求（CSS 注入防闪）
- 构建期方案：白标产物（每租户一构建，DefinePlugin 注入品牌）——首屏零额外请求、产物体积最小，但租户数量大时构建矩阵爆炸
- 混合策略：大租户（SLA 客户）构建期定制 + 小租户运行时主题——按租户分级是现实解
- 主题内容分层：样式类（CSS 变量）运行时；结构性差异（不同组件树）构建期或组件级条件渲染

```javascript
// 运行时主题（layout 注入，CSS 变量）
export default async function TenantLayout({ params, children }) {
  const theme = await getTenantTheme(params.tenant)
  return (
    <div style={{ '--brand': theme.color }} data-theme={theme.mode}>
      <style>{`:root{--brand:${theme.color}}`}</style>      {/* 防闪：SSR 内联 */}
      {children}
    </div>
  )
}
```
