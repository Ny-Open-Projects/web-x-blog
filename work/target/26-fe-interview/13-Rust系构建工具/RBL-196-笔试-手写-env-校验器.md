---
title: [RBL-196] 笔试：手写构建环境变量校验器（缺变量提前失败）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-196：笔试：手写构建环境变量校验器（fail fast，别跑 20 分钟才报缺变量）

**答**：写 env-guard.mjs：1) 输入声明文件 env.schema.json：必填/可选变量、类型（string/int/url/bool）、默认值、正则约束；2) 校验 process.env：必填缺失 → 报错列出全部缺失项（一次报全，不是逐个失败）；类型不符/正则不过 → 报错；可选缺省 → 注入默认值；3) 支持 scope：prod-only 变量仅在 NODE_ENV=production 时必填；4) 校验通过后输出 sanitized 摘要（值脱敏：PASSWORD/KEY/TOKEN 只显示 ***）；5) 失败 exit 1 且在构建开始前运行（CI 第一步）。

```javascript
// env-guard.mjs
// env.schema.json 示例：
// {
//   "NODE_ENV": { "type": "string", "pattern": "^(development|test|production)$" },
//   "CDN_HOST": { "type": "url", "required": true },
//   "BUILD_NUMBER": { "type": "int", "required": false, "default": "0" },
//   "UPLOAD_KEY": { "type": "string", "required": "prod-only" },
//   "APP_ID": { "type": "string", "required": true }
// }

const CHECK = {
  string: v => typeof v === 'string' && v.length > 0,
  int: v => /^-?\d+$/.test(v),
  url: v => /^https?:\/\//.test(v),
  bool: v => /^(true|false|0|1)$/.test(v),
};

export function envGuard(schema, env = process.env) {
  const missing = [], invalid = [], resolved = {};
  const isProd = env.NODE_ENV === 'production';

  for (const [name, rule] of Object.entries(schema)) {
    const required = rule.required === true || (rule.required === 'prod-only' && isProd);
    let v = env[name];
    if (v === undefined || v === '') {
      if (required) { missing.push(name); continue; }
      v = rule.default;
      if (v === undefined) continue;                 // 可选且无默认：跳过
    }
    if (!CHECK[rule.type]?.(v)) { invalid.push({ name, reason: `类型应为 ${rule.type}, got "${v.slice(0, 20)}"` }); continue; }
    if (rule.pattern && !new RegExp(rule.pattern).test(v)) { invalid.push({ name, reason: '正则不符' }); continue; }
    resolved[name] = v;
  }
  const SENSITIVE = /PASSWORD|KEY|TOKEN|SECRET/i;
  const summary = Object.fromEntries(Object.entries(resolved)
    .map(([k, v]) => [k, SENSITIVE.test(k) ? '***' : v])); // 脱敏后打日志，防密钥泄进 CI 日志

  if (missing.length || invalid.length) {
    console.error('缺失必填:', missing.join(', '));
    invalid.forEach(i => console.error(`非法: ${i.name} — ${i.reason}`));
    process.exit(1);
  }
  Object.assign(process.env, resolved);              // 默认值回填
  console.log('[env-guard] ok', summary);
  return summary;
}
envGuard(JSON.parse(readFileSync('env.schema.json', 'utf8')));
```
**评分点**：
- 一次收集全部缺失项再失败（fail fast 且 fail complete）。
- prod-only 作用域条件必填。
- 类型+正则双约束，默认值回填。
- 敏感变量脱敏摘要（密钥不进 CI 日志是安全意识）。
- 定位在流水线第一步（构建前置门禁）。
