---
title: [AIC-064] 用 AI 处理 i18n 文案翻译与 key 管理要注意什么？直接让它翻译会有哪些坑？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-064：用 AI 处理 i18n 文案翻译与 key 管理要注意什么？直接让它翻译会有哪些坑？
**答**：
- 坑一：占位符破坏——AI 翻译会丢/改 `{{name}}`、`%s` 插值，翻译后必须校验占位符集合与原文一致。
- 坑二：长度失控——德语/俄语比中文长 2~3 倍，AI 不会自觉控制，需要约束「译文长度 ≤ 原文 × 目标语言膨胀系数」并对超长的重新措辞。
- 坑三：术语不一致——同一术语在不同页面翻出不同译法，要提供术语表（glossary）作为强约束输入。
- key 管理：key 命名规范由人定（模块.页面.语义），AI 只产出值；删源 key 时用脚本找「孤儿翻译」清理。
- 追问钩子：完整流程是「导出待译 JSON → AI 按术语表翻译 → 占位符/长度校验器 → 人工抽检 → 回导」，其中校验器是笔试考点。

```javascript
// i18n 翻译校验器：占位符一致 + 长度膨胀检查
function validateTranslation(src, dst, { maxInflation = 3 } = {}) {
  const ph = (s) => [...s.matchAll(/\{\{(\w+)\}\}|%[sd]/g)].map(m => m[0]).sort();
  if (JSON.stringify(ph(src)) !== JSON.stringify(ph(dst))) {
    return { ok: false, reason: '占位符不一致' };
  }
  if (dst.length > src.length * maxInflation) {
    return { ok: false, reason: `译文过长：${dst.length} vs ${src.length}×${maxInflation}` };
  }
  return { ok: true };
}
```
