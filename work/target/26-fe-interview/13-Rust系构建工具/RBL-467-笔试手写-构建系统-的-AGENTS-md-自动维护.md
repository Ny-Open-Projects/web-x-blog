---
title: [RBL-467] 笔试：手写构建文档（AGENTS.md 类）自动维护器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-467：手写构建文档自动维护器
**需求**：实现 `syncBuildDocs(config, docs)`：1) 单一事实源：从 config schema 自动生成「构建配置文档」章节（字段/默认值/说明）——手写文档必然漂移；2) 变更检测：config 变更 → 文档 diff → 提示需要更新（PR 门禁：改配置必改文档或声明不适用）；3) 章节 protect：人工写的章节（架构决策/最佳实践）不会被自动生成覆盖（区域标记 <!-- auto -->）；4) 示例同步：配置示例从 schema 生成合法示例（不会出现过期字段）；5) 输出：更新后的文档 + diff 摘要。

```javascript
export function syncBuildDocs(schema, currentDocs) {
  const AUTO_START = '<!-- auto:config-docs -->'
  const AUTO_END = '<!-- /auto:config-docs -->'

  function renderSchema(schema) {
    const lines = ['| 字段 | 类型 | 默认值 | 说明 |', '|---|---|---|---|']
    for (const [key, rule] of Object.entries(schema)) {
      lines.push(`| ${key} | ${rule.type}${rule.values ? ` (${rule.values.join('|')})` : ''} | ${rule.default ?? '-'} | ${rule.desc ?? ''} |`)
    }
    return [AUTO_START, ...lines, AUTO_END].join('\n')
  }

  function apply(docs) {
    const rendered = renderSchema(schema)
    if (docs.includes(AUTO_START)) {
      // 区域替换：保护人工章节
      const pre = docs.slice(0, docs.indexOf(AUTO_START))
      const post = docs.slice(docs.indexOf(AUTO_END) + AUTO_END.length)
      return { next: pre + rendered + post, changed: true }
    }
    return { next: docs + '\n\n' + rendered, changed: true }      // 首次插入
  }

  function detectDrift(docs) {
    const rendered = renderSchema(schema)
    if (!docs.includes(AUTO_START)) return { drift: true, reason: 'auto section missing' }
    const existing = docs.slice(docs.indexOf(AUTO_START), docs.indexOf(AUTO_END) + AUTO_END.length)
    return { drift: existing !== rendered, reason: existing !== rendered ? 'schema changed' : null }
  }

  return { apply, detectDrift }
}
```
**评分点**：
- 单一事实源（schema → 文档——手写文档必漂移的根治）
- 区域保护标记（人工章节不被覆盖——自动化的边界）
- drift 检测进 PR 门禁（改配置必改文档——漂移预防）
- 示例从 schema 生成（不会过期）
