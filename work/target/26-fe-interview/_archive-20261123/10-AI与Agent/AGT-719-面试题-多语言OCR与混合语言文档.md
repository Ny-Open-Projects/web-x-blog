---
title: [AGT-719] 中英混排/多语言文档的 OCR 与索引怎么处理？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-719：中英混排/多语言文档的 OCR 与索引怎么处理

**答**：
- OCR 按区域语言检测（行级/块级语言识别后选对应模型），中英混排用支持混合的 OCR 引擎；置信度分语言统计（低资源语言单独阈值）。
- 索引语言标注：chunk 标注主语言与次要语言，检索时 query 语言做偏置（中文问题优先中文块但不排除英文块——技术文档常见"英文术语中文解释"）。
- 翻译辅助层：可选为非用户语言的 chunk 生成翻译摘要做二次索引（原内容+译文摘要都可命中），引用时仍指向原文。

```javascript
async function indexMultilang(page) {
  const blocks = await ocr(page, { langDetect: 'block' });
  return blocks.map(b => ({
    text: b.text, lang: b.lang,
    translated: b.lang !== PRIMARY_LANG
      ? summarizeTranslate(b.text) : null,         // 译文摘要二次索引
    conf: b.conf, langOk: b.conf > LANG_THRESH[b.lang],
  }));
}
```

