---
title: [PER-723] 手写一个页面栈管理器（移动端 SPA）：keep-alive 缓存页面、栈上限与返回秒回的实现
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-723：手写一个页面栈管理器（移动端 SPA）：keep-alive 缓存页面、栈上限与返回秒回的实现

**答**：
- 实现：路由切换时旧页面 DOM 移入 keep-alive 容器（display:none 保留状态），返回时移回并恢复滚动位置；栈上限（如 5 页）LRU 淘汰最久未访问的缓存页。
- 要点：缓存页隐藏时挂起其定时器/轮询/observer（注册-挂起协议，页面组件实现 onSuspend/onResume）；隐藏页的事件监听会继续积累（全局监听要挂起）；上限淘汰前先执行清理钩子。
- 边界：内存预算（缓存页 DOM 总节点数限制）；带表单/播放器的页面可标记 nocache；缓存页与路由参数绑定（不同参数不同实例）。
- 评分点：挂起/恢复协议与 LRU 淘汰。

```javascript

class PageStackManager {
  constructor({ max = 5, maxNodes = 50000 } = {}) {
    this.stack = []; this.max = max; this.maxNodes = maxNodes;
    this.cache = new Map();                                     // key -> {el, state}
  }
  async navigate(route, mountFn) {
    this.suspendTop();                                          // 挂起当前页
    const key = route.key;
    const cached = this.cache.get(key);
    if (cached) {
      this.show(cached);                                        // 返回秒回
      cached.state.onResume?.();
    } else {
      const page = await mountFn();                             // 新建
      this.cache.set(key, { el: page.el, state: page });
      this.enforceLimits();
    }
    this.stack.push(key);
  }
  suspendTop() {
    const top = this.stack.at(-1);
    const c = top && this.cache.get(top);
    if (c) {
      c.el.style.display = 'none';
      c.state.onSuspend?.();                                    // 挂起定时器/轮询/observer
      saveScroll(c.el, c.state);
    }
  }
  enforceLimits() {
    let nodes = totalCachedNodes(this.cache);
    while (this.cache.size > this.max || nodes > this.maxNodes) {
      const oldest = [...this.cache.entries()]
        .filter(([k]) => !this.stack.includes(k))               // 不淘汰栈内页
        .sort((a, b) => a[1].lastUsed - b[1].lastUsed)[0];
      if (!oldest) break;
      oldest[1].state.onDestroy?.();                            // 清理钩子
      oldest[1].el.remove();
      this.cache.delete(oldest[0]);
      nodes = totalCachedNodes(this.cache);
    }
  }
}
```
