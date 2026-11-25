---
title: [TST-019] Vitest 的并发测试（concurrent / sequence）怎么用？有什么坑？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-019：Vitest 的并发测试（concurrent / sequence）怎么用？有什么坑？
**答**：
- 文件级并行：Vitest 默认多个 worker 并行跑不同测试文件（pool: threads/forks），文件之间天然隔离，这是主要的加速来源。
- 用例级并行：`it.concurrent`（或 test.concurrent）让同一 describe 内的用例并发跑，适合互相独立的 IO 型用例；配 `sequence.concurrent: true` 可全局开启。
- 大坑：concurrent 用例共享同一环境（同一 window/mock 状态），只有用例内不触碰共享状态的才安全；jsdom 下并发操作 DOM 会互相踩。
- 钩子关系：concurrent 用例不共享 beforeEach 的串行语义，前置条件要用 fixture 或在每个用例内部自建。
- 追问钩子：想跑「同一文件内顺序无关」的验证，先用随机顺序（sequence.shuffle）找出顺序依赖，比直接 concurrent 更稳。

```typescript
describe('纯计算用例可并发', () => {
  it.concurrent('A 计算', async ({ expect }) => { expect(await calc(1)).toBe(2); });
  it.concurrent('B 计算', async ({ expect }) => { expect(await calc(2)).toBe(4); });
});

// vitest.config.ts
export default defineConfig({
  test: {
    pool: 'threads',          // fork: 进程隔离更彻底，threads 更快
    sequence: { shuffle: true }, // 本地验证顺序依赖
    maxWorkers: '50%',        // 控制 CPU 占用
  },
});
```
