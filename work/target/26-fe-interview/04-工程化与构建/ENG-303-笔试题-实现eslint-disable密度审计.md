---
title: [ENG-303] 笔试题——实现 eslint-disable 密度审计与豁免清单校验？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-303：手写 disable 审计

**需求与边界**：
- 需求：扫描源码 eslint-disable 注释——① 无原因注释的 disable 违规；② 密度（disable 数/千行）超阈值告警；③ disable 的规则必须仍在豁免清单中（清单外禁用规则 = 违规）；④ 过期豁免检测（豁免带 expiresAt）。
- 边界：① 支持 eslint-disable-next-line / eslint-disable 区间两种形式；② 多规则合并禁用（eslint-disable rule-a, rule-b）逐规则校验；③ 豁免清单按目录 scope 匹配。

**答**：
```javascript
function auditDisables(files, waiverList, { densityThreshold = 1 } = {}) {
  const issues = [];
  const counts = {};
  for (const f of files) {
    const lines = f.content.split('\n');
    let disables = 0;
    lines.forEach((line, i) => {
      const m = line.match(/eslint-disable(?:-next-line)?\s+(.*)/);
      if (!m) return;
      const rules = m[1].trim().split(/[\s,]+/).filter(Boolean);
      const hasReason = /--\s+\S/.test(m[1]) || reasonAbove(lines, i);   // 行内或上一行原因
      if (!hasReason) issues.push({ file: f.path, line: i + 1, type: 'NO_REASON' });
      for (const rule of rules) {
        const waiver = waiverList.find(w =>
          w.rule === rule && f.path.startsWith(w.scope));
        if (!waiver) issues.push({ file: f.path, line: i + 1, type: 'NOT_IN_WAIVER', rule });
        else if (waiver.expiresAt && new Date(waiver.expiresAt) < new Date())
          issues.push({ file: f.path, type: 'WAIVER_EXPIRED', rule });
      }
      disables++;
    });
    counts[f.path] = disables / (lines.length / 1000);   // 千行密度
    if (counts[f.path] > densityThreshold)
      issues.push({ file: f.path, type: 'DENSITY_HIGH', value: counts[f.path].toFixed(2) });
  }
  return issues;
}
```

**评分点**:
- 两种 disable 形式解析 + 多规则拆分校验。
- 原因检测（行内/上一行）+ 豁免清单三态（存在/过期/越界）。
- 千行密度阈值（ENG-219 的工程化落地）。
- 输出按类型可行动（NO_REASON/NOT_IN_WAIVER/WAIVER_EXPIRED）。
