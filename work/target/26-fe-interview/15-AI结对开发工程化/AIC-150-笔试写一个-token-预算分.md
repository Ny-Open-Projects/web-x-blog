---
title: [AIC-150] 笔试：实现一个任务级 token 预算分配器，为「规则/任务/代码/缓冲」四段动态分配窗口预算？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-150：笔试：实现一个任务级 token 预算分配器，为「规则/任务/代码/缓冲」四段动态分配窗口预算？
**需求**：实现 `allocate(window, sections)`：
- 四段固定比例：rules 20% / task 20% / code 50% / buffer 10%；
- 各段实际占用 tokens 可能小于预算（剩余归还给 code）；
- code 超预算时：先裁剪最长文件（文件列表按「与任务相关度」排序已给出），截断到剩余空间；
- 返回每段的实际分配与裁剪记录。

```javascript
const RATIO = { rules: 0.2, task: 0.2, code: 0.5, buffer: 0.1 };

function tokens(text) {
  const cjk = (text.match(/[\u4e00-\u9fa5]/g) || []).length;
  return Math.ceil(cjk / 1.5 + (text.length - cjk) / 4);
}

function allocate(window, sections) {
  const plan = {};
  for (const k of Object.keys(RATIO)) plan[k] = Math.floor(window * RATIO[k]);
  const report = { clipped: [], returned: 0 };

  // 1. 非代码段：装得下则剩余归还
  let codeBudget = plan.code;
  for (const k of ['rules', 'task']) {
    const t = tokens(sections[k]);
    if (t > plan[k]) { // 规则/任务超预算属于异常，报错而非静默裁剪
      throw new Error(`${k} 超预算：${t}/${plan[k]}，请精简规则或任务描述`);
    }
    codeBudget += plan[k] - t;
    report.returned += plan[k] - t;
  }

  // 2. 代码段：按相关度顺序放入，超预算截断
  const used = [];
  let left = codeBudget;
  for (const f of sections.files) { // files 已按相关度降序
    const t = tokens(f.content);
    if (t <= left) { used.push({ file: f.path, clipped: false }); left -= t; continue; }
    if (left > 100) {
      const chars = Math.floor(f.content.length * (left / t));
      used.push({ file: f.path, clipped: true, kept: left });
      report.clipped.push(f.path);
      left = 0;
    } else {
      used.push({ file: f.path, omitted: true });
      report.clipped.push(f.path);
      break; // 预算耗尽，其余全部省略
    }
  }
  return { plan, codeBudget, used, ...report, usedTotal: window - Math.max(left, 0) };
}

// 测试
const r = allocate(8000, {
  rules: '规则'.repeat(1000),        // ~667 tokens < 1600
  task: '任务描述'.repeat(100),      // 很小
  files: [
    { path: 'target.ts', content: 'a'.repeat(4000) },   // ~1000
    { path: 'dep.ts', content: 'b'.repeat(30000) },     // 超预算被截断
    { path: 'unrelated.ts', content: 'c'.repeat(20000) }, // 省略
  ],
});
console.log(r.clipped); // ['dep.ts', 'unrelated.ts']
```

**评分点**：
1. 「剩余归还」方向正确：省下的给 code（代码上下文是伸缩弹性最大的段）；
2. rules/task 超预算应 fail-fast——静默裁掉规则会悄悄改变 AI 行为，这是门禁级错误；
3. 文件截断按相关度顺序处理，低相关文件先牺牲；
4. 截断后应保留 import/头部信息（可补充说明按行截断策略，加分）；
5. buffer 段不可被挪用——它是给模型输出漂移的安全垫。
