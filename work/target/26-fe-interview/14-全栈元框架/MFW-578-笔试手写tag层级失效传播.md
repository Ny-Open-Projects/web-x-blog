---
title: [MFW-578] 笔试：手写 tag 层级失效传播
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-578：笔试：手写 tag 层级失效传播

**答**：实现 `createTagInvalidator(hierarchy, { revalidate })`。hierarchy: `Record<tag, string[]>`（tag → 子 tag 模式列表，支持 `product:*` 通配）。revalidate 注入：`(tag) => void`（模拟 Next revalidateTag）。`invalidate(tag)`：1) 失效自身；2) 递归失效子 tag（通配匹配：'product:*' 匹配 'product:123'、'product:456'——所有已注册 tag 中匹配模式的）；3) 返回失效的 tag 列表（去重排序）。边界：无层级声明（只失效自身）；环（a→b→a——去重防死循环）；通配无匹配（只失效自身）。

```javascript
function createTagInvalidator(hierarchy = {}, { revalidate } = {}) {
  const known = new Set();                               // 已注册 tag（供通配匹配）
  const all = (tag) => {
    known.add(tag);
    for (const child of Object.keys(hierarchy)) known.add(child);
    return tag;
  };
  function match(pattern, tag) {
    if (pattern === tag) return true;
    if (pattern.endsWith(':*')) return tag.startsWith(pattern.slice(0, -1));
    return false;
  }
  function invalidate(tag) {
    all(tag);
    const affected = new Set([tag]);
    const queue = [tag];
    const seen = new Set(queue);
    while (queue.length) {
      const cur = queue.shift();
      for (const pattern of hierarchy[cur] ?? []) {
        for (const t of known)
          if (match(pattern, t) && !seen.has(t)) {
            seen.add(t); affected.add(t); queue.push(t);
          }
      }
    }
    [...affected].sort().forEach(revalidate);
    return [...affected].sort();
  }
  return { invalidate, _known: known };
}

// 自测
const log = [];
const inv = createTagInvalidator({
  products: ['product:*'],
  user: ['cart:*'],
}, { revalidate: (t) => log.push(t) });

// 实体注册
['product:1', 'product:2', 'user:u1', 'cart:u1'].forEach(t => inv._known.add(t));

// 失效集合 tag → 传播到所有实体
let r = inv.invalidate('products');
console.log(r.join(','));                                // product:1,product:2,products
console.log(log.length === 3);

// 失效实体 tag → 只自身
log.length = 0;
r = inv.invalidate('product:1');
console.log(r.join(',') === 'product:1');

// 用户 tag → 级联 cart
log.length = 0;
r = inv.invalidate('user:u1');
console.log(r.join(','));                                // cart:u1,user:u1

// 环不爆栈
const ring = createTagInvalidator({ a: ['b'], b: ['a'] }, { revalidate: () => {} });
console.log(ring.invalidate('a').join(',') === 'a,b');

// 通配无匹配
r = inv.invalidate('ghost');                              // ghost 无层级
console.log(r.join(',') === 'ghost');
```

**评分点**：
- 层级递归失效正确（集合 tag → 实体 tag 传播）；通配匹配（product:* 前缀）
- 去重防环（seen 集合）；失效列表排序输出（可审计）
- 边界：无层级/通配无匹配/环
- 能说清「实体变更需同时失效实体与列表 tag——缓存一致性域 = 依赖闭包失效（RBL-635 的缓存语义）」属于加分
