---
title: [PER-625] SRI 在什么情况下会失效或给不了保护？hash 与版本、缓存、动态加载的关系怎么处理？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-625：SRI 在什么情况下会失效或给不了保护？hash 与版本、缓存、动态加载的关系怎么处理？

**答**：
- SRI 生效前提：响应必须是完整下载（流式渲染的 HTML 无效）、资源为 CORS 可读（crossorigin 属性正确）、服务器支持（部分 CDN 对 SRI 校验失败返回 403 需处理）。
- 失效场景：**跟随 latest**（内容变化 hash 必变，不能同时用 latest+SRI，二选一）、**服务端动态生成资源**（每次内容不同无法固定 hash）、**polyfill.io 类按 UA 返回不同内容的服务**（hash 永不匹配，这类服务本质上不可信）、**缓存了旧 HTML 引用新 hash**（发版顺序问题）。
- 与发版流程的配合：静态资源内容定稿 -> 生成 hash -> 更新 HTML 引用，HTML 与资源原子发布（或资源保留旧版本 N 天，保证旧 HTML 可用）；构建工具链自动化生成 SRI（vite-plugin-sri 等）。
- 兜底策略：SRI 失败触发降级加载（备用域名无 SRI 版本）要非常谨慎——降级等于放弃校验，只允许对非核心资源，且要告警。

```javascript

const sriRules = {
  mustPair: { '固定版本 + SRI': '安全组合', 'latest + SRI': '不可能成立，二选一',
    'latest 无 SRI': '高危，仅非核心资源' },
  flow: '构建期自动生成 integrity -> HTML 原子引用 -> 资源保留旧版本 7 天',
  failure: {
    behavior: 'script error 事件 -> 上报',
    fallback: '仅非核心资源允许降级无 SRI 重载，核心资源宁可页面不可用',
    alert: 'SRI 失败率突增 -> 立即检查是否 CDN 被篡改',
  },
  forbidden: 'polyfill.io 类按 UA 返回内容的服务：hash 永不匹配，禁用',
};
console.log(sriRules.mustPair);
```
