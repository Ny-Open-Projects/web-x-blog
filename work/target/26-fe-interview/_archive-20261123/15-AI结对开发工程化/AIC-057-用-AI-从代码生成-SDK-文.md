---
title: [AIC-057] 用 AI 从代码生成 API 文档/SDK 文档的流程怎么做？如何防止文档「编造参数」？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-057：用 AI 从代码生成 API 文档/SDK 文档的流程怎么做？如何防止文档「编造参数」？
**答**：
- 流程：类型定义（d.ts/TS 接口）为**唯一事实源** + 函数实现为行为参考，让 AI 只做「翻译」不做「创作」，输出表格化文档。
- 防编造手段：prompt 约束「参数名/类型/默认值必须逐字来自类型定义，类型里没有的字段一律不写」；生成后用脚本校验文档里的参数名集合是否与类型字段集合一致。
- 输出结构：每个导出给「签名 + 参数表 + 行为说明 + 示例 + 边界错误」；示例代码要可运行（提出来跑一遍最稳）。
- 增量更新：CI 上对「导出签名发生变化的文件」重跑文档生成，diff 只更新变化章节，避免全量重写漂移。
- 追问钩子：文档校验器（比对类型字段 vs 文档字段）就是笔试题 AIC-192 的原型。

```javascript
// 文档防编造校验：文档参数必须 ⊆ 类型字段
function validateDoc(doc, typeDef) {
  const typeFields = extractFields(typeDef); // 从 interface 抽取字段名
  const docFields = doc.params.map(p => p.name);
  const phantom = docFields.filter(f => !typeFields.includes(f));
  const missing = typeFields.filter(f => f !== 'optional' && !docFields.includes(f));
  return { phantom, missing, ok: phantom.length === 0 };
}
```
