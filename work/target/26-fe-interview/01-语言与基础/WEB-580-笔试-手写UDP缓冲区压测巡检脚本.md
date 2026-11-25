---
title: [WEB-580] 笔试：手写 UDP 缓冲区健康巡检脚本（Node）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, HTTP3]
type: 笔试题
---

## WEB-580：笔试：手写 UDP 缓冲区健康巡检脚本（Node）

**答**：实现 Node 巡检脚本 `checkUdpHealth()`：① 读取 `/proc/net/udp` 统计 drops 列（第 5 列为丢弃计数）总和；② 读取当前 `rmem_max`/`wmem_max`（`/proc/sys/net/core/rmem_max`）；③ 判定规则：drops > 0 为 `critical`；rmem_max < 16MB 为 `warn`；否则 `ok`；④ 每 60s 巡检一次，状态变化时输出告警行并记录时间。用 fs 同步读 + 错误兜底（非 Linux 环境跳过）。

```javascript
const fs = require('fs');

function readNum(p) { try { return parseInt(fs.readFileSync(p, 'utf8').trim(), 10); } catch { return NaN; } }

function parseDrops() {
  try {
    const lines = fs.readFileSync('/proc/net/udp', 'utf8').split('\n').slice(1);
    let drops = 0;
    for (const line of lines) {
      const cols = line.trim().split(/\s+/);
      const d = parseInt(cols[4], 16);  // drops 列(十六进制)
      if (Number.isFinite(d)) drops += d;
    }
    return drops;
  } catch { return -1; }
}

function checkOnce() {
  const drops = parseDrops();
  const rmem = readNum('/proc/sys/net/core/rmem_max');
  if (drops < 0) return { state: 'skip', note: 'non-linux' };
  if (drops > 0) return { state: 'critical', drops, rmem };
  if (rmem < 16 * 1024 * 1024) return { state: 'warn', drops, rmem };
  return { state: 'ok', drops, rmem };
}

let last = null;
setInterval(() => {
  const cur = checkOnce();
  if (cur.state !== last) console.log(new Date().toISOString(), JSON.stringify(cur));
  last = cur.state;
}, 60_000);
```

**评分点**：
- /proc/net/udp drops 列为十六进制且解析有兜底
- 双条件分级（critical 优先于 warn）逻辑顺序正确
- 非 Linux 环境优雅跳过（catch 返回 NaN/-1）
- 状态变化才告警，避免重复刷屏；说明该巡检对 QUIC 服务为何关键（单 socket 多流、突发丢弃不可见于应用层）
