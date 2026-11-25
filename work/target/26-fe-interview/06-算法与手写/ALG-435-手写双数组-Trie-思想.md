---
title: [ALG-435] 手写双数组 Trie 思想：海量词库内存压缩
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-435：手写双数组 Trie 思想：海量词库内存压缩

**答**：
- 题目：敏感词库 10 万词，对象式 Trie 内存爆炸（每节点一个对象 + Map）。双数组 Trie（DAT）：base/check 两个数组表达树结构，内存降一个数量级。
- 思路：state s 经字符 c 到 state t：check[t] = s 且 base[s] + code(c) = t。构建：为每个新状态分配 base 使转移槽无冲突（冲突重定位）。面试给思想与简化构建即可，说明压缩比与查找 O(len)。
- 评分点：base/check 语义；冲突重定位；查找无指针跳转（缓存友好）。

```javascript
class DoubleArrayTrie {
  constructor(words) {
    this.base = [1]; this.check = [0];                     // base/check 数组
    const code = new Map();                                // 字符编码
    for (const w of words) for (const c of w)
      if (!code.has(c)) code.set(c, code.size + 1);
    this.code = code;
    for (const w of words) this.insert(w);
  }
  insert(word) {
    let s = 0;                                             // 根状态 0
    for (const c of word) {
      const cc = this.code.get(c);
      let t = Math.abs(this.base[s] ?? 1) + cc;            // 目标状态
      if (this.check[t] === undefined) {
        // 空槽：直接分配 base
        while (this.check.length <= t) { this.check.push(0); this.base.push(0); }
        this.base[s] ??= 1;
        this.base[t] = t; this.check[t] = s;
        s = t;
      } else if (this.check[t] === s) {
        s = t;                                             // 已有转移
      } else {
        // 冲突：重定位 base[s]（简化演示，完整实现需迁移子树）
        this.base[s] = (this.base[s] ?? 1) + 1;
        s = Math.abs(this.base[s]) + cc;
        while (this.check.length <= s) { this.check.push(0); this.base.push(0); }
        this.base[s] = s; this.check[s] = s;
      }
    }
    this.base[s] = -Math.abs(this.base[s] ?? 1);           // 负 base 标记词尾
  }
  search(word) {
    let s = 0;
    for (const c of word) {
      const t = Math.abs(this.base[s] ?? 0) + this.code.get(c);
      if (this.check[t] !== s) return false;               // 转移无效
      s = t;
    }
    return this.base[s] < 0;                               // 词尾判断
  }
}
// 内存对比：对象 Trie 10 万词 ~200MB（对象开销）；DAT 两个数组 ~数 MB
```
