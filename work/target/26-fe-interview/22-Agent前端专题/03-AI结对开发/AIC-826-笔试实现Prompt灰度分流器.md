---
title: [AIC-826] 笔试：实现 Prompt 灰度分流器（粘性哈希 + 比例放量 + 强制回滚）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-826：笔试：实现 Prompt 灰度分流器（粘性哈希 + 比例放量 + 强制回滚）
**答**：
- 核心需求：实现 `SplitBucket`，支持 `setConfig(versions: { version, weight }[])`、`assign(key): version`、`rollback()`。`weight` 为百分比可直接配（如 5 表示 5%），总和允许 != 100（余数归到第一个版本）；`assign` 对同一 `key` 必须稳定返回同一版本；`rollback` 立即让所有流量回到首个版本。
- 边界：空配置返回 `'default'`；weight 为负或 NaN 视为 0；key 为空时用固定桶；配置变更正在进行的请求不受影响（快照语义）。
- 稳定性：用 FNV-1a 之类的确定性哈希，不能用 `Math.random()`；同一 key 不同配置权重变化时允许重新分布，但相同配置必须稳定。
- 追问钩子：追问「如何统计每个版本的实际流量是否偏离配置」——能答出「按版本埋点 + 卡方检验判断是否显著偏离」的候选人把分流和度量闭环了。

```typescript
type Version = { version: string; weight: number };

function fnv1a(s: string): number {
  let h = 0x811c9dc5;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h;
}

class SplitBucket {
  private config: Version[] = [];
  private snapshot: Version[] = []; // 配置变更的快照，保证单次 assign 一致
  setConfig(versions: Version[]) {
    this.config = (versions ?? []).map(v => ({
      version: v.version,
      weight: Number.isFinite(v.weight) && v.weight > 0 ? v.weight : 0,
    }));
  }
  rollback() {
    this.config = this.config.map((v, i) => ({ ...v, weight: i === 0 ? 100 : 0 }));
  }
  assign(key: string): string {
    this.snapshot = this.config.length ? this.config : [{ version: 'default', weight: 100 }];
    const bucket = fnv1a(key || '__empty__') % 100;
    let acc = 0;
    for (const v of this.snapshot) {
      acc += v.weight;
      if (bucket < acc) return v.version;
    }
    return this.snapshot[0].version; // 余数兜底
  }
}

const sb = new SplitBucket();
sb.setConfig([{ version: 'p7', weight: 95 }, { version: 'p8', weight: 5 }]);
console.log(sb.assign('user-A'), sb.assign('user-A')); // 稳定一致
sb.rollback();
console.log(sb.assign('user-A')); // 'p7' 立即全量回滚
```
**评分点**：
- 使用确定性哈希（FNV-1a），禁止 Math.random，保证粘性。
- weight 非法值（负/NaN）归零，空配置兜底 `default`。
- 余数兜底到首个版本，保证任何 key 都有返回值。
- `rollback` 即时生效且无需等待请求完成（配置快照语义）。
- 能讨论「配置变更导致用户版本跳变」的取舍属于加分项。
