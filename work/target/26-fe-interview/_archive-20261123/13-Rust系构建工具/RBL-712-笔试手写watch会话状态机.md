---
title: [RBL-712] 笔试：手写 watch 会话状态机（失效合并 + 追跑语义）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-712：笔试：手写 watch 会话状态机（失效合并 + 追跑语义）

**需求**：实现 `createWatchSession({ rebuild })`。rebuild(files) 为注入的异步函数（测试可控，返回产物字符串）。会话规则：1) `change(file)`：加入待处理集；2) 若空闲立即触发一轮 rebuild（传入当前待处理集快照并清空）；3) 若正在构建：不启动新构建，等当前完成后**用最新待处理集再跑一轮**（追跑）；4) 连续 change（构建中）只保留集合去重；5) rebuild 抛错：会话不死，记录错误、状态回 idle（可被后续 change 唤醒），通过 `onError` 通知；6) `dispose()`：清理，后续 change 忽略。返回 `{ change, dispose, state }`（state: 'idle'|'building'|'disposed'）。

```javascript
function createWatchSession({ rebuild, onError }) {
  let pending = new Set();
  let state = 'idle';
  let disposed = false;

  async function pump() {
    while (!disposed && pending.size) {
      const batch = [...pending];
      pending = new Set();
      state = 'building';
      try {
        await rebuild(batch);                            // 增量重建
      } catch (e) {
        state = 'idle';
        onError?.(e);                                    // 会话不死
        return;                                          // 回 idle，等下次 change
      }
    }
    state = disposed ? 'disposed' : 'idle';
  }

  return {
    change(file) {
      if (disposed) return;
      pending.add(file);
      if (state !== 'building') pump();                  // 空闲：立即跑；构建中：标记等追跑
    },
    dispose() {
      disposed = true; pending.clear(); state = 'disposed';
    },
    get state() { return state; },
    _pendingSize: () => pending.size,
  };
}

// 自测
let builds = []; let resolveBuild;
const rebuild = (files) => new Promise(res => {
  builds.push(files); resolveBuild = res;                // 挂起，测试手动放行
});
const session = createWatchSession({ rebuild, onError: () => {} });

session.change('a.js');
console.log(session.state === 'building' && builds.length === 1);
session.change('b.js'); session.change('a.js');          // 构建中合并去重
console.log(session._pendingSize() === 2);
resolveBuild('v1'); await sleep(0);
console.log(builds.length === 2);                        // 追跑
console.log(session._pendingSize() === 0);
resolveBuild('v2'); await sleep(0);
console.log(session.state === 'idle');

// 空闲时批量 change
session.change('c.js'); session.change('d.js');
console.log(builds.length === 3 && builds[2].join(',') === 'c.js,d.js');
resolveBuild('v3'); await sleep(0);

// 错误恢复
const errSession = createWatchSession({ rebuild: async () => { throw new Error('boom'); },
  onError: () => {} });
errSession.change('x.js'); await sleep(0);
console.log(errSession.state === 'idle');                // 会话不死
errSession.change('y.js'); await sleep(0);
console.log(errSession.state === 'idle');

session.dispose();
session.change('e.js');
console.log(session.state === 'disposed' && builds.length === 3);   // dispose 后忽略
```

**评分点**：
- 追跑语义正确：构建中不启动新轮、完成后用最新集合追跑（while 循环）；集合去重
- 错误恢复：rebuild 抛错会话回 idle 可再唤醒（不吞错误、通知 onError）
- dispose 后忽略 change；state 三态准确
- 能说清「完成当前轮 + 追跑优于中断」的语义依据（消费者是文件系统）属于加分
