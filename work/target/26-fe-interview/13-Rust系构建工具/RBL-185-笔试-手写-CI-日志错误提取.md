---
title: [RBL-185] 笔试：手写 CI 日志解析器（阶段耗时 + 错误提取）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-185：笔试：手写 CI 日志解析器（阶段耗时统计 + 错误上下文提取）

**答**：写 parse-log.mjs：1) 输入 CI 原始日志（行数组，形如 `[11:02:11] START build` / `[11:02:35] END build ok` / 堆栈错误行）；2) 解析每个阶段的耗时（START/END 配对，输出秒）；3) 提取错误：匹配 `Error:`、`ERROR in`、`FAILED` 开头行，带其后 5 行上下文，同源错误去重（按 message hash）；4) 输出结构化 {stages, errors}；5) 未配对 START（阶段中断）标记为 aborted 并用日志总时长封顶。

```javascript
// parse-log.mjs
import { createHash } from 'node:crypto';

const HHMMSS = s => { const [h, m, sec] = s.split(':').map(Number); return h * 3600 + m * 60 + sec; };
const ERR_RE = /^(?:.*(?:Error:|ERROR in|FAILED\b).*)$/;

export function parseLog(lines) {
  const stages = {}, errors = [], open = new Map();
  const firstTs = HHMMSS(lines[0]?.match(/^\[(\d\d:\d\d:\d\d)\]/)?.[1] ?? '0:0:0');
  let lastTs = firstTs, errSeen = new Set();

  lines.forEach((line, i) => {
    const m = line.match(/^\[(\d\d:\d\d:\d\d)\]/);
    if (m) lastTs = HHMMSS(m[1]);

    const s = line.match(/START (\S+)/);
    const e = line.match(/END (\S+) (ok|failed)/);
    if (s) open.set(s[1], lastTs);                          // 记录开始时间
    if (e) {
      const t0 = open.get(e[1]);
      stages[e[1]] = { dur: t0 === undefined ? null : lastTs - t0,
        status: e[2], aborted: t0 === undefined };
      open.delete(e[1]);
    }
    if (ERR_RE.test(line.trim())) {
      const ctx = lines.slice(i, i + 6).join('\n');         // 错误 + 5 行上下文
      const key = createHash('md5').update(line.trim()).digest('hex');
      if (!errSeen.has(key)) { errSeen.add(key); errors.push({ line: i + 1, message: line.trim(), context: ctx }); }
    }
  });
  for (const [name, t0] of open)                            // 未配对：中断
    stages[name] = { dur: lastTs - t0, status: 'aborted', aborted: true };
  return { stages, errors };
}
// 示例日志：
// [11:02:11] START build
// [11:02:12] ERROR in ./src/a.ts  Type 'string' is not assignable...
// [11:02:35] END build failed
// → stages.build = { dur: 24, status: 'failed' }, errors[0].context 含类型错误 5 行
```
**评分点**：
- START/END 配对统计（含未配对中断处理，用最后时间戳封顶）。
- 错误按 message 去重（重复堆栈只留一条）。
- 上下文窗口固定 5 行且不越界。
- 时间解析用秒数差而非字符串比较（跨分钟正确）。
- 结构化输出可直接喂告警/PR 评论。
