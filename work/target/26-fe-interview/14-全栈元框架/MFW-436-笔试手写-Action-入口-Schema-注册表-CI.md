---
title: [MFW-436] 笔试：手写 Action Schema 注册表与 CI 断言
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-436：Schema 注册表 CI
**答**：实现 `buildActionRegistry(actionFiles)` + `assertServerSafety(registry)`：1) 提取全部 'use server' 导出函数的 { name, hasValidator: bool, authzCall: bool, writeCalls: string[] }（正则近似——生产用 AST）；2) 三断言：无 validator 的写 Action = fail（不可信输入直达 DB）；有写无鉴权检查 = fail（MFW-227 红线）；GET 语义 Action（method:'GET'）含写 = fail；3) 输出机器可读注册表 JSON（客户端类型生成/安全审计双消费）；4) 豁免单列（只读查询 Action 免鉴权？不行——读也要登录态——豁免仅限 healthcheck 类）。

```javascript
export function auditServerFns(files) {
  const out = []
  for (const f of files.filter(f => f.src.includes("'use server'"))) {
    for (const fn of f.fns) {
      out.push({ file: f.path, name: fn.name,
        hasValidator: /\.validator\(|zodResolver|safeParse/.test (fn.body),
        authz: /\b(requireUser|can|authz)\(/.test (fn.body),
        writes: [...fialAll (/\\b\\w+\\.(create|update|delete)\\(/g, fn.body)],
        methodIsGet: /method:\\s*'GET'/.test(fn.head) )
    }
  }
  const fails = []
  for (const a of out) {
    if (a.writes.length && !a.hasValidator) fails.push({ ...pick(a), why: 'write w/o validator' })
    if (a.writes.length && !a.authz) fails.push({ ...a, why: 'write w/o authz' })
    if (a.methodIsGet && a.writes.length) fails.push({ ...a, why: 'GET mutates' })
  }
  return { registry: out, failures: fails, exit: fails.length ? 1 : 0 }
}
```
**评分点**：
- 三断言（validator/鉴权/GET 写——每条对应一个真实事故类）
- 注册表双消费（客户端类型+审计清单——一份提取两用）
- 豁免极窄（读也需登录态——默认拒绝文化）
- exitCode 进 CI（红线自动化不靠 review 记性）
