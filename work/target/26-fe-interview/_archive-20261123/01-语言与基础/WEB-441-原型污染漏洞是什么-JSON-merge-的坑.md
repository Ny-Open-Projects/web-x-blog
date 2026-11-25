---
title: [WEB-441] 原型污染漏洞是什么，JSON merge 的坑
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-441：原型污染漏洞是什么，JSON merge 的坑

**答**：
- 原理：合并用户可控对象时，键 `__proto__`、`constructor.prototype` 会写到 Object.prototype 上，全站对象继承被改
- 危害示例：污染后 `{}.isAdmin === true` 成立；或污染 toString 导致后续 RCE 链
- 典型入口：深拷贝/深合并工具（lodash merge 老版本 CVE）、URL 参数转对象（qs 配置 allowPrototypes）、JSON.parse 不受影响但后续 merge 会
- 防御：merge 时过滤 `__proto__`/`prototype`/`constructor` 键；用 `Object.create(null)` 的干净字典；升级依赖版本
- 前端自查：`grep -r "merge\|extend" src/` 找所有用户输入进深合并的路径

```javascript
function safeMerge(target, src) {
  for (const k of Object.keys(src)) {
    if (k === '__proto__' || k === 'constructor') continue; // 关键过滤
    if (typeof src[k] === 'object' && src[k] !== null) {
      target[k] = safeMerge(target[k] ?? {}, src[k]);
    } else target[k] = src[k];
  }
  return target;
}
```
