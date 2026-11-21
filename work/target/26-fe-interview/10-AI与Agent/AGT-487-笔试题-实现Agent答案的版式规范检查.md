---
title: [AGT-487] 笔试题——实现输出版式检查（结构规范+引用完整+长度超标）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-487：手写版式检查器：章节结构、引用编号连续性、长度超标、空段检测

**需求与边界**：
- 输入：输出文本、版式规范；输出：检查结果与自动修复建议。
- 边界要求：① 章节结构检查（必含章节/顺序）；② 引用编号连续且存在；③ 长度超预算检测（超标率）；④ 空段落/重复段落检测；⑤ 可自动修复的给出修复文本（重试或结构化裁剪）。

**答**：
```javascript
function layoutCheck(text, spec, { docs } = {}) {
  const issues = [];
  // 1. 章节结构：必含章节按序
  const sections = text.match(/^#{1,3}\s+.+$/gm) ?? [];
  const titles = sections.map(s => s.replace(/^#+\s*/, ''));
  spec.requiredSections?.forEach((req, i) => {
    if (!titles.includes(req))
      issues.push({ type: 'missing_section', detail: req });
    else if (i > 0 && titles.indexOf(req) < titles.indexOf(spec.requiredSections[i - 1]))
      issues.push({ type: 'section_order', detail: `${req} 顺序错误` });
  });
  // 2. 引用编号：存在且（可选）连续
  const refs = [...text.matchAll(/\[(\d+)\]/g)].map(m => +m[1]);
  for (const n of new Set(refs))
    if (docs && n > docs.length)
      issues.push({ type: 'bad_ref', detail: `[${n}] 越界` });
  if (spec.refStrict && new Set(refs).size !==
      Math.max(0, ...refs))
    issues.push({ type: 'ref_gap', detail: '引用编号不连续' });
  // 3. 长度超标
  const len = text.length;
  if (len > spec.maxChars * 1.2)
    issues.push({ type: 'too_long',
      detail: `${len}/${spec.maxChars}（超 20%）`,
      fix: 'trim' });
  // 4. 空段与重复段
  const paras = text.split(/\n\s*\n/);
  if (paras.some(p => !p.trim()))
    issues.push({ type: 'empty_para' });
  const seen = new Set();
  for (const p of paras) {
    const k = p.trim().slice(0, 50);
    if (k && seen.has(k))
      issues.push({ type: 'dup_para', detail: k });
    seen.add(k);
  }
  return { pass: issues.length === 0, issues,
    fixable: issues.every(i =>
      ['too_long', 'empty_para', 'dup_para'].includes(i.type)) };
  // fixable → 自动重试（带修复指令）；
  // 不可修（缺章节）→ 人工或重新生成。
}
```

**评分点**:
- 四类检查完整：章节（含顺序）、引用（越界+连续）、长度超标率、空/重复段。
- fixable 分级：可自动修（重试带修复指令）与需重生成区分。
- 引用检查与文档集联动（越界判定）。
- 长度超标阈值 1.2（轻微超放行）的合理容差。
