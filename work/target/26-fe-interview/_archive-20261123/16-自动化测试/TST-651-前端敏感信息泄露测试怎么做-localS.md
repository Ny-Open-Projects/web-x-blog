---
title: [TST-651] 前端敏感信息泄露测试怎么做（localStorage / 日志 / 堆栈 / Source Map）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-651：前端敏感信息泄露测试怎么做（localStorage / 日志 / 堆栈 / Source Map）？

**答**：
- 结论：按「存储面 + 输出面 + 分发面」三处扫描——浏览器存储、console/网络日志、构建产物与 Source Map。
- 注入蜜罐令牌（canary token）后全域搜索，确认没有进入 localStorage、日志与第三方请求。
- 生产 Source Map 要么不上传，要么仅内部可访问；错误堆栈对用户输入做脱敏。
- 追问钩子：第三方 SDK 自己往 localStorage 写数据，你怎么归责与拦截？

```javascript
function scanLeaks({ storage, logs, requests }, canary) {
  const hits = [];
  const walk = (obj, path) => {
    if (typeof obj === 'string' && obj.includes(canary))
      hits.push(path);
    else if (obj && typeof obj === 'object')
      Object.entries(obj).forEach(([k, v]) => walk(v, `${path}.${k}`));
  };
  walk(storage, 'storage');
  logs.forEach((l, i) => walk(l, `log[${i}]`));
  requests.forEach((r, i) => walk(r, `req[${i}]`));
  return hits;
}
```
