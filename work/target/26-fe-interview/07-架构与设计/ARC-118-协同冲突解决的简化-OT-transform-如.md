---
title: [ARC-118] 协同冲突解决的简化 OT transform 如何实现？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-118：协同冲突解决的简化 OT transform 如何实现？
**答**：
- 核心问题：A、B 基于同一版本并发产生两个操作，应用到同一状态必须收敛。transform 计算出"对方操作对我操作位置的影响"，互相调整偏移与长度。
- 服务端定序模型：服务端收到 op 后与"已提交但未包含它"的操作做 transform，得到服务端版本的操作；客户端收到远端 op 后也要与本地未确认操作做 transform 再应用。
- 实现要点：insert 与 insert 比较 pos 先后（同位置用 clientId 打破对称）；insert 与 delete 组合要处理"删区包含插入点"；简化版可先只处理单字符操作再泛化。
- 工程建议：生产环境不要手写完整 OT（组合/属性/undo 的 transform 极复杂），用成熟库；手写 transform 用于理解原理与面试表达。

```typescript
// 简化 OT transform：两个并发操作的互相变换（纯文本）
interface Op { type: 'insert' | 'delete'; pos: number; text?: string; len?: number }

function transform(a: Op, b: Op): Op {
  // 返回 a'：b 先应用之后，a 应该变成什么样
  if (a.type === 'insert') {
    if (a.pos <= b.pos) return a;                          // a 在 b 之前插入（含同位置，a 先插），位置不变
    if (b.type === 'insert') {
      return { ...a, pos: a.pos + b.text!.length };        // a 在 b 之后：右移 b 的长度
    }
    // b 是 delete：a.pos 在删区左侧不动；在删区内部塌缩到删区起点；在右侧左移删区长度
    const bEnd = b.pos + (b.len ?? 0);
    if (a.pos <= bEnd) return { ...a, pos: b.pos };
    return { ...a, pos: a.pos - (b.len ?? 0) };
  }
  // a 是 delete：把删除区间的两端按 b 造成的坐标变化重新映射
  const mapPos = (p: number) => (p <= b.pos ? p : b.type === 'insert' ? p + b.text!.length : p);
  const aStart = mapPos(a.pos), aEnd = mapPos(a.pos + a.len!);
  if (b.type === 'insert') {
    // b 插在 a 的删除区间中间时，aStart 不动、aEnd 右移，区间自然变长
    // 注：单区间 delete 无法精确表达"delete 与落在其区间内的 insert 并发"（正确结果要拆成两段删除），
    // 此处按"并发插入的文字一并删除"处理；完整实现需把 delete 拆分为两段 op
    return { ...a, pos: aStart, len: aEnd - aStart };
  }
  // b 也是 delete：b 删掉且落在 a 区间内的字符要从 a 的区间里扣除
  const bEnd = b.pos + (b.len ?? 0);
  const cut = (p: number) => p - Math.max(0, Math.min(bEnd, p) - b.pos);
  return { ...a, pos: cut(Math.min(aStart, aEnd)), len: Math.max(0, cut(aEnd) - cut(aStart)) };
}
// 服务端使用：incoming 与所有 pending op 做 transform(incoming, pending) 后提交
// 客户端使用：收到远端 op 后 transform(remote, localPending) 再应用到本地
```
