---
title: "题 9：手写简单的 Bloom Filter（缓存穿透前置件）"
date: 2026-11-18
categories: [Java面试, 手写代码]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 9：手写简单的 Bloom Filter（缓存穿透前置件）

```java
class SimpleBloomFilter {
    private final BitSet bits;
    private final int[] seeds = {7, 11, 13, 31, 37};   // 多哈希降低误判
    private final int size;

    SimpleBloomFilter(int expectedInsertions) {
        this.size = expectedInsertions * 4 / 3;        // 经验：约 25% 冗余
        this.bits = new BitSet(size);
    }

    void add(String value) {
        for (int seed : seeds) bits.set(hash(value, seed));
    }

    boolean mightContain(String value) {
        for (int seed : seeds)
            if (!bits.get(hash(value, seed))) return false;  // 有一位为 0 必不存在
        return true;                                          // 全 1 = 可能存在（有误判）
    }

    private int hash(String value, int seed) {
        int h = 0;
        for (char c : value.toCharArray()) h = h * seed + c;
        return (h & 0x7fffffff) % size;   // 抹掉符号位再取模——Math.abs(h % size) 在 h 为负时虽安全，但 abs 对 MIN_VALUE 会溢出，review 高频标记项
    }
}
```

**必讲**：① 无漏判（说不存在就一定不存在）→ 适合当"拦截器"放在 DB 前；② 有误判 → 拦截后仍要 DB 兜底一次（防止误杀）；③ 不支持删除 → 计数布隆/布谷鸟过滤器；④ 容量估算公式 `n = -m·ln(1-p... )` 讲不清就说"误判率与位数组大小和插入量相关，工程上用 Guava 的 BloomFilter，按预期插入量和误判率创建"。

---
