---
title: [ALG-313] 无限滚动截流：IO 哨兵 + 加载态互斥 + 到底收敛（三态哨兵：可加载/加载中/无更多）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-313：无限滚动截流：IO 哨兵 + 加载态互斥 + 到底收敛（三态哨兵：可加载/加载中/无更多）？
**答**：无限滚动的三态收敛：可加载（哨兵可见触发）/加载中（互斥防重复）/无更多（哨兵移除收敛）——IO 哨兵的 state 机（HW-182 强化：无更多时停止观察）。

**思路**：哨兵三态机——loading 标志互斥；hasMore false 时 unobserve（哨兵移除替换"到底"提示）。

```javascript
class InfiniteLoader {
  #loading = false; #hasMore = true; #io = null;
  constructor(container, fetchPage, { renderMore } = {}) { Object.assign(this, { container, fetchPage, renderMore });
    const sentinel = document.createElement('div');
    sentinel.style.height = '1px';
    container.append(sentinel);
    this.#io = new IntersectionObserver(async ([e]) => {
      if (!e.isIntersecting || this.#loading || !this.#hasMore) return;   // 三态门卫
      this.#loading = true;
      try {
        const rows = await fetchPage();
        this.renderMore(rows);
        this.#hasMore = rows.length > 0;                  // 空页 = 无更多（服务端契约）
        if (!this.#hasMore) {
          this.#io.unobserve(sentinel);                   // 收敛：停止观察（省 IO 回调）
          sentinel.replaceWith(noMoreNode());             // "到底了"提示
        }
      } finally { this.#loading = false; }                // finally 互斥释放（失败也解锁）
    }, { root: container, rootMargin: '400px' });
    this.#io.observe(sentinel);
  }
}
// 三态门卫：loading 互斥（防重复触发）+ hasMore 收敛（unobserve 停止观察）+ visible 触发
// finally 解锁：加载失败也释放互斥（下滚可重试——死锁防护）
// rootMargin 400px：提前量（滚到底才触发会闪加载态）
// 空页契约：服务端返回空数组 = 无更多 —— 客户端不用数 count（分页游标语义天然收敛）
```

**评分点**：
- 三态门卫（loading 互斥/hasMore 收敛/visible 触发）——本题核心。
- finally 解锁防死锁。
- unobserve 收敛（无更多停止观察）。
- 空页契约替代 count 计数。
