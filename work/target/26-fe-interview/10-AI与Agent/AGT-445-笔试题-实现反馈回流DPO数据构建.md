---
title: [AGT-445] 笔试题——实现反馈回流管线（偏好对构建+质量过滤+授权校验）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-445：手写偏好数据构建：编辑差异抽取、正负样本配对、质量与授权过滤

**需求与边界**：
- 输入：用户编辑事件（AI 原稿+用户改后稿）、反馈开关状态；输出：DPO 偏好对数据集。
- 边界要求：① 编辑幅度过小（同义改写）不入集（噪声）；② 用户授权（数据用于训练的开关）强制校验；③ PII 脱敏；④ 配对质量：改动须可归因（改了什么维度标注）。

**答**：
```javascript
async function buildPreferencePairs(edits, { consentOf, diff }) {
  const pairs = [];
  for (const e of edits) {
    // 1. 授权校验（强制，无授权不入集）
    if (!await consentOf(e.userId, 'training'))
      continue;
    // 2. 编辑幅度：改动率过低（同义润色）不入集
    const d = diff(e.aiDraft, e.userFinal);
    if (d.ratio < 0.1) continue;
    // 3. PII 脱敏（双方文本都过）
    const clean = (s) => redactPII(s);
    // 4. 改动维度归因（可解释的偏好标签）
    const dims = classifyDiff(d);            // [fact/style/length/structure]
    if (!dims.length) continue;              // 无法归因不入集
    pairs.push({
      prompt: e.query,
      chosen: clean(e.userFinal),            // 用户改后=偏好
      rejected: clean(e.aiDraft),
      dims, source: 'user_edit',
      consent: true, ts: e.ts,
    });
  }
  // 5. 去重与平衡：同 prompt 多次编辑取最新，正负类目均衡检查
  const dedup = new Map(pairs.map(p => [p.prompt + p.dims.join(), p]));
  return [...dedup.values()];
}
// 使用约束：偏好对仅用于反馈类微调，
// 不得包含跨用户上下文；训练前再过一次 PII 扫描。
```

**评分点**:
- 授权强制前置（consent 校验最先），合规红线。
- 噪声过滤三关：编辑幅度阈值、改动维度归因（无法归因不入）、去重。
- PII 双侧脱敏 + 训练前复扫的纵深意识。
- chosen/rejected 语义正确（用户改后为 chosen）且带维度标签（可解释偏好）。
