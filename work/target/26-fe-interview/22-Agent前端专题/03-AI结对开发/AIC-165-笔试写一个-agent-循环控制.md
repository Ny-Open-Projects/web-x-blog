---
title: [AIC-165] 笔试：实现一个 Agent 循环控制器：最多 N 轮、无进展检测、终止条件与最终报告？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-165：笔试：实现一个 Agent 循环控制器：最多 N 轮、无进展检测、终止条件与最终报告？
**答**：实现 `runAgent(step, { maxSteps, verify })`：
- 每轮调 `step()` 返回 `{action, done?}`；`verify()` 判定任务是否达成（如测试通过）；
- 终止条件：verify 通过 / agent 自报 done / 达到 maxSteps / 无进展（连续 3 轮文件改动哈希不变）；
- 每轮记录 trace（动作 + 结果 + token）；结束输出报告 `{status, steps, traces, summary}`；
- verify 失败且达上限时 status='failed' 并附「未达成项」。

```javascript
import { createHash } from 'crypto';

function runAgent(step, { maxSteps = 10, verify, onTrace = () => {} }) {
  const traces = [];
  let stall = 0, lastState = '';

  for (let i = 1; i <= maxSteps; i++) {
    const s = step();
    const stateHash = createHash('md5')
      .update(JSON.stringify(s.files ?? s)).digest('hex').slice(0, 8);
    const progressed = stateHash !== lastState;
    stall = progressed ? 0 : stall + 1;
    lastState = stateHash;

    traces.push({ step: i, action: s.action, stateHash, progressed });
    onTrace(traces.at(-1));

    if (s.done) return report('done', traces, 'agent 自报完成');
    if (verify()) return report('done', traces, `verify 通过（第 ${i} 轮）`);
    if (stall >= 3) return report('stalled', traces, '连续 3 轮无进展，提前止损');
  }
  return report('failed', traces, `达到 ${maxSteps} 轮上限，verify 未通过`);
}
function report(status, traces, summary) {
  const unmet = status === 'failed' ? traces.filter(t => !t.progressed).length : 0;
  return { status, steps: traces.length, traces, summary, unmetHints: unmet };
}

// 测试：模拟一个第二轮就修好的 agent
let round = 0;
const files = { a: 'v1' };
const result = runAgent(() => {
  round++;
  if (round === 2) files.a = 'v2';
  return { action: `edit a.ts (round ${round})`, files, done: false };
}, { maxSteps: 5, verify: () => files.a === 'v2' });
console.log(result.status, result.summary); // done verify 通过（第 2 轮）
```

**评分点**：
1. 四类终止条件齐备（verify/自报/上限/无进展），漏「无进展检测」会让烂 agent 空转烧钱；
2. 无进展判定用状态哈希而非 action 文本——agent 可以换个说法重复同一动作；
3. 每轮 trace 完整可回放（AIC-085），trace 含 progressed 便于分析卡点；
4. verify 优先级高于 agent 自报 done——防止 agent 声称完成实际没完成（窗口幻觉）；
5. failed 报告附未达成线索，衔接人工接管。
