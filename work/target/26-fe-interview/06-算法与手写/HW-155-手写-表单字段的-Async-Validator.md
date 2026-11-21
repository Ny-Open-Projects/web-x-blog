---
title: [HW-155] 手写字段级 AsyncValidator——并行校验聚合、依赖注入与错误消息本地化
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：异步校验聚合器：多字段并行校验（唯一性/风控/黑名单），Promise.allSettled 聚合（单个失败不影响其他错误收集）；错误消息本地化（校验器返回消息 key，渲染层按 locale 翻译——校验与展示解耦）；依赖注入（校验器接收 service 实例，测试时注入 mock）。

```javascript
function createValidator(rules, services) {
  // rules: { field: [{ key, test: (v, all, svc) => Promise<boolean|string-key> }] }
  return async function validate(values) {
    const jobs = [];
    for (const [field, rs] of Object.entries(rules)) {
      for (const r of rs) jobs.push(
        Promise.resolve(r.test(values[field], values, services))
          .then((ok) => ({ field, rule: r.key, ok: ok === true, msg: ok === true ? null : ok }))
      );
    }
    const settled = await Promise.allSettled(jobs);
    const errors = {};
    for (const s of settled) {
      if (s.status === 'rejected') continue;                // 单校验器崩溃：不炸整体（记日志）
      const { field, rule, ok, msg } = s.value;
      if (!ok) (errors[field] ??= []).push({ rule, msgKey: msg ?? rule });   // 消息 key：渲染层翻译
    }
    return { valid: Object.keys(errors).length === 0, errors };
  };
}
// 用法：services 依赖注入（测试 mock）
const validate = createValidator({
  email: [{ key: 'email.taken', test: async (v, all, svc) => !(await svc.checkEmail(v)) }],
  password: [{ key: 'pwd.weak', test: (v) => v.length >= 8 || 'pwd.weak' }],
}, { checkEmail: (e) => api.checkEmail(e) });
// 渲染层：t(errors.email[0].msgKey) —— "邮箱已被注册"/"Email taken" 按 locale
// allSettled：email 校验服务挂了，password 错误仍然收集（部分可用）
```

**评分点**：
- allSettled 聚合（单校验器崩溃不炸整体）——本题核心。
- 错误消息 key 与渲染层翻译解耦（校验器返回 key 不是文案）。
- 依赖注入 services（可测性）。
- errors 按 field 分组数组（同字段多规则错误都保留）。
