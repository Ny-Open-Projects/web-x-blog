---
title: [SOFT-880] 手写 resumeRewriter：把原始经历条目改写为 STAR-Q 格式（弱动词替换/量化注入/口径标注）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-880：手写 resumeRewriter：把原始经历条目改写为 STAR-Q 格式（弱动词替换/量化注入/口径标注）

**需求与边界**：
- 实现 rewrite(raw, jd)。
- 边界要求：① 弱动词检测与替换提示（“参与/协助/负责对接”→要求重述为具体动作——SOFT-862 反例词清单）；② 量化注入：无数字的条目标 QUILT_MISSING（不编数字 SOFT-639）；③ 口径标注检查（有数字无口径标 SCOPE_MISSING）；④ JD 关联：输出该条目命中的 JD 关键词（自然覆盖不堆砌——命中数标注）；⑤ 输出改写后条目+修改说明。

**答**：
```javascript
const WEAK = /参与|协助|负责对接|配合|了解/;
function rewrite(raw, jd) {
  const issues = [];
  let text = raw.text;
  if (WEAK.test(text)) {
    issues.push(`弱动词「${text.match(WEAK)[0]}」——重述为具体动作（做了什么决策/写了什么代码/推动什么落地）`);
  }
  const hasNum = /\d/.test(text);
  if (!hasNum) issues.push('QUANT_MISSING：无量化——从证据库补数字（SOFT-616），不许编');
  if (hasNum && !raw.scope)
    issues.push('SCOPE_MISSING：数字无口径标注（SOFT-639）');
  const hits = (jd.keywords ?? []).filter(k => text.includes(k));
  if (!hits.length)
    issues.push('JD_MISS：未命中任何JD关键词——措辞替换或舍弃');
  return {
    rewritten: hasNum && !WEAK.test(text)
      ? `${text}（${raw.scope}）` : null,
    issues,
    jdHits: hits,
    action: issues.length === 0 ? '可用'
      : issues.some(i => i.includes('QUANT') || i.includes('SCOPE'))
      ? '补量化与口径后再用'
      : '重述弱动词后再用' };
}
```

**评分点**:
- 弱动词检测（参与/协助=无贡献信号 SOFT-862 反例清单）。
- 量化缺失与口径缺失分开检测（QUANT/SCOPE——不编数字纪律）。
- JD 命中检查（自然覆盖不堆砌；未命中建议舍弃或改写）。

