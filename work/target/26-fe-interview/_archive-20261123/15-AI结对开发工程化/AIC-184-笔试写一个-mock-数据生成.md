---
title: [AIC-184] 笔试：实现一个 mock 数据生成器：按 schema 类型分布生成、脏数据变异与固定 seed 可复现？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-184：笔试：实现一个 mock 数据生成器：按 schema 类型分布生成、脏数据变异与固定 seed 可复现？
**需求**：实现 `genMock(schema, { count, seed, dirtyRate })`：
- schema: `{fields: {name: {type: 'string'|'number'|'boolean'|'enum'|'array', ...opts}}}`；
- 固定 seed 的伪随机（mulberry32），同 seed 同输出；
- dirtyRate 比例的对象做脏数据变异：null/空串/超长/NaN/emoji 超长（真实世界脏数据）；
- enum 按给权分布；array 长度在 min~max 随机。

```javascript
function mulberry32(seed) {
  let a = seed >>> 0;
  return () => {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function genMock(schema, { count = 10, seed = 42, dirtyRate = 0.2 } = {}) {
  const rand = mulberry32(seed);
  const pick = (arr) => arr[Math.floor(rand() * arr.length)];
  const genField = (f) => {
    switch (f.type) {
      case 'string': return pick(f.samples ?? ['商品A', '商品B']);
      case 'number': return f.min + Math.floor(rand() * ((f.max ?? 100) - f.min));
      case 'boolean': return rand() > 0.5;
      case 'enum': {
        let r = rand() * (f.weights ?? f.values.map(() => 1)).reduce((a, b) => a + b, 0);
        for (let i = 0; i < f.values.length; i++) {
          r -= (f.weights ?? [])[i] ?? 1;
          if (r <= 0) return f.values[i];
        }
        return f.values.at(-1);
      }
      case 'array': {
        const len = f.min + Math.floor(rand() * ((f.max ?? f.min + 3) - f.min));
        return Array.from({ length: len }, () => genField(f.items));
      }
    }
  };
  const DIRTY = {
    string: ['', 'x'.repeat(2000), '<img onerror=x>', '😀'.repeat(50)],
    number: [0, -1, NaN],
    boolean: [null],
    array: [[], null],
    enum: [null],
  };
  const out = [];
  for (let i = 0; i < count; i++) {
    const obj = {};
    for (const [name, f] of Object.entries(schema.fields)) obj[name] = genField(f);
    if (rand() < dirtyRate) {                    // 脏数据变异（固定变异字段）
      const key = pick(Object.keys(schema.fields));
      obj[key] = pick(DIRTY[schema.fields[key].type] ?? [null]);
    }
    out.push(obj);
  }
  return out;
}

// 测试
const schema = { fields: {
  title: { type: 'string', samples: ['手机', '耳机'] },
  price: { type: 'number', min: 10, max: 500 },
  status: { type: 'enum', values: ['on', 'off', 'draft'], weights: [0.7, 0.2, 0.1] },
  tags: { type: 'array', min: 0, max: 3, items: { type: 'string', samples: ['hot'] } },
}};
console.log(genMock(schema, { count: 3, seed: 42 }));
console.log(JSON.stringify(genMock(schema, { count: 3, seed: 42 })) ===
            JSON.stringify(genMock(schema, { count: 3, seed: 42 }))); // true 可复现
```

**评分点**：
1. 可复现性：种子化 PRNG（mulberry32 或 LCG），用 Math.random 直接失分——E2E 与测试必须确定性；
2. 脏数据变异覆盖类型化脏值（null/空串/超长/NaN），不是「随机乱改」；
3. enum 权重分布生成（按权重落在连续区间）；
4. 脏变异选择固定字段（pick 字段也用同一 PRNG），保证整体可复现；
5. 追问：敏感字段假名化（人名/手机号用固定假数据池），禁止真实 PII 进 mock。
