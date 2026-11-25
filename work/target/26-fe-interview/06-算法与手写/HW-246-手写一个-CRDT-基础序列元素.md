---
title: [HW-246] 手写一个 CRDT 基础序列元素：唯一 ID 与偏序比较
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-246：手写一个 CRDT 基础序列元素：唯一 ID 与偏序比较

**答**：
- 需求：实现 CRDT 基础：每个字符元素 {id: [siteId, counter], ch, deleted}；比较函数 compare(a, b) 定义全序（counter 先比，相同 siteId 大者后——保证并发插入收敛顺序）；doc 结构为按序元素数组；localInsert 生成递增 counter。
- 边界：同 site 插入顺序按 counter 单调；不同 site 并发插入的顺序由 compare 决定（确定性，任何站点重放一致）；id 不可变。
- 评分点：全序定义确定性；counter 单调；tombstone 占位。

```javascript
class CRDTDoc {
  constructor(siteId) { this.site = siteId; this.counter = 0; this.items = []; }
  localInsert(idx, ch) {
    const id = [this.site, ++this.counter];
    const left = this.items[idx - 1]?.id ?? [null, 0];
    const right = this.items[idx]?.id ?? null;
    const item = { id, ch, left, right, deleted: false };
    this.insertSorted(item);
    return item;
  }
  insertSorted(item) {                                     // 按 left/right 链序插入
    let i = this.items.findIndex(it => sameId(it.id, item.right));
    if (i < 0) i = this.items.length;
    // 并发插入到同位置：按 id 全序（site 大者在后，保证各站点一致）
    while (i > 0 && compareId(this.items[i - 1].id, item.id) > 0
      && sameId(this.items[i - 1].right, item.right)) i--;
    this.items.splice(i, 0, item);
  }
  remoteApply(item) { this.insertSorted({ ...item, deleted: item.deleted }); }
  text() { return this.items.filter(i => !i.deleted).map(i => i.ch).join(''); }
}
function compareId(a, b) {                                 // 全序：先 counter 后 site
  if (a[1] !== b[1]) return a[1] - b[1];
  return (a[0] ?? '') < (b[0] ?? '') ? -1 : (a[0] ?? '') > (b[0] ?? '') ? 1 : 0;
}
const sameId = (a, b) => JSON.stringify(a) === JSON.stringify(b);
```

## 补充：评分点与变体

**评分点**：

- 全序必须确定性：先比 counter 再比 siteId，任何站点以任意顺序重放都要得到同一顺序
- 同站点 counter 严格单调递增，这是「同 site 内插入保序」的唯一依据
- 插入要按 compare 找到位置再插，直接 push 会让并发插入顺序依赖到达时间，不收敛
- tombstone 只置 deleted 不删元素，删掉后后续插入失去定位锚点

**变体与延伸**：

1. 两站点同时在同一位置插入 → 由 id 全序决定先后，所有站点收敛到同一结果，这是收敛性的核心验证点
2. 每个字符一个对象导致内存爆炸 → 改块编码，连续字符合并为一个 item（Yjs 的思路）
3. 要支持移动操作（拖拽段落）→ 引入 move op 并保证不产生引用环，或先用 delete + insert 近似
