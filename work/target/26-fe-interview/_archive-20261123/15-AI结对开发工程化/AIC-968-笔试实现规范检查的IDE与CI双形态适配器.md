---
title: [AIC-968] 笔试：实现「规范检查的双形态适配器」（同一份规则输出 IDE 友好与 CI 友好两种报告）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-968：笔试：实现「规范检查的双形态适配器」（同一份规则输出 IDE 友好与 CI 友好两种报告）
**答**：
- 核心需求：实现 `adaptReport(violations, target)`。`violations: { file, line, rule, msg, severity }[]`；`target` 为 "ide" 或 "ci"。返回对应格式报告。
- IDE 格式：`{ diagnostics: [{ file, range:{start:{line,character}}, message, severity:1|2|3, source:"ai-rules" }] }`（行号转 0-based，character=0）；severity 映射 error→1、warn→2、info→3。
- CI 格式：`{ passed:boolean, summary:"X errors, Y warnings", annotations:[{ path, start_line, message, annotation_level:"error"|"warning" }] }`。
- 边界：violations 为空时 IDE 返回空 diagnostics、CI 返回 passed=true；未知 target 抛错；每种格式都要保留 file/line/rule/msg 信息不丢失。
- 语义：这是「一份规则、多端消费」的适配层——规则单一来源，适配器负责格式转换，避免 IDE 与 CI 规则漂移。
- 追问钩子：能指出「适配器是 CI/IDE 关注点分离的体现；规则定义应完全中立于消费端，才能复用」的候选人理解架构分层。

```typescript
function adaptReport(violations=[], target='ide') {
  if(target==='ide') return { diagnostics: violations.map(v=>({
    file:v.file, range:{start:{line:Math.max(0,v.line-1),character:0}},
    message:v.msg, severity: v.severity==='error'?1:v.severity==='warn'?2:3,
    source:'ai-rules' })) };
  if(target==='ci'){
    const errors=violations.filter(v=>v.severity==='error').length;
    return { passed:errors===0, summary:`${errors} errors, ${violations.length-errors} warnings`,
      annotations: violations.map(v=>({ path:v.file, start_line:v.line, message:v.msg,
        annotation_level:v.severity==='error'?'error':'warning' })) };
  }
  throw new Error('未知target: '+target);
}
console.log(adaptReport([{file:'a.ts',line:5,rule:'R1',msg:'x',severity:'error'}],'ci'));
```
**评分点**：
- IDE 格式：行号转 0-based、severity 映射 1/2/3、source 标识正确。
- CI 格式：passed 按 error 数判定、summary 统计、annotations 字段完整。
- 空 violations 与未知 target 的边界处理正确。
- 两种格式均保留 file/line/rule/msg 信息，代码可运行。
- 明确「规则中立于消费端、适配层做关注点分离」（加分项）。
