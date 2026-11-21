---
title: [WEB-446] GraphQL 常见安全问题有哪些
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-446：GraphQL 常见安全问题有哪些

**答**：
- 内省（Introspection）：生产环境开着可让攻击者枚举整个 schema，应关闭或按环境区分
- 深度/复杂度攻击：一次 query 嵌套几十层或超大列表，直接打爆服务端——需 depth limit、复杂度限制、分页强制
- 字段级鉴权缺失：schema 暴露 ≠ 有权访问，resolver 内必须逐字段校验，不能只靠网关登录态
- 批量查询与 DoS：aliases 可以在一次请求里重复触发昂贵 resolver，需按操作限流
- 前端关联：错误信息把 stack/内部字段透给前端也是 GraphQL 常见泄漏，需要统一错误脱敏

```javascript
// Apollo 服务端加固片段
const server = new ApolloServer({
  schema,
  introspection: process.env.NODE_ENV !== 'production', // 生产关闭内省
  validationRules: [depthLimit(5), createComplexityLimitRule(1000)],
});
```
