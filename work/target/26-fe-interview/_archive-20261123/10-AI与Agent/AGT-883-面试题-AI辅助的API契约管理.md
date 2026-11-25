---
title: [AGT-883] 前后端接口契约（OpenAPI/schema）用 AI 辅助维护：同步与漂移检测？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-883：前后端接口契约（OpenAPI/schema）用 AI 辅助维护：同步与漂移检测

**答**：
- 契约单一来源：后端 OpenAPI 是唯一事实，前端类型从 schema 生成（openapi-typescript），AI 不得手写接口类型（手写必然漂移）——AI 的角色是「生成请求层样板+漂移解释」。
- 漂移检测：CI 里 schema diff（后端改了字段→前端类型再生成→编译报错定位到受影响代码），AI 产出"该变更影响哪些调用点+适配建议"。
- 契约测试补位：MSW mock 从 schema 生成（AI 补充 realistic 数据），前端不依赖后端环境也能开发与测试。

```javascript
// 契约驱动：类型生成而非手写
export type Api = paths;                           // openapi-typescript
async function onSchemaChange(diff) {
  regenTypes(diff);
  const impacted = await compileErrors();          // 类型报错=漂移点
  return ai.explain(impacted, {                    // 漂移影响解释
    diff, require: '影响调用点+适配建议' });
}
export const mock = mswFromSchema(schema, {
  data: aiRealisticData(schema),                   // AI 补真实感mock
});
```

