---
title: [ENG-315] 笔试题——实现 onboarding 一键检查器（环境自检 + 可行动提示）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-315：手写环境自检器

**需求与边界**：
- 需求：`pnpm verify` 环境自检——① Node/pnpm 版本匹配 packageManager；② 必需 env 存在（对照 .env.example）；③ 依赖完整（install 干净）；④ codegen 已生成；输出「✅/❌ + 可行动修复命令」，全部通过才允许 dev 启动。
- 边界：① 版本 semver 主版本校验（次版本容差）；② 检查顺序依赖（env 缺失就不检查下游）；③ 修复命令可直接复制执行。

**答**：
```javascript
async function verifyEnv() {
  const checks = [];
  const nodeMajor = parseInt(process.versions.node);
  const required = parseInt(readPackageManager().split('@')[1].split('.')[0]);
  checks.push(nodeMajor === required ? { ok: true, name: 'node' } : {
    ok: false, name: 'node',
    fix: `corepack use pnpm@${readPackageManager()}`,   // 可复制修复命令
  });
  const requiredEnv = parseEnvExample();
  const missing = requiredEnv.filter(k => !(k in process.env));
  if (missing.length) {
    checks.push({ ok: false, name: 'env', fix: `cp .env.example .env && 填写 ${missing.slice(0, 3)}` });
    return finish(checks);                             // env 缺失不查下游（顺序依赖）
  }
  const installed = fs.existsSync('node_modules/.pnpm');
  checks.push(installed ? { ok: true, name: 'deps' } : { ok: false, name: 'deps', fix: 'pnpm install' });
  const generated = fs.existsSync('src/generated');
  checks.push(generated ? { ok: true, name: 'codegen' } : { ok: false, name: 'codegen', fix: 'pnpm codegen' });
  return finish(checks);
}
function finish(checks) {
  for (const c of checks)
    console.log(`${c.ok ? '✅' : '❌'} ${c.name}${c.fix ? `\n   修复: ${c.fix}` : ''}`);
  if (checks.some(c => !c.ok)) process.exit(1);
  console.log('环境就绪，pnpm dev 开始开发');
}
```

**评分点**:
- 检查顺序依赖（env 缺失短路下游——ENG-212 的体验细节）。
- 每个失败项带可复制修复命令（非报错堆栈）。
- semver 主版本匹配（次版本容差）。
- exit code 语义（CI/脚本可消费）。
