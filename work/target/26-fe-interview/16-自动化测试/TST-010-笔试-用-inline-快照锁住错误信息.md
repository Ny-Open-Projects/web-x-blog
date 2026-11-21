---
title: [TST-010] 笔试：用 toMatchInlineSnapshot 锁住一段格式化输出
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-010：笔试：用 toMatchInlineSnapshot 锁住一段格式化输出
**答**：
- 需求：`formatOrder(order)` 输出多行文本，要求把期望值直接写在测试代码里（inline 快照），断言失败时能用 `-u` 自动回填。
- 要点：`toMatchInlineSnapshot()` 不传参数时首跑自动把实际值序列化写进源码（AST 定位插入），后续变成精确比对。
- 边界：动态字段（时间戳、随机 ID）要在被序列化对象上先抹掉或映射，否则快照永远失败；快照不应包含过多无关字段。

```javascript
// src/format.test.ts
import { describe, it, expect } from 'vitest';
import { formatOrder } from './format';

describe('formatOrder', () => {
  it('输出订单摘要（inline 快照）', () => {
    const order = { id: 'ORD-1', items: ['键盘', '鼠标'], total: 649, createdAt: '2026-01-01' };
    const out = formatOrder({ ...order, createdAt: 'FIXED' }); // 抹掉动态时间
    expect(out).toMatchInlineSnapshot(`
      "订单 ORD-1
      商品: 键盘、鼠标
      合计: ¥649.00"
    `); // 首跑为空时 vitest -u 会自动填入上面内容
  });
});

// 更新命令：npx vitest run -u
// 手动删除快照内容留空 expect(out).toMatchInlineSnapshot() 再 -u 可整段重新生成。
```
**评分点**：
- 知道 inline 快照首跑自动写入源码、-u 更新的机制。
- 动态字段固定化处理（时间/随机值）。
- 能对比外部快照文件（toMatchSnapshot）说明取舍：inline 可读性高、适合小快照。
