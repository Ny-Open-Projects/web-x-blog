---
title: [SCN-1176] SCADA 大屏的多语言支持（合资工厂）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1176：SCADA 大屏的多语言支持（合资工厂）

**答**：
- 支持：中英双语切换（工位术语双语），外方管理层看板英文。
- 实现：术语库（工艺术语双语对照，工艺部门审核），大屏双语同显（主+副标注）。
- 一致性：同一 tag 双语言描述一致。

```javascript
// 工业双语
function bilingualTag(tag) {
  return { zh: tag.desc, en: tag.descEn ?? tag.desc,   // 缺英文回退中文
    unit: tag.unit,                                    // 单位不翻译
    note: '术语对照需工艺部门审核' };
}
function tagBoard(tags, lang) {
  return tags.map(t => lang === 'en' ? bilingualTag(t).en : bilingualTag(t).zh);
}
```
