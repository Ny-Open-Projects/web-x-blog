---
title: [DP-013] 单例和多例（Multiton）、享元模式的边界在哪里？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-013：单例和多例（Multiton）、享元模式的边界在哪里？
**答**：
- 单例：全局 1 个实例；多例：按 key 缓存有限个实例（如按租户/按主题各一个 store）——`getInstance(key)`。
- 享元：面向"大量细粒度对象"，共享内部状态、外部状态外部传入——共享的是"对象内部的数据"，不是"唯一的实例"。
- 边界判断：控制"实例数量"（1 个或 N 个 keyed 实例）是单例/多例；控制"内存占用"（复用细粒度对象）是享元。
- 前端例子：全局一个 store 是单例；每个 tab 一个 store 是多例；一万个列表项共享同一个行组件配置对象是享元。

```javascript
// 多例：按 key 各持有一个实例，有界缓存
class ThemeStore {
  static #pool = new Map();
  static getInstance(key) {
    if (!ThemeStore.#pool.has(key)) ThemeStore.#pool.set(key, new ThemeStore(key));
    return ThemeStore.#pool.get(key);
  }
  constructor(key) { this.key = key; this.count = 0; }
}
console.log(ThemeStore.getInstance('dark') === ThemeStore.getInstance('dark')); // true
console.log(ThemeStore.getInstance('dark') === ThemeStore.getInstance('light')); // false —— 多例

// 享元：共享内部状态，外部状态作为参数传入
class TreeType { // 享元对象：内部状态（共享的部分）
  constructor(name, color, texture) { this.name = name; this.color = color; this.texture = texture; }
  draw(canvas, x, y) { console.log(`在 ${x},${y} 画 ${this.name}（共享纹理 ${this.texture}）`); }
}
class TreeFactory { // 享元工厂：保证同类享元只有一个
  static #types = new Map();
  static getType(name, color, texture) {
    const k = `${name}|${color}|${texture}`;
    if (!TreeFactory.#types.has(k)) TreeFactory.#types.set(k, new TreeType(name, color, texture));
    return TreeFactory.#types.get(k);
  }
}
// 一万棵树只创建极少数 TreeType，坐标（外部状态）画时才传
const trees = Array.from({ length: 10000 }, (_, i) => ({
  type: TreeFactory.getType('松树', '绿', 'pine.png'),
  x: i % 100, y: Math.floor(i / 100),
}));
console.log(trees[0].type === trees[9999].type); // true —— 内存从 1 万个对象降到 1 个
```

---

## 三、工厂模式
