---
title: [HW-039] 手写 Vue 双向绑定（v-model 简版）
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-039：手写 Vue 双向绑定（v-model 简版）

**答**：
- 评分点：双向绑定 = **数据劫持**（defineProperty）+ **编译**（遍历 DOM 找 `v-model` 与 `{{}}`）+ **订阅更新**（Dep/Watcher）；编译时：文本节点替换插值并注册更新函数；input 节点绑定 `input` 事件把值写回数据（视图 → 数据），同时初始化 `node.value`（数据 → 视图）；数据变化时要通知到对应的 updater（维护 key → updaters 映射）；能一句话总结：v-model 是 `:value` + `@input` 的语法糖。

```javascript
// ===== 5 分钟速写版 =====
class MiniVue {
  constructor({ el, data }) {
    this.$el = document.querySelector(el);
    this.$data = data;
    this.updaters = new Map(); // key → Set<updater 函数>
    Object.keys(data).forEach(k => this._reactive(k, data[k]));
    this._compile(this.$el);
  }
  _reactive(key, val) {
    const updaters = new Set();
    this.updaters.set(key, updaters);
    Object.defineProperty(this.$data, key, {
      get: () => val,
      set: nv => {
        val = nv;
        updaters.forEach(fn => fn(nv)); // 数据 → 视图
      }
    });
  }
  _bind(key, updater) {
    this.updaters.get(key).add(updater);
    updater(this.$data[key]); // 初始化视图
  }
  _compile(node) {
    node.childNodes.forEach(child => {
      if (child.nodeType === 3) { // 文本节点：处理 {{ xx }}
        const match = child.textContent.match(/\{\{\s*(\w+)\s*\}\}/);
        if (match) {
          const key = match[1];
          this._bind(key, v => { child.textContent = v; });
        }
      } else if (child.nodeType === 1) {
        if (child.hasAttribute('v-model')) {
          const key = child.getAttribute('v-model');
          this._bind(key, v => { child.value = v; });      // 数据 → 视图
          child.addEventListener('input', e => {            // 视图 → 数据
            this.$data[key] = e.target.value;
          });
        }
        if (child.childNodes.length) this._compile(child); // 递归编译子节点
      }
    });
  }
}

// ===== 标准完整版（含边界处理）=====
class MiniVuePro {
  constructor({ el, data }) {
    if (!el || !document.querySelector(el)) throw new Error('mount target not found');
    this.$el = document.querySelector(el);
    this.$data = data;
    this.updaters = new Map();
    Object.keys(data).forEach(k => this._reactive(k, data[k]));
    this._compile(this.$el);
  }
  _reactive(key, val) {
    const updaters = new Set();
    this.updaters.set(key, updaters);
    Object.defineProperty(this.$data, key, {
      enumerable: true,
      get: () => val,
      set: nv => {
        if (nv === val) return;
        val = nv;
        // 拷贝遍历：updater 内可能再次修改数据
        [...updaters].forEach(fn => fn(nv));
      }
    });
  }
  _bind(key, updater) {
    if (!this.updaters.has(key)) throw new Error(`unknown key: ${key}`); // 模板写错尽早暴露
    this.updaters.get(key).add(updater);
    updater(this.$data[key]);
  }
  _compile(node) {
    node.childNodes.forEach(child => {
      if (child.nodeType === 3) {
        // 支持一段文本内多个插值 {{ a }}-{{ b }}
        const text = child.textContent;
        if (/\{\{\s*\w+\s*\}\}/.test(text)) {
          const keys = [...text.matchAll(/\{\{\s*(\w+)\s*\}\}/g)].map(m => m[1]);
          const render = () => {
            child.textContent = text.replace(/\{\{\s*\w+\s*\}\}/g, (_, k) =>
              this.$data[k.trim()] ?? '');
          };
          keys.forEach(k => this.updaters.get(k)?.add(render));
          render();
        }
      } else if (child.nodeType === 1) {
        if (child.hasAttribute('v-model')) {
          const key = child.getAttribute('v-model');
          const tag = child.tagName.toLowerCase();
          const bindEvent = tag === 'input' ? 'input' : tag === 'textarea' ? 'input' : 'change';
          this._bind(key, v => { if (child.value !== v) child.value = v; });
          child.addEventListener(bindEvent, e => { this.$data[key] = e.target.value; });
        }
        if (child.childNodes.length) this._compile(child);
      }
    });
  }
}
```

---
