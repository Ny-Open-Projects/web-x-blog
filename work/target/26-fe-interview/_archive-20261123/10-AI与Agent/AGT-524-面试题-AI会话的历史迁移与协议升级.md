---
title: [AGT-524] 前端会话数据协议升级（v1→v2 加了 parts 结构）时，历史数据怎么迁移？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-524：前端会话数据协议升级（v1→v2 加了 parts 结构）时，历史数据怎么迁移

**答**：
- IndexedDB 用版本化 upgrade 回调迁移，迁移逻辑要幂等且可中断续跑（大存量分批，每批 commit）。
- 服务端会话同理：协议版本存字段，读时 lazy migrate（读到旧版本就升级回写），避免一次性停机迁移。
- 迁移要有影子校验：抽样对比迁移前后语义等价（消息数/角色/引用完整），失败告警回滚版本号。

```javascript
idb.open('ai-chat', 2, (s, oldV) => {
  if (oldV < 2) migrateV1toV2(s);   // content: string → parts: []
});
async function migrateV1toV2(store) {
  const all = await store.getAll();
  for (const msg of all) {
    if (msg.parts) continue;        // 幂等：已迁移跳过
    await store.put({ ...msg, parts: [{ type: 'text', value: msg.content }],
      content: undefined, v: 2 });
  }
}
```

