---
title: [AGT-420] 笔试题——实现 Agent 审计 trace 记录器（决策链+脱敏+回放）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-420：手写 trace 记录器：任务根/span 树、上下文快照、脱敏、回放接口

**需求与边界**：
- 输入：任务事件流（llm/tool/approval 事件）；输出：可回放 trace。
- 边界要求：① trace_id/causality 链（span 关联父 span）；② 敏感字段脱敏（password/token/身份证模式）后存储但保留原文指纹（hash 可比对）；③ 回放可按任务还原完整决策链；④ 采样与分级存储（敏感任务全量、普通任务采样）。

**答**：
```javascript
class Tracer {
  constructor({ sink, sample = 0.1 }) {
    this.sink = sink; this.sample = sample;
    this.tasks = new Map();
  }
  startTask(taskId, meta) {
    this.tasks.set(taskId, { id: taskId, meta, spans: [],
      fullAudit: meta.riskLevel === 'high' ||
                 Math.random() < this.sample });   // 分级采样
    return taskId;
  }
  span(taskId, span) {
    const t = this.tasks.get(taskId); if (!t) return;
    if (!t.fullAudit) return;                       // 采样外跳过
    t.spans.push({ ...span, id: span.id ?? uid(),
      parent: span.parent ?? t.spans.at(-1)?.id,    // causality 链
      ts: Date.now(),
      input: redact(span.input), output: redact(span.output),
      inputHash: hash(span.input), outputHash: hash(span.output),
      model: span.model, promptVer: span.promptVer, // 版本留痕
      cost: span.cost ?? 0 });
  }
  async flush(taskId) {
    const t = this.tasks.get(taskId); if (!t) return;
    await this.sink.save(t); this.tasks.delete(taskId);
  }
  replay(taskId) {                                  // 回放决策链
    const t = this.sink.load(taskId);
    return t.spans.map(s => ({ step: s.id, parent: s.parent,
      type: s.type, input: s.input, output: s.output,
      integrity: hash(s.input) === s.inputHash ? 'ok' : 'tampered' }));
  }
}
const redact = (v) => JSON.parse(JSON.stringify(v ?? null), (k, val) =>
  /password|token|secret/i.test(k) ? '***' :
  (typeof val === 'string' && /\d{17}[\dXx]/.test(val)
    ? val.replace(/\d{6}\d{8}\d{3}[\dXx]/, '***') : val));
```

**评分点**:
- span 树带 causality（parent 链）可回放完整决策链。
- 脱敏分层：字段名级（password/token）+ 模式级（身份证），原文 hash 保留可校验篡改。
- 版本留痕（model/promptVer）满足审计要求；分级采样控制存储成本。
- 回放接口含完整性校验（hash 比对）——审计 trace 自身防篡改。
