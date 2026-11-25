---
title: [WCN-501] 多 BU 联邦治理下，跨 BU 元素库的命名空间与版本仲裁应如何设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-501：多 BU 联邦治理下，跨 BU 元素库的命名空间与版本仲裁应如何设计？

**答**：
- 结论：中央平台只管「命名空间 + 版本协议」，BU 保留实现自治，避免中央成为发布瓶颈。
- 命名空间采用 `@bu/<name>` 作用域，注册时校验前缀归属，防止 BU 间 tag 冲突。
- 仲裁器负责：同名多版本共存、按宿主声明的版本区间选择、冲突时降级到默认版本。
- 追问：某个 BU 下线后其命名空间如何回收且不破坏存量页面？（答：保留别名段 + 冻结期 + 重定向）

```javascript
const registry = new Map();                 // scope/name -> Map(version -> impl)
function register(scope, name, version, impl) {
  if (!scope.startsWith('@')) throw new Error('scope must be @bu/xxx');
  const key = `${scope}/${name}`;
  if (!registry.has(key)) registry.set(key, new Map());
  registry.get(key).set(version, impl);
}
function resolve(scope, name, range /* e.g. '^2.0.0' */) {
  const versions = [...(registry.get(`${scope}/${name}`)?.keys() || [])];
  const hit = versions.filter(v => satisfies(v, range)).sort(cmpSemver).pop();
  if (!hit) return { fallback: true, impl: defaultImpl }; // 冲突/缺失降级
  return { fallback: false, impl: registry.get(`${scope}/${name}`).get(hit) };
}
function satisfies(v, r) { return r === '*' || v.startsWith(r.replace('^', '')); }
function cmpSemver(a, b) { return a.localeCompare(b, undefined, { numeric: true }); }
```
