---
title: [AIC-993] IM 遗留消息协议要迁到新协议，如何用「双写双读」校验让 AI 生成的转换不出错？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-993：IM 遗留消息协议要迁到新协议，如何用「双写双读」校验让 AI 生成的转换不出错？
**答**：
- 双写：迁移期同一条消息同时按旧/新协议写入（或同时维护两种表示），双读：读取时分别用旧/新解析器解析并与预期比对——结论：新旧共存期是验证转换正确性的黄金窗口。
- 用「影子流量」对比：把线上真实消息复制一份喂给新解析器（不影响用户），对比新旧解析结果，差异即转换 bug；AI 生成的转换器在影子流量下跑一段时间再放量。
- 要有「差异分类与阈值」：允许已知的可控差异（如时间戳格式），其他差异必须为零才放量；监控差异率作为放行指标。
- 追问钩子：能说出「双写双读的代价是存储与复杂度，换来对转换正确性的高置信；迁移完成后要及时清理双写，否则它自己变成新的遗留」的候选人有全周期视角。

```typescript
// 双读影子校验：新旧解析器对比
function shadowCheck(messages, oldParse, newParse, allowKeys=new Set(['formattedAt'])) {
  const diffs=[];
  for(const m of messages){
    const a=oldParse(m), b=newParse(m);
    const keys=new Set([...Object.keys(a),...Object.keys(b)]);
    for(const k of keys){
      if(allowKeys.has(k)) continue; // 已知可控差异
      if(JSON.stringify(a[k])!==JSON.stringify(b[k])) diffs.push({ id:m.id, field:k, old:a[k], new:b[k] });
    }
  }
  return { pass:diffs.length===0, diffs };
}
console.log(shadowCheck([{id:1,type:'text',body:'hi',formattedAt:'today'}],
  m=>({type:m.type,body:m.body,formattedAt:'昨天'}),
  m=>({type:m.type,body:m.body,formattedAt:'today'}))); // pass=true（忽略已知差异）
```
