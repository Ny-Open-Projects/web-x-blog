---
title: [SCN-982] 医疗健康 App 的数据同步（可穿戴设备）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-982：医疗健康 App 的数据同步（可穿戴设备）

**答**：
- 同步：蓝牙同步（手环步数/心率）批量上传、失败重试、去重（时间戳幂等）。
- 频率：自动同步每 30 分钟 + 手动同步；后台低功耗策略（301）。
- 展示：同步状态（最后同步时间/失败原因）。

```javascript
// 可穿戴同步
class WearableSync {
  constructor(device) { this.device = device; }
  async sync(lastTs) {
    const records = await this.device.pull(lastTs);    // 增量拉取
    const dedup = records.filter(r => !synced.has(r.ts));
    for (let i = 0; i < dedup.length; i += 100)
      await api('/health/sync', { batch: dedup.slice(i, i + 100) });
    return { synced: dedup.length,
      lastTs: dedup[dedup.length - 1]?.ts ?? lastTs };
  }
}
```
