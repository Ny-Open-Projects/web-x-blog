---
title: [ARC-332] 笔试题：实现组件库的 Form 校验引擎？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-332：笔试题：实现组件库的 Form 校验引擎？
**答**：实现表单校验引擎 `validate(values, rules)`：1) 支持嵌套路径（'a.b.c'）与数组（'users.0.name' / 'users.*.name'）；2) 同步规则与异步规则混合，单字段内串行、字段间并行；3) 返回错误结构按路径聚合；4) 支持中止（第一个失败即停）模式。
**评分点**：
- 路径取值正确（嵌套+数组通配符遍历）。
- 并发模型正确（字段 Promise.all、字段内规则顺序 await）。
- 错误聚合结构合理（{ 'user.name': '必填', 'users.*.age': [...] }）。
- abort 语义正确（字段内短路；字段间保持并行但可 cancel）。
```typescript
function getPath(obj, path) {
  return path.split('.').reduce((o, k) => (o == null ? undefined : o[k]), obj);
}
function matchPaths(obj, pattern) {           // 'users.*.name' → ['users.0.name', ...]
  const parts = pattern.split('.');
  let cur = [{ key: '', value: obj }];
  for (const p of parts) {
    cur = cur.flatMap(({ key, value }) => {
      if (p === '*') return Object.keys(value ?? {}).map(k => ({ key: `${key}.${k}`, value: value[k] }));
      return [{ key: `${key}.${p}`, value: value?.[p] }];
    });
  }
  return cur.map(c => c.key.slice(1));   // key 恒以 '.' 开头，去掉首字符即可；加 startsWith 过滤会把结果全滤空
}
async function validate(values, rules, { abortFirst = false } = {}) {
  const errors = {};
  await Promise.all(Object.entries(rules).map(async ([pattern, fieldRules]) => {
    for (const path of matchPaths(values, pattern)) {
      for (const rule of fieldRules) {        // 2) 字段内串行
        const ok = await rule.validator(getPath(values, path), values);
        if (!ok) {
          (errors[path] ??= []).push(rule.message);
          if (abortFirst) throw { abort: true, errors };                  // 4) 短路
          break;
        }
      }
    }
  }));
  return errors;                                                          // 3) 聚合
}
```

## 变体与延伸（补充）

**变体与延伸**：

1. 异步校验的竞态怎么处理？→ 按路径维护请求序号只采纳最新结果，输入期间做 debounce，过期的响应直接丢弃而不是覆盖当前错误提示。
2. 依赖字段（如确认密码）怎么校验？→ 规则函数拿到全量 values，被依赖字段变更时主动触发依赖方重校验，依赖关系显式声明而不是隐式耦合。
3. 大表单性能怎么保证？→ 字段级订阅只重渲染出错字段，规则按路径缓存避免每次全量遍历，字段规模上万时再考虑分片校验。
