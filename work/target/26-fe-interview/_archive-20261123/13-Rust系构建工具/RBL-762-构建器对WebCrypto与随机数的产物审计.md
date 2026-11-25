---
title: [RBL-762] 产物安全审计：Math.random 用于安全场景、硬编码密钥模式与 eval 残留
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-762：产物安全审计：Math.random 用于安全场景、硬编码密钥模式与 eval 残留

**答**:
- 产物级安全审计的三个高频模式：1) **Math.random 用于安全场景**（token/id 生成本该用 crypto.getRandomValues——Math.random 可预测）；2) **硬编码密钥模式**（API key 正则/熵分析——第三方 SDK 的 key 常被误当「公开的」内联）；3) **eval/new Function 残留**（依赖里的 eval 在 CSP 严格站点直接失效 + 攻击面）。构建器审计器在产物字符串上跑，比源码扫描更接近现实（压缩后仍可识别模式）。
- Math.random 的判定难点：「安全场景」不可静态判定——启发式：变量名上下文（token/secret/otp/nonce）+ 用途模式（UUID 生成 `Math.random().toString(36)`）；保守策略是 warn 而非 error（误报多），高危模式（密码学上下文）error。
- eval 残留的来源：老依赖（moment 插件/旧模板引擎）、jsonp 类动态加载——审计报告标注来源模块（sourcemap 反查 RBL-608），修复动作是替换依赖或 CSP nonce 方案。
- 熵分析：固定密钥检测不能只靠正则（AKIA 模式只覆盖 AWS）——「高熵字符串检测」（连续 base64 样式长串 + 命名上下文）能抓到自研密钥；误报（压缩后的 hash/URL）靠上下文过滤。
- 追问钩子：为什么产物审计比源码审计更能抓到「真实问题」？——源码里密钥可能来自 define 注入（RBL-760）或 env 替换，产物才是「实际发布的内容」；且产物审计对「依赖引入的问题」（eval/老库模式）可见性更高——产物是唯一要为线上安全负责的形态。

```javascript
// 产物安全审计器
const PATTERNS = [
  { id: 'math-random-crypto', re: /Math\.random\(\)[^;]{0,40}(token|secret|otp|nonce|uuid)/i, level: 'error' },
  { id: 'aws-key', re: /AKIA[0-9A-Z]{16}/, level: 'error' },
  { id: 'generic-key', re: /(?:api[_-]?key|secret)["']?\s*[:=]\s*["'][A-Za-z0-9+/]{20,}["']/i, level: 'error' },
  { id: 'eval', re: /\beval\(|new Function\(/, level: 'warn' },
];
function auditSecurity(products, { sm }) {
  const findings = [];
  for (const f of products) {
    for (const p of PATTERNS) {
      for (const m of f.code.matchAll(new RegExp(p.re, 'g'))) {
        const loc = sm ? sm.find(f.name, offsetOf(f.code, m.index)) : null;
        findings.push({ id: p.id, level: p.level, file: f.name,
          source: loc ? `${loc.srcFile}:${loc.srcLine}` : 'unknown' });
      }
    }
    // 高熵字符串检测（上下文含 key/token）
    for (const m of f.code.matchAll(/(["'])([A-Za-z0-9+/]{32,})\1/g))
      if (entropy(m[2]) > 4.5 && /key|token|secret/i.test(f.code.slice(Math.max(0, m.index - 60), m.index)))
        findings.push({ id: 'high-entropy-literal', level: 'warn', file: f.name });
  }
  return findings;
}
const entropy = (s) => { const f = {}; for (const c of s) f[c] = (f[c] || 0) + 1;
  return -Object.values(f).reduce((a, n) => a + (n / s.length) * Math.log2(n / s.length), 0); };
```
