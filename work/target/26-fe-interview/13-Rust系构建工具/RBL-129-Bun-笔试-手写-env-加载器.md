---
title: [RBL-129] 笔试：手写 .env 多环境加载器（优先级 + 注入 Define）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-129：笔试：手写 .env 多环境加载器（优先级 + 注入 Define）
**答**：写 loadEnv(mode)：1) 依次加载 .env、.env.local、.env.{mode}、.env.{mode}.local（后者优先级高）；2) 解析 KEY=VALUE（支持引号包裹与注释行）；3) process.env 已存在的键不被覆盖（系统环境优先）；4) 返回仅"前端可见"前缀（如 PUBLIC_）的键值对；5) 输出 DefinePlugin 风格的映射。

```typescript
// load-env.ts
import { readFileSync, existsSync } from 'node:fs';

function parse(content: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const raw of content.split('\n')) {
    const line = raw.trim();
    if (!line || line.startsWith('#')) continue;
    const eq = line.indexOf('=');
    if (eq < 0) continue;
    let v = line.slice(eq + 1).trim();
    // 引号剥离
    if (/^".*"$/.test(v) || /^'.*'$/.test(v)) v = v.slice(1, -1);
    out[line.slice(0, eq).trim()] = v;
  }
  return out;
}

export function loadEnv(mode: string) {
  const order = ['.env', '.env.local', `.env.${mode}`, `.env.${mode}.local`];
  const merged: Record<string, string> = {};
  for (const f of order) {
    if (!existsSync(f)) continue;
    Object.assign(merged, parse(readFileSync(f, 'utf8'))); // 后者覆盖前者
  }
  // 系统环境优先：不覆盖已有 process.env
  for (const [k, v] of Object.entries(merged))
    if (process.env[k] === undefined) process.env[k] = v;

  // 前端可见白名单前缀 → define 映射
  return Object.fromEntries(
    Object.entries(merged)
      .filter(([k]) => k.startsWith('PUBLIC_'))
      .map(([k, v]) => [`import.meta.env.${k}`, JSON.stringify(v)]),
  );
}

// 用法：const define = loadEnv('production');
// Bun.build({ define, ... })
```
**评分点**：
- 四文件加载顺序与优先级（local > mode > base）。
- 注释行与引号剥离（解析健壮性）。
- 系统环境不被覆盖（安全默认）。
- PUBLIC_ 前缀白名单（防密钥泄漏进前端产物——安全意识分）。
- 输出 define 映射可直接消费。
