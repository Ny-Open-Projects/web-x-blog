---
title: [ARC-813] 笔试：手写架构约束 CI 检测器
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## ARC-813：手写架构约束检测器

**答**：实现「架构约束」的 CI 检测器——防止架构劣化的自动化：① 模块边界约束：{ module, allowedImports: [...] }——模块 A 只准 import 白名单（如 core 不得 import 任何业务模块）；② 禁用 API 清单：{ pattern, reason, alternative }（如 document.write → 禁用）；③ 新依赖门禁：package.json diff——新增依赖需在白名单或带审批标记（// approved-by:arch）；④ 约束违规的分级：error（阻断）/warn（记录趋势）；⑤ 报告与豁免：违规清单 + 豁免文件（exemptions.json 带期限——到期自动失效）。写出实现。

```javascript
const MODULE_RULES = [
  { module: 'src/core/**', forbidden: ['src/features/**', 'src/pages/**'],
    reason: '内核不得依赖业务' },
  { module: 'src/ui/**', forbidden: ['src/api/**'],
    reason: 'UI 不得直连 API, 经 service 层' },
];
const BANNED = [
  { pattern: /document\.write/, reason: 'XSS 风险', alternative: 'textContent' },
  { pattern: /eval\(/, reason: '安全+性能', alternative: 'JSON.parse/Function 构造替代' },
];

function archConstraints(srcDir, changedFiles, exemptions) {
  const now = Date.now();
  const violations = [];
  const files = changedFiles ?? collect(srcDir);
  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');
    // 1) 模块边界
    for (const rule of MODULE_RULES) {
      if (!minimatch(file, rule.module)) continue;
      for (const imp of extractImports(content)) {
        if (rule.forbidden.some((f) => minimatch(imp, f))) {
          if (isExempt(file, rule.reason, exemptions, now)) continue;   // 豁免检查
          violations.push({ level: 'error', type: 'module-boundary', file, imp, reason: rule.reason });
        }
      }
    }
    // 2) 禁用 API
    for (const b of BANNED)
      if (b.pattern.test(content))
        violations.push({ level: 'error', type: 'banned-api', file, api: b.pattern.source, alternative: b.alternative });
  }
  // 3) 新依赖门禁
  const pkgDiff = diffPackageJson();
  for (const dep of pkgDiff.added)
    if (!WHITELIST.has(dep) && !pkgDiff.approved?.includes(dep))
      violations.push({ level: 'error', type: 'new-dep', dep, hint: '需 // approved-by:arch 标记' });
  const errors = violations.filter((v) => v.level === 'error');
  process.exit(errors.length ? 1 : 0);
}
function isExempt(file, reason, exemptions, now) {
  return exemptions?.some((e) => e.file === file && e.reason === reason && new Date(e.until) > now);
}
```

**评分点**：
- 三类约束统一检测（边界/禁用 API/新依赖）
- 豁免机制带期限（到期自动失效——豁免也是债）
- 新依赖的审批标记协议（// approved-by:arch）
- CI 集成（error 阻断/warn 记录分级）
