---
title: [TST-731] 平台如何支持「安全左移」到 IDE 侧的即时反馈
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-731：平台如何支持「安全左移」到 IDE 侧的即时反馈

**答**：
- 结论：IDE 左移要在「写代码时」给即时反馈，依赖轻量的本地规则引擎 + 平台规则库定时同步，而非每次请求云端扫描。
- 本地只跑高置信度、低开销规则（危险 API、硬编码密钥），深度扫描仍交给 CI，避免卡编辑器。
- 反馈要精准到行并提供修复建议，支持一键忽略并带上原因（同步到平台做误报统计）。
- 追问钩子：本地规则与 CI 规则不一致导致「IDE 绿、CI 红」，如何治理？

```javascript
// IDE 侧轻量安全规则：检测硬编码密钥
const RULES = [
  { name: 'HARDCODED_SECRET', re: /(api[_-]?key|secret|token)\s*[:=]\s*['"][A-Za-z0-9]{16,}['"]/i },
];
function scanLine(line) {
  return RULES.filter(r => r.re.test(line)).map(r => ({
    rule: r.name, fix: '改用环境变量注入',
  }));
}
console.log(scanLine("const apiKey = 'AKIAIOSFODNN7EXAMPLE1234';"));
```
