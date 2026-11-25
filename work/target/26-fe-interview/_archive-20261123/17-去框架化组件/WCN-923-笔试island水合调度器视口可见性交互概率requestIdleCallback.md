---
title: [WCN-923] 手写 island 水合调度器：按视口可见性 + 交互概率分批 requestIdleCallback 水合
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-923：手写 island 水合调度器：按视口可见性 + 交互概率分批 requestIdleCallback 水合

**题目**：实现 `createHydrationScheduler({ hydrate, threshold = 0.5 })`，返回 `{ register(el, { priority, onHydrate }), observe(), destroy() }`。要求：① register 收集待水合岛（el + 优先级 + 回调），返回取消注册函数；② observe 启动调度：对每个岛计算「可见性（用注入的 isVisible 函数，默认全可见）× priority」，得分 ≥ threshold 的用 requestIdleCallback（注入的 scheduleIdle，默认 setTimeout(fn,0)）分批水合，每批最多 batchSize 个；③ 高分（≥0.9）岛立即水合，不等 idle；④ 水合后调用 onHydrate 并从队列移除；⑤ destroy 清空队列、停止调度。依赖必须注入（isVisible、scheduleIdle）便于测试，不依赖真实浏览器。请自足实现并给出可运行示例。

**答**：

```javascript
function createHydrationScheduler({ hydrate, threshold = 0.5, batchSize = 2,
    isVisible = () => true, scheduleIdle = fn => setTimeout(fn, 0) } = {}) {
  let queue = [], stopped = false;
  return {
    register(el, { priority = 0.5, onHydrate } = {}) {
      queue.push({ el, priority, onHydrate });
      return () => { queue = queue.filter(x => x.el !== el); };
    },
    observe() {
      if (stopped) return;
      const scored = queue.map(x => ({ ...x,
        score: (isVisible(x.el) ? 1 : 0) * x.priority }));
      const immediate = scored.filter(x => x.score >= 0.9);
      const deferred = scored.filter(x => x.score >= threshold && x.score < 0.9);
      immediate.forEach(run);
      scheduleIdle(() => {
        if (stopped) return;
        deferred.slice(0, batchSize).forEach(run);
      });
      function run(x) {
        hydrate(x.el);
        x.onHydrate && x.onHydrate();
        queue = queue.filter(y => y.el !== x.el);
      }
    },
    destroy() { stopped = true; queue = []; },
  };
}
const hydrated = [];
const s = createHydrationScheduler({
  hydrate: el => hydrated.push(el.dataset.name),
  isVisible: el => el.dataset.visible === '1',
  scheduleIdle: fn => fn(), // 测试：同步执行
});
s.register({ dataset: { name: 'buy', visible: '1' } }, { priority: 1 });
s.register({ dataset: { name: 'footer', visible: '0' } }, { priority: 0.3 });
s.observe();
console.log(hydrated); // ['buy']（footer 不可见且低分，跳过）
```

**评分点**：
- 评分 = 可见性 × 优先级，threshold 过滤正确。
- 高分（≥0.9）立即水合、其余走注入的 scheduleIdle 分批（batchSize 限制）。
- register 返回取消函数、destroy 清空停止，无残留调度。
- 水合后回调 onHydrate 并出队，不重复水合。
- 依赖注入 isVisible/scheduleIdle，示例可运行且输出正确。
