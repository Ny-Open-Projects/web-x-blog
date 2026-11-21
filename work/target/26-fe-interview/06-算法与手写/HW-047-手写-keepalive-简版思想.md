---
title: [HW-047] 手写 keep-alive 简版思想
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-047：手写 keep-alive 简版思想

**答**：
- 评分点：核心思想是**缓存组件实例而不是重新挂载**——切走时不销毁（不执行 unmount），切回时直接复用 DOM 与状态（对应 Vue keep-alive 的 activated / deactivated 钩子）；缓存要有 **LRU 上限**（配合 include/exclude 控制哪些缓存），超限淘汰最久未访问的实例并真正销毁；用 Map 保序实现 LRU（命中 delete+set 移到最新端）；能类比 React 的方案——React 没有官方 keep-alive，用 CSS display 隐藏 + 状态提升 / Offscreen（Activity）组件实现同等能力；说出缓存的是「实例 + vnode + DOM」三层是深度加分。

```javascript
// ===== 5 分钟速写版 =====
class KeepAlive {
  constructor(max = 5) {
    this.max = max;
    this.cache = new Map(); // key → 组件实例
  }
  mount(key, createComponent) {
    if (this.cache.has(key)) {
      const comp = this.cache.get(key);
      this.cache.delete(key);       // LRU 提位
      this.cache.set(key, comp);
      comp.activate();              // 恢复：不重新 created/mounted
      return comp;
    }
    const comp = createComponent(); // 新建实例
    comp.mount();
    this.cache.set(key, comp);
    if (this.cache.size > this.max) this._evict();
    return comp;
  }
  _evict() {
    const oldestKey = this.cache.keys().next().value; // Map 首个 = 最久未用
    const comp = this.cache.get(oldestKey);
    this.cache.delete(oldestKey);
    comp.destroy();               // 淘汰才真正销毁
  }
}

// ===== 标准完整版（含边界处理）=====
class KeepAlivePro {
  constructor({ max = 5, include = null, exclude = null } = {}) {
    if (!Number.isInteger(max) || max < 1) throw new TypeError('max must be a positive integer');
    this.max = max;
    this.include = include;   // 字符串 / 正则 / 数组：命中才缓存
    this.exclude = exclude;   // 命中则永不缓存
    this.cache = new Map();
    this.listeners = new Set(); // 缓存变化通知（调试面板 / 内存监控）
  }
  _match(key) {
    const inList = list => !list || (Array.isArray(list) ? list.includes(key) : list.test(key));
    if (this.exclude && inList(this.exclude)) return false;
    return this.include ? inList(this.include) : true;
  }
  mount(key, createComponent) {
    const comp = this.cache.get(key);
    if (comp) {
      this.cache.delete(key);
      this.cache.set(key, comp);
      comp.activate && comp.activate();     // 恢复（activated）
      return comp;
    }
    if (!this._match(key)) {
      const fresh = createComponent();
      fresh.mount();
      return fresh;                          // 不缓存：每次全新挂载
    }
    if (this.cache.size >= this.max) this._evict();
    const instance = createComponent();
    instance.mount();
    this.cache.set(key, instance);
    this.listeners.forEach(fn => fn('add', key, this.cache.size));
    return instance;
  }
  deactivate(key) {                          // 切走：只隐藏不销毁（deactivated）
    const comp = this.cache.get(key);
    if (comp) comp.deactivate && comp.deactivate();
  }
  _evict() {
    const oldestKey = this.cache.keys().next().value;
    const comp = this.cache.get(oldestKey);
    comp.destroy && comp.destroy();
    this.cache.delete(oldestKey);
    this.listeners.forEach(fn => fn('evict', oldestKey, this.cache.size));
  }
  remove(key) {                              // 主动清除：路由登出等场景
    const comp = this.cache.get(key);
    if (comp) { comp.destroy && comp.destroy(); this.cache.delete(key); }
  }
  clear() { [...this.cache.keys()].forEach(k => this.remove(k)); }
  onCacheChange(fn) { this.listeners.add(fn); return () => this.listeners.delete(fn); }
  get size() { return this.cache.size; }
}
// 追问：
// 1. keep-alive 三个参数 —— include / exclude / max（Vue 官方同名）
// 2. 缓存了什么 —— vnode + 组件实例 + 真实 DOM，切回时跳过整个实例化流程
// 3. React 对应方案 —— 状态提升 / 条件隐藏 / <Activity>（原 Offscreen）保留实例卸载效果
```

---
## 六、综合高频必手写（HW-048 ~ HW-060）
