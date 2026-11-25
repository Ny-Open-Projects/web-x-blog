---
title: [PER-767] 手写一个 IM 消息洪泛缓冲渲染器：批量 flush、同人合并与渲染节流的完整实现
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-767：手写一个 IM 消息洪泛缓冲渲染器：批量 flush、同人合并与渲染节流的完整实现

**答**：
- 实现：消息到达进缓冲队列（按会话分桶），250ms 定时 flush；flush 时同人连续消息合并计数（"x 发送了 3 条展开项）；单次 flush 上限（30 条，超出留给下一轮）；渲染用 DocumentFragment 一次插入。
- 要点：正在滚动到底部（跟随模式）时 flush 后自动滚底，用户上翻（浏览历史）时不打扰（只更新未读计数）；批量里含撤回/编辑类变更消息要按 msgId 精确更新而不是追加。
- 边界：会话切换清空缓冲（防串会话）；flush 内 DOM 操作次数限制（一次 flush 一次插入）；洪泛结束检测（队列空后释放合并态）。
- 评分点：跟随模式判定与变更消息处理。

```javascript

class MessageBuffer {
  constructor(render, { flushMs = 250, maxPerFlush = 30 } = {}) {
    this.render = render; this.queue = []; this.timer = null;
    this.following = true;                                       // 跟随底部模式
    this.render.el.addEventListener('scroll', () => {
      this.following = this.render.atBottom();                   // 上翻即退出跟随
    }, { passive: true });
  }
  push(msg) {
    this.queue.push(msg);
    if (!this.timer) this.timer = setTimeout(() => this.flush(), 250);
  }
  flush() {
    this.timer = null;
    if (!this.queue.length) return;
    const batch = this.queue.splice(0, 30);                      // 上限留余
    const { appends, mutations } = splitBatch(batch);            // 追加类 vs 变更类（撤回/编辑）
    mutations.forEach(m => this.render.mutateById(m.msgId, m));  // 按 msgId 精确更新
    const merged = coalesceSameAuthor(appends);                  // 同人合并
    const frag = this.render.buildFragment(merged);
    this.render.append(frag);                                    // 一次 DOM 插入
    if (this.following) this.render.scrollToBottom({ smooth: false });  // 跟随滚底
    if (this.queue.length) this.timer = setTimeout(() => this.flush(), 250);
    else track('flood-drained', { pending: 0 });
  }
  clearOnSwitch() { clearTimeout(this.timer); this.queue = []; } // 会话切换清缓冲
}
function coalesceSameAuthor(msgs) {                               // 同人合并
  return msgs.reduce((out, m) => {
    const last = out.at(-1);
    if (last && last.author === m.author && m.ts - last.lastTs < 60000) {
      last.count = (last.count ?? 1) + 1; last.lastTs = m.ts;    // 合并计数
    } else out.push({ ...m, count: 1 });
    return out;
  }, []);
}
```
