---
title: [ALG-014] 低代码平台要实现 `您好，{{user.name}}，您有 {{count}} 条消息` 的模板解析，支持点路径取值与缺失值兜底为空串。如何实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-014：低代码平台要实现 `您好，{{user.name}}，您有 {{count}} 条消息` 的模板解析，支持点路径取值与缺失值兜底为空串。如何实现？
**答**：用正则匹配 `{{ 变量 }}`，replace 回调里把路径按 `.` 拆分后 `reduce` 逐层取值，任何一层为 `null/undefined` 就返回空串，避免抛错。时间 O(n × d)（d 为路径深度），空间 O(n)。

```javascript
function renderTemplate(tpl, data) {
  return tpl.replace(/\{\{\s*([\w.]+)\s*\}\}/g, (_, path) => {
    const val = path.split('.').reduce(
      (obj, key) => (obj == null ? undefined : obj[key]),
      data
    );
    return val == null ? '' : String(val); // 缺失值兜底
  });
}
// renderTemplate('你好 {{user.name}}，共 {{count}} 条', { user: { name: 'Tom' } })
// => '你好 Tom，共  条'
```
