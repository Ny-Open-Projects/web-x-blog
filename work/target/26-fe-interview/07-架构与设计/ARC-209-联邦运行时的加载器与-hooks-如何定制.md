---
title: [ARC-209] 联邦运行时的加载器与 hooks 如何定制？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-209：联邦运行时的加载器与 hooks 如何定制？
**答**：
- 2.0 运行时是插件化的：提供 hooks（init 之前/之后、加载 remote 前后、错误等），公司级公共能力（监控、鉴权、CDN 改写、降级）做成一个 npm 包，各主应用统一接入，而不是每处自己写 try/catch。
- 典型定制：beforeLoadRemote 里做 CDN 域名改写（按用户就近）与灰度路由（见 ARC-276 灰度平台）；afterLoadRemote 里上报加载耗时；onError 统一降级。
- 加载器抽象：把"URL 解析 → fetch manifest → 协商共享 → 执行模块"封装为可替换的 loader，测试时注入 mock loader（依赖倒置）。

```javascript
// 公司级联邦运行时插件：统一监控 + 就近 CDN + 灰度
import { registerPlugins } from '@module-federation/enhanced/runtime';

registerPlugins([{
  name: 'company-mf-plugin',
  beforeLoadRemote(args) {
    const { name, entry } = args;
    return { ...args, entry: rewriteByRegion(entry) };          // 就近 CDN：cn→cn.example.com
  },
  afterLoadRemote(args) {
    perf.report('mf-load', { remote: args.id, ms: args.timestamp - args.startTimestamp });
    return args;
  },
  errorLoadRemote(args) {
    report({ type: 'mf-error', remote: args.id });
    return { ...args, fallbackEntry: localFallback(args.id) };   // 统一降级入口
  },
}]);
```
