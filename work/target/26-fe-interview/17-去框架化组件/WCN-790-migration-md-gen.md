---
title: [WCN-790] 笔试：手写组件属性变更的迁移文案生成器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-790：笔试：手写组件属性变更的迁移文案生成器

**答**：
- 需求：实现 `genMigration(changes)`，changes 为 `[{ from, to, reason, options? }]`（options 为旧值→新值的映射对象，可选）。为每个变更生成一段 markdown：标题 `### from → to`、原因行、若有 options 则生成「值映射表」表格（旧值 | 新值）。最后拼接返回。边界：空数组返回空字符串；缺 reason 用默认文案。
- 要点：逐条构造字符串；options 用 Object.entries 生成表格行；reason 兜底；拼接。

```javascript
function genMigration(changes) {
  return (changes || []).map((c) => {
    const reason = c.reason || '（未说明原因）';
    let md = `### ${c.from} → ${c.to}\n\n- 原因：${reason}\n`;
    if (c.options && Object.keys(c.options).length) {
      md += '\n- 值映射：\n\n| 旧值 | 新值 |\n| --- | --- |\n';
      for (const [oldV, newV] of Object.entries(c.options)) {
        md += `| ${oldV} | ${newV} |\n`;
      }
    }
    return md;
  }).join('\n');
}
console.log(genMigration([
  { from: 'size', to: 'scale', reason: '统一命名', options: { sm: 's', lg: 'l' } },
  { from: 'onClick', to: 'onPress' },
]));
```

**评分点**：
- 标题、原因、值映射表格格式完整正确。
- options 存在才生成表格，缺 reason 有默认文案。
- 空数组返回空字符串，具备边界处理。
- 输出可直接用于迁移文档，结构清晰。
