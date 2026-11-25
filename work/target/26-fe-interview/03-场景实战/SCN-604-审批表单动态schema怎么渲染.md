---
title: [SCN-604] 审批表单的动态 schema 怎么渲染？不同节点看到的表单不一样怎么办？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-604：审批表单动态 schema 怎么渲染？
**答**：
- schema 分层：表单字段定义（类型/校验/联动）+ 节点权限（各节点可编辑/只读/隐藏哪些字段）；渲染器按「字段 schema × 当前节点权限」计算视图模型。
- 权限三种态：EDITABLE（可改，需重新校验）/ READONLY（展示 + 显示谁填的）/ HIDDEN（不渲染——注意与只读的区别，隐藏字段仍会提交原值吗？——必须明确：hidden 字段不提交，防越权改值）。
- 联动规则声明式：visibleWhen/requiredWhen/optionSource 用 JSON 表达，渲染器统一求值；禁止业务组件里散落 if。
- 版本兼容：审批进行中表单 schema 升级，已提交实例用提交时版本渲染（快照），新发起用新版本。
- 追问钩子：为什么每节点存表单快照——审批中改表单定义不能影响在途审批，这是审计要求。

```javascript
function buildViewModel(fieldSchema, nodePerm, formData) {
  return fieldSchema
    .filter(f => nodePerm[f.name] !== 'HIDDEN')               // hidden 不渲染也不提交
    .map(f => ({
      ...f,
      mode: nodePerm[f.name] || 'READONLY',
      value: formData[f.name],
      required: evaluate(f.requiredWhen, formData),           // 联动求值
      visible: evaluate(f.visibleWhen, formData),
    }))
    .filter(f => f.visible);
}
function evaluate(rule, data) {
  if (!rule) return true;
  return rule.op === 'eq' ? data[rule.field] === rule.value
       : rule.op === 'in' ? rule.values.includes(data[rule.field])
       : true;                                                // 未知操作符放行可见，提交时校验
}
```
