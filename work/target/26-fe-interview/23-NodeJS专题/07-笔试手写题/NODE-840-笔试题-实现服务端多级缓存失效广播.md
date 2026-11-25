---
title: [NODE-840] 笔试题——实现多级缓存失效广播（pub/sub + 断点补漏）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-840：手写失效广播

**需求与边界**：
- 需求：缓存失效广播（SCN-NODE-727）——① pub/sub 广播失效（SCN-NODE-727）；② 失效消息丢失的补漏（失效版本号——断点补漏，SCN-NODE-640 seq 空洞语义）；③ 批量失效合并（SCN-OPS-320）；④ 失效与写路径联动（SCN-FIN-688）。
- 边界：① 失效消息的 seq 单调（空洞检测——SCN-FIN-628 seq 补漏）；② 重连补漏（resumeFrom——SCN-NODE-628 断线补增量）；③ 广播风暴防御（SCN-OPS-320 合并）。

**答**：
```javascript
function invalidateBus() {
  let seq = 0;
  return {
    async invalidate(keys) {                           // 批量失效（SCN-OPS-320 合并）
      await redis.del(...keys);
      await redis.publish('cache:inv', JSON.stringify({ keys, seq: ++seq }));
    },
    subscribe(instanceL1) {
      redisSub.subscribe('cache:inv');
      redisSub.on('message', (ch, raw) => {
        const { keys, seq: s } = JSON.parse(raw);
        if (s > this.lastSeq + 1) this.resync();       // seq 空洞：全量 resync（SCN-NODE-640 兜底）
        this.lastSeq = s;
        keys.forEach(k => instanceL1.delete(k));
      });
      redisSub.on('reconnect', () => this.resync());   // 重连补漏（SCN-NODE-628 resumeFrom 语义）
    },
  };
}
```

**评分点**:
- pub/sub 广播失效（SCN-NODE-727）。
- seq 空洞检测 + 全量 resync（消息丢失兜底——SCN-NODE-640 最终一致）。
- 重连补漏（SCN-NODE-628 resume 语义）。
- 批量失效合并（SCN-OPS-320）。
