---
title: [NODE-747] 笔试题——实现 Redis 大 key 扫描与渐进治理？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-747：手写大 key 治理

**需求与边界**：
- 需求：Redis 大 key 治理（SCN-NODE-689）——① SCAN 扫描（非阻塞——不用 KEYS 全量阻塞）；② 大 key 检测（type+size——MEMORY USAGE 采样）；③ 渐进删除（hscan 分批 hdel + unlink 异步）；④ 拆分建议（大 hash 拆桶——阈值报告）。
- 边界：① SCAN 的 COUNT 调优（每批大小——扫描时长控制）；② 删除排程低峰（阻塞影响窗口）；③ 写入预防（应用层单值上限——SCN-NODE-689 预防优于治理）。

**答**：
```javascript
async function scanBigKeys(redis, { thresholdMB = 1 } = {}) {
  const big = [];
  let cursor = '0';
  do {
    const [next, keys] = await redis.scan(cursor, { COUNT: 200 });   // 非阻塞扫描
    cursor = next;
    for (const k of keys) {
      const type = await redis.type(k);
      let size = 0;
      if (type === 'hash' || type === 'zset') size = await redis.hlen(k) ?? 0;   // 元素数
      const mem = await redis.memory('usage', k).catch(() => 0);   // 内存采样
      if (mem > thresholdMB * 1e6)
        big.push({ key: k, type, mem, elems: size });
    }
  } while (cursor !== '0');
  return big.sort((a, b) => b.mem - a.mem);
}
async function gradualDelete(redis, key) {             // 渐进删除（SCN-NODE-689）
  let cursor = 0;
  do {
    const [next, items] = await redis.hscan(key, cursor, { COUNT: 100 });
    if (items.length) await redis.hdel(key, items.filter((_, i) => i % 2 === 0));
    cursor = next;
    await sleep(50);                                   // 限速（不阻塞主线程）
  } while (cursor !== '0');
  await redis.unlink(key);                             // 异步删壳（SCN-NODE-689）
}
```

**评分点**:
- SCAN 非阻塞（不用 KEYS——主线程保护）。
- 渐进删除（hscan 分批 + sleep 限速 + unlink 异步——SCN-NODE-689）。
- 大 key 报告排序（治理优先级）。
- 写入预防意识（应用层单值上限——治理优于修复）。
