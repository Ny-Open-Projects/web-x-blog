---
title: [HW-401] 手写一个编辑器 API 设计：命令面、事件面与数据面分层
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-401：手写一个编辑器 API 设计：命令面、事件面与数据面分层

**答**：
- 需求：实现 EditorAPI：三层设计——命令层（execCommand(name, args)，幂等可组合）、事件层（on/once/off，事件分类：change/selection/destroy，含事件载荷 schema）、数据层（getDoc/setDoc/serialize，数据不可变引用约定）；层间约束（命令触发事件，数据层只读给外部）。
- 边界：事件载荷不可变（冻结对象）；命令返回值统一（{ok, value?|error}）；API 版本化（v2 命名空间）；废弃策略（旧 API 标记 deprecated + 迁移提示）。
- 评分点：三层职责清晰；载荷不可变；版本化。

```javascript
class EditorAPI {
  constructor(kernel) { this.kernel = kernel; this.events = new Map(); }
  // ── 命令层：幂等可组合 ──
  async execCommand(name, args) {
    const cmd = COMMANDS[name];
    if (!cmd) return { ok: false, error: `unknown-command: ${name}` };
    try {
      const value = await cmd(this.kernel, args);
      this.kernel.emit('change', { type: name, args });      // 命令触发事件
      return { ok: true, value };
    } catch (e) { return { ok: false, error: String(e) }; }  // 统一返回
  }
  // ── 事件层：分类订阅 ──
  on(event, fn) {
    const EVENTS = new Set(['change', 'selection', 'destroy']);
    if (!EVENTS.has(event)) throw new Error('bad-event: ' + event);
    const set = this.events.get(event) ?? new Set();
    set.add(fn); this.events.set(event, set);
    return () => set.delete(fn);                             // 返回退订函数
  }
  emit(event, payload) {                                     // 载荷不可变
    const frozen = Object.freeze({ ...payload, ts: Date.now() });
    this.events.get(event)?.forEach(fn => fn(frozen));
  }
  // ── 数据层：只读给外部 ──
  getDoc() { return Object.freeze(structuredClone(this.kernel.doc)); }   // 不可变快照
  setDoc(doc) { this.kernel.replaceDoc(deepFreeze(structuredClone(doc))); }
  serialize(fmt = 'json') { return SERIALIZERS[fmt](this.kernel.doc); }
}
const deepFreeze = o => { Object.freeze(o);
  for (const v of Object.values(o)) if (v && typeof v === 'object') deepFreeze(v);
  return o; };
// v2 命名空间：api.v2.execCommand(...)，旧 api.execCommand 标记 deprecated
```
