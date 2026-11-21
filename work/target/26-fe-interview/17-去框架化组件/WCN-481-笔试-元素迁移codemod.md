---
title: [WCN-481] 笔试：实现元素 API 迁移的 codemod（属性重命名/事件改名）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-481：笔试：实现元素 API 迁移的 codemod（属性重命名/事件改名）。
**题目**：输入源码与映射 `[{from, to, kind: 'prop'|'event'|'tag'}]`。正则替换：prop（`.from` → `.to`，注意边界）、event（字符串字面量）、tag（标签名）。输出替换计数与歧义清单（多候选匹配）。

```javascript
function codemod(src, mappings) {
  let count = 0; const ambiguous = [];
  const lines = src.split('\n').map((line, i) => {
    let out = line;
    for (const m of mappings) {
      if (m.kind === 'prop') {
        const re = new RegExp(`\\.${m.from}\\b`, 'g');
        const hits = line.match(re)?.length || 0;
        if (hits > 1) ambiguous.push({ line: i + 1, text: line.trim() });
        out = out.replace(re, `.${m.to}`); count += hits;
      } else if (m.kind === 'event') {
        out = out.replace(new RegExp(`['"]${m.from}['"]`, 'g'), `'${m.to}'`);
      } else if (m.kind === 'tag') {
        out = out.replace(new RegExp(`<${m.from}\\b`, 'g'), `<${m.to}`);
      }
    }
    return out;
  });
  return { code: lines.join('\n'), count, ambiguous };
}

```

**评分点**：
- 三类映射不同替换模式。
- 词边界（避免误替换子串）。
- 歧义检测（同一行多匹配 → 人工标记）。
- 计数与清单输出（可复审）。
