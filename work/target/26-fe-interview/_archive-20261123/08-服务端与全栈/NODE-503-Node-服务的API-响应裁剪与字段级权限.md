---
title: [NODE-503] Node 服务的响应裁剪与字段级权限（按调用方裁字段）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-503：响应裁剪与字段级权限
**答**:
- 两个动机：传输效率（BFF 只要 5 个字段，下游返回 50 个——过度传输浪费带宽与序列化 CPU）、权限（内部接口的字段含敏感数据——调用方权限不同可见字段不同 NODE-484 数据级）。
- 裁剪实现：字段白名单声明（每接口每 profile 的字段集——NODE-494 profile 机制）、动态裁剪（fields 参数 + 白名单校验——调用方只能要白名单内的）、深裁剪（嵌套对象按路径裁剪：user.address.city——递归选择器）。
- 字段级权限：字段标记敏感级（schema 注解：phone: { sensitivity: 2 }）→ 按调用方权限过滤（无权限 → 字段缺失或脱敏——NODE-396/441 规则）；默认拒绝（未声明的敏感字段不出）。
- 序列化优化：裁剪在序列化前（对象树选择器）——裁剪后再 JSON.stringify 才省 CPU；大响应流式裁剪（NODE-423）。
- 验证：裁剪正确性测试（各 profile 输出快照——字段集回归）、敏感字段泄漏扫描（响应扫描敏感模式——巡检 NODE-458）。
```javascript
// 字段选择器 + 敏感过滤
function project(data, fields, perm) {
  return walk(data, {
    include: (path) => fields.includes(path) && perm.can(path),  // 白名单 ∩ 权限
    transform: (path, v) => SENSITIVE[path] ? mask(v) : v        // 敏感脱敏
  });
}
// schema 注解：{ phone: { type: 'string', sensitivity: 2, mask: 'middle' } }
```
