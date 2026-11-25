---
title: [AGT-531] Agent 让用户填参数（订机票：出发/目的/日期）时，用自由文本还是结构化表单交互？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-531：Agent 让用户填参数（订机票：出发/目的/日期）时，用自由文本还是结构化表单交互

**答**：
- 结构化参数收集用「动态表单卡」：Agent 输出 schema（字段/类型/候选项/校验），前端渲染表单组件嵌入对话流，提交后以结构化数据回传。
- 混合模式最好：表单卡 + 旁边输入框仍可用自然语言补充（"改成靠窗"），前端把补充合并进表单值再提交。
- 表单状态可被对话修正：用户说"日期改成下周三"，前端解析意图高亮对应字段待确认，不静默修改。

```javascript
// Agent 输出 schema → 动态表单卡
function TaskFormCard({ schema, onSubmit }) {
  const [vals, setVals] = useState(schema.defaults);
  return <form onSubmit={() => onSubmit(normalize(vals))}>
    {schema.fields.map(f => f.options
      ? <Select {...f} value={vals[f.name]} onChange={v => setVals(s => ({ ...s, [f.name]: v }))} />
      : <Input {...f} />)}
    <button>确认并继续</button>
  </form>;
}
// 自然语言修正：解析→高亮字段待确认
function applyCorrection(form, text) {
  const patch = parseIntent(text, form.schema);  // { date: 'next-wed' }
  form.highlight(Object.keys(patch));            // 高亮而非静默修改
  return form.pendingPatch(patch);
}
```

