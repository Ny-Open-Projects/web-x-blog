---
title: [AGT-461] 笔试题——实现多 Agent 共享事实库（写入校验+订阅广播+幻觉扩散防护）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-461：手写共享事实库：写入校验、来源与时间戳、订阅通知、扩散防护

**需求与边界**：
- 输入：事实写入/查询请求；输出：事实库服务。
- 边界要求：① 写入校验（必须有来源 Agent 与依据引用——无依据事实拒绝）；② 事实带来源/时间/置信度；③ 订阅者按维度收到变更通知；④ 单 Agent 撤回事实时联动清理（引用它的下游通知复核）。

**答**：
```javascript
class SharedFacts {
  constructor() { this.facts = new Map(); this.subs = new Map(); }
  async write({ text, dim, by, evidence }, { verify }) {
    // 1. 写入校验：来源+依据必填（无依据 = 幻觉扩散入口）
    if (!by) throw new Error('缺来源 Agent');
    if (!evidence?.length)
      throw new Error('事实必须附依据引用');
    const ok = await verify(text, evidence);      // 依据真实性抽验
    if (!ok) return { accepted: false,
      reason: '依据校验未通过' };
    const fact = { id: uid(), text, dim, by, evidence,
      ts: Date.now(), confidence: ok.score };
    // 2. 同维度冲突：标记而非覆盖
    const olds = [...this.facts.values()]
      .filter(f => f.dim === dim && contradicts(f.text, text));
    fact.conflictsWith = olds.map(o => o.id);
    this.facts.set(fact.id, fact);
    // 3. 订阅广播
    this.notify(dim, { type: 'added', fact });
    // 4. 撤回联动：删除时通知引用者复核
    this.retract = async (id) => {
      const dependents = [...this.facts.values()]
        .filter(f => f.evidence.some(e => e.factId === id));
      this.facts.delete(id);
      this.notify(dim, { type: 'retracted', id,
        review: dependents.map(d => d.id) });     // 下游复核清单
    };
    return { accepted: true, fact };
  }
  get(query, { dim }) {
    return [...this.facts.values()]
      .filter(f => !dim || f.dim === dim)
      .sort((a, b) => b.confidence - a.confidence);
  }
  subscribe(dim, fn) {
    (this.subs.get(dim) ?? this.subs.set(dim, []).get(dim)).push(fn);
  }
  notify(dim, ev) { (this.subs.get(dim) ?? [])
    .forEach(fn => fn(ev)); }
}
```

**评分点**:
- 写入校验（来源+依据引用+真实性抽验）阻断幻觉扩散入口。
- 冲突标记不覆盖（同维度矛盾双保留）。
- 订阅按维度广播；撤回联动通知下游复核（依赖清理）。
- 事实带来源/时间/置信度（可审计可衰减）。
