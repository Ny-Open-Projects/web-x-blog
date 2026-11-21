---
title: "题 2：手写 LRU 缓存（LinkedHashMap 版 + 纯手写双向链表版）"
date: 2026-11-18
categories: [Java面试, 手写代码]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 2：手写 LRU 缓存（LinkedHashMap 版 + 纯手写双向链表版）

**30 秒版（先给这个，体现 API 熟练）**：

```java
class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    LRUCache(int capacity) {
        super(16, 0.75f, true);          // true = accessOrder 按访问顺序
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;        // 超容量淘汰"最老"节点
    }
}
```

**追问必到手写版（双向链表 + HashMap，O(1)）**：

```java
class LRUCache {
    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node();   // 哨兵头（存最新）
    private final Node tail = new Node();   // 哨兵尾（存最旧）

    static class Node { int key, value; Node prev, next; Node() {} 
                        Node(int k, int v) { key = k; value = v; } }

    LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail; tail.prev = head;
    }

    public int get(int key) {
        Node n = map.get(key);
        if (n == null) return -1;
        moveToHead(n);                    // 访问即提升为最新
        return n.value;
    }

    public void put(int key, int value) {
        Node n = map.get(key);
        if (n != null) { n.value = value; moveToHead(n); return; }
        if (map.size() == capacity) {     // 淘汰尾部
            Node oldest = tail.prev;
            unlink(oldest); map.remove(oldest.key);
        }
        Node fresh = new Node(key, value);
        map.put(key, fresh); addToHead(fresh);
    }

    private void unlink(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }
    private void addToHead(Node n) { n.next = head.next; n.prev = head;
        head.next.prev = n; head.next = n; }
    private void moveToHead(Node n) { unlink(n); addToHead(n); }
}
```

**坑点**：① 用哨兵节点避免判空边界（面试官会问"为什么要哨兵"——消灭头尾特判）；② 淘汰时要同时摘链表和删 map（漏一个就内存泄漏）；③ 追问"并发版怎么做" → 加锁 or 讲 Caffeine 的无锁思路（呼应第 1 章题 1.4.1）。

---
