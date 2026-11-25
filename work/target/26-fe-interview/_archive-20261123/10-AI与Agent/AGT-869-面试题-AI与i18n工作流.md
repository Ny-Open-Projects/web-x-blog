---
title: [AGT-869] 多语言文案的 AI 辅助（翻译/长度适配/术语一致），工程化要点？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-869：多语言文案的 AI 辅助（翻译/长度适配/术语一致），工程化要点

**答**：
- 术语表锁定：产品术语（品牌名/功能名）进翻译 glossary，AI 翻译必须遵守（术语不一致是最常见的 AI 翻译事故）；占位符与标签完整性校验（翻译不得丢失 {variable} 与 HTML 标签）。
- 长度适配：UI 文案按语言膨胀系数（德语 +30%）预警，超长让 AI 出「短变体」而非硬截断。
- 流程：AI 初译 → 术语/占位符/长度三道自动校验 → 母语者抽检（按重要性抽）→ 入库；翻译 diff 可视化评审。

```javascript
async function translateBatch(keys, langs) {
  return pMap(langs, async lang => {
    const out = await ai.translate(keys, lang, { glossary: TERMS });
    const checks = {
      placeholder: placeholdersIntact(keys, out),   // 占位符完整
      terms: glossaryOk(out, TERMS),
      length: keys.filter(k => len(out[k]) > len(keys[k]) * EXPANSION[lang]),
    };
    return { lang, out, issues: checks,
      shortVariants: checks.length.length ? await ai.shorten(checks.length) : null };
  });
}
```

