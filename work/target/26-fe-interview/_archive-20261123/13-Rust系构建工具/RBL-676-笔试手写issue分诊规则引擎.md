---
title: [RBL-676] 笔试：手写 issue 分诊规则引擎（优先级 + 相似检测 + 自动关闭）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-676：笔试：手写 issue 分诊规则引擎（优先级 + 相似检测 + 自动关闭）

**需求**：实现 `triage(issue, ctx)`。issue: `{ id, title, body, hasRepro, openedAt, labels? }`；ctx: `{ now, closedIssues: { id, title, body }[], comment(msg), label(name), close(), priority(p) }`。规则按序执行（先到先停）：1) 标题/正文含 crash|panic|segfault → label 'crash' + priority P0 + 结束；2) 含 slow|slower|regression → label 'regression' + P1 + 结束；3) 与已关闭 issue 的标题相似度（Jaccard on 词集）≥ 0.6 → label 'duplicate' + comment 指向相似 id + 结束；4) 无复现且开启超 14 天 → comment 复现指引 + close；5) 其余 → priority 'P3'。返回 `actions: string[]`（执行的动作名列表）。

```javascript
const tokenize = (s) => new Set(s.toLowerCase().split(/\W+/).filter(Boolean));
const jaccard = (a, b) => {
  const A = tokenize(a), B = tokenize(b);
  const inter = [...A].filter(x => B.has(x)).length;
  const uni = new Set([...A, ...B]).size;
  return uni ? inter / uni : 0;
};
const ageDays = (issue, now) => (now - new Date(issue.openedAt)) / 86400000;

function triage(issue, ctx) {
  const actions = [];
  const text = issue.title + ' ' + issue.body;
  const act = (name, ...fns) => { fns.forEach(fn => fn()); actions.push(name); };

  if (/crash|panic|segfault/i.test(text)) {
    act('crash', () => ctx.label('crash'), () => ctx.priority('P0'));
    return { actions };
  }
  if (/slow|slower|regression/i.test(text)) {
    act('regression', () => ctx.label('regression'), () => ctx.priority('P1'));
    return { actions };
  }
  let best = null;
  for (const c of ctx.closedIssues) {
    const sim = jaccard(issue.title, c.title);
    if (!best || sim > best.sim) best = { id: c.id, sim };
  }
  if (best && best.sim >= 0.6) {
    act('duplicate', () => ctx.label('duplicate'),
      () => ctx.comment(`疑似重复 #${best.id}（相似度 ${best.sim.toFixed(2)}）`));
    return { actions };
  }
  if (!issue.hasRepro && ageDays(issue, ctx.now) > 14) {
    act('close-no-repro', () =>
      ctx.comment('缺少最小复现（配置+文件集+预期/实际），补充后可重开：docs/repro-guide'),
      () => ctx.close());
    return { actions };
  }
  act('p3', () => ctx.priority('P3'));
  return { actions };
}

// 自测
function makeCtx(closed = []) {
  const log = [];
  return { log,
    now: new Date('2026-11-22'),
    closedIssues: closed,
    comment: (m) => log.push('comment:' + m),
    label: (l) => log.push('label:' + l),
    close: () => log.push('close'),
    priority: (p) => log.push('prio:' + p) };
}

let r = triage({ id: 1, title: 'build segfault', body: 'panic at module graph', hasRepro: false, openedAt: '2026-11-20' }, makeCtx());
console.log(r.actions.join(',') === 'crash' && r.log.includes('prio:P0'));

r = triage({ id: 2, title: 'build is slow after upgrade', body: '', hasRepro: true, openedAt: '2026-11-20' }, makeCtx());
console.log(r.actions.join(',') === 'regression' && r.log.includes('label:regression'));

const closed = [{ id: 100, title: 'build is slow after upgrade' }];
r = triage({ id: 3, title: 'build is slow after upgrade to v2', body: '', hasRepro: false, openedAt: '2026-11-01' }, makeCtx(closed));
console.log(r.actions.join(',') === 'duplicate' && r.log.some(x => x.includes('#100')));

r = triage({ id: 4, title: 'css order wrong', body: '', hasRepro: false, openedAt: '2026-10-01' }, makeCtx());
console.log(r.actions.join(',') === 'close-no-repro' && r.log.includes('close'));

r = triage({ id: 5, title: 'css order wrong', body: '', hasRepro: true, openedAt: '2026-11-21' }, makeCtx());
console.log(r.actions.join(',') === 'p3' && r.log.includes('prio:P3'));
```

**评分点**：
- 规则优先级正确（crash > regression > duplicate > 无复现关闭 > 默认 P3），先到先停
- Jaccard 相似检测阈值 0.6 且取最高相似者；tokenize 大小写/非词边界处理
- 无复现关闭的条件（超 14 天）与重开指引的 comment 文案
- 能说清「快速关闭无复现 issue 是维护可持续性而非不友好」属于加分
