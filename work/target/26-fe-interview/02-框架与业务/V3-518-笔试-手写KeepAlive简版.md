---
title: [V3-518] 笔试：手写 KeepAlive 简版
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 编译器]
type: 笔试题
---

## V3-518：笔试：手写 KeepAlive 简版

**答**：实现 `MyKeepAlive` 组件：① 缓存组件 vnode（Map: key → vnode + DOM 容器）；② 切换时卸载走「缓存」而非销毁—— deactivated/activated 语义（简化为 onActivated 调用）；③ include 白名单匹配（按组件 name）；④ max 上限 LRU 淘汰（最久未用 unmount 真实卸载）；⑤ 内部状态（响应式数据）在缓存期间保留。写出实现。

```javascript
import { h, ref, getCurrentInstance, onMounted, watchEffect } from 'vue';

const MyKeepAlive = {
  name: 'MyKeepAlive',
  __isKeepAlive: true,
  props: { include: RegExp, max: Number },
  setup(props, { slots }) {
    const cache = new Map();        // key -> { vnode, container }
    const keys = [];                // LRU 顺序
    const instance = getCurrentInstance();
    instance.ctx.deactivate = (vnode) => {   // 卸载时移入缓存容器
      const el = vnode.el;
      const container = document.createElement('div');
      container.appendChild(el);              // DOM 移出文档但保留
      vnode.component.isDeactivated = true;
    };
    instance.ctx.activate = (vnode, container, anchor) => {
      container.insertBefore(vnode.el, anchor);
      vnode.component.isDeactivated = false;
      vnode.component.bn?.forEach(a => a());  // 触发 activated 钩子
    };
    return () => {
      const child = slots.default()[0];
      const key = child.type.name ?? child.key ?? child.type;
      if (props.include && !props.include.test?.(String(key))) return child; // 白名单外不缓存
      const cached = cache.get(key);
      if (cached) {
        child.el = cached.vnode.el;           // 复用 DOM
        child.component = cached.vnode.component;
        keys.splice(keys.indexOf(key), 1); keys.push(key);  // 提升为最新
      } else {
        cache.set(key, { vnode: child });
        keys.push(key);
        if (props.max && cache.size > props.max) {
          const eldest = keys.shift();
          const old = cache.get(eldest);
          unmountComponent(old.vnode);        // 真实卸载
          cache.delete(eldest);
        }
      }
      pendingKey.value = key;                 // 供 patch 层判断
      return child;
    };
  },
};
```

**评分点**：
- 缓存的是「vnode + DOM 容器」，activate 用 insert 移回文档（非重建）
- include 白名单短路返回原 vnode
- max LRU 淘汰走真实 unmount
- isDeactivated 状态标记防缓存期间响应式更新渲染
