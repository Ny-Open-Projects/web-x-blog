---
title: [RBL-181] 笔试：手写并行任务 runner（限流 + 失败快速终止）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-181：笔试：手写并行任务 runner（并发限流 + fail-fast + 超时 kill）

**答**：写 task-runner.mjs：1) 输入命令数组（如 ['pnpm --filter a build', ...]）与并发度 N；2) 用 child_process.spawn 并发执行，同时最多 N 个；3) fail-fast：任一命令非零退出，不再派发新任务，等待在跑任务结束（或 --hard 立即 kill 全部）；4) 每任务支持超时（默认 5min）超时 kill 并计为失败；5) 输出每个任务耗时与状态汇总，退出码 = 失败数 >0 ? 1 : 0。

```javascript
// task-runner.mjs
import { spawn } from 'node:child_process';

function runCmd(cmd, timeoutMs) {
  return new Promise(resolve => {
    const t0 = performance.now();
    const p = spawn(cmd, { shell: true, stdio: ['ignore', 'pipe', 'pipe'] });
    let killed = false;
    const timer = setTimeout(() => { killed = true; p.kill('SIGKILL'); }, timeoutMs);
    let out = '';
    p.stdout.on('data', d => out += d);
    p.stderr.on('data', d => out += d);
    p.on('exit', code => {
      clearTimeout(timer);
      resolve({ cmd, code, killed, log: out, ms: performance.now() - t0 });
    });
    p.on('error', () => { clearTimeout(timer); resolve({ cmd, code: -1, killed: false, log: out, ms: 0 }); });
  });
}

export async function runAll(cmds, { concurrency = 4, timeoutMs = 300_000, failFast = true, hard = false } = {}) {
  const queue = [...cmds];
  const results = [];
  let failed = false;
  const worker = async () => {
    while (queue.length) {
      if (failFast && failed) return;              // 不再派发新任务
      const cmd = queue.shift();
      const r = await runCmd(cmd, timeoutMs);
      results.push(r);
      if (r.code !== 0) {
        failed = true;
        console.error(`FAIL ${cmd} (${(r.ms / 1000).toFixed(1)}s)`);
        if (hard) process.kill(-process.pid, 'SIGTERM'); // 粗化：硬终止模式
      } else {
        console.log(`OK   ${cmd} (${(r.ms / 1000).toFixed(1)}s)`);
      }
    }
  };
  await Promise.all(Array.from({ length: Math.min(concurrency, cmds.length) }, worker));
  const ok = results.filter(r => r.code === 0).length;
  console.log(`summary: ${ok}/${results.length} ok, dispatched=${results.length}/${cmds.length}`);
  return { results, failed, exit: failed ? 1 : 0 };
}
// 若作为 CLI：process.argv.slice(2) 为命令列表，末尾 process.exit(exit)。
```
**评分点**：
- 并发池 = 固定 N 个 worker 消费队列（不是每任务一个 spawn）。
- fail-fast 语义：停派发但等在跑任务收尾（hard 模式可选）。
- 超时 kill + killed 标记进结果。
- 汇总输出包含"派发了多少/总数多少"（failFast 丢失量可见）。
- 退出码语义正确。
