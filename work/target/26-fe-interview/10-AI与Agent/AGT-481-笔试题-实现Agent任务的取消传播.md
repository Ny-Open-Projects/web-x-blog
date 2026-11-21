---
title: [AGT-481] 笔试题——实现任务取消传播（级联中止+资源释放+部分结果保留）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-481：手写取消传播：AbortController 级联、下游资源释放、部分结果落库

**需求与边界**：
- 输入：任务树（主任务+子任务+工具调用）；取消请求；输出：级联取消结果。
- 边界要求：① 取消沿依赖树级联（父取消→子取消）；② 每层 abort 信号传递到实际资源（LLM 流/HTTP 请求）；③ 已完成子任务结果保留可复用；④ 取消状态落库（防"僵尸任务"继续计费）。

**答**：
```javascript
class CancellableTask {
  constructor({ id, deps = [], run, store }) {
    this.id = id; this.deps = deps; this.run = run;
    this.store = store;
    this.ac = new AbortController();
    this.children = [];
  }
  spawn(childFactory) {
    const child = childFactory(this.ac.signal);   // 信号传子
    this.children.push(child);
    return child;
  }
  async execute() {
    try {
      const result = await this.run({
        signal: this.ac.signal,
        // 工具调用透传 abort（HTTP/LLM 客户端支持）
        fetchOpts: { signal: this.ac.signal },
      });
      await this.store.saveResult(this.id, result);
      return result;
    } catch (e) {
      if (this.ac.signal.aborted) {
        // 取消：部分结果落库（已完成子任务可复用）
        await this.store.savePartial(this.id, {
          done: this.children.filter(c => c.done)
            .map(c => c.id),
          state: 'cancelled' });
        return { cancelled: true };
      }
      throw e;
    }
  }
  async cancel({ cascade = true } = {}) {
    this.ac.abort();                               // 本级中止
    if (cascade) await Promise.all(
      this.children.map(c => c.cancel?.({ cascade })));
    await this.store.markCancelled(this.id);       // 状态落库
    this.children.length = 0;
    this.ac = new AbortController();               // 不可复用旧信号
  }
}
// 关键点：abort 信号要传到"实际资源"
// （LLM SDK / fetch 均支持 signal）——
// 只标志位不透传 = 假取消，钱照烧。
```

**评分点**:
- AbortController 级联：信号传递到实际资源（LLM 流/HTTP），非标志位假取消。
- 子任务树递归取消；已完成子任务结果落库可复用。
- 取消状态持久化（防僵尸任务继续计费）。
- 取消后信号不可复用（新建 controller）。
