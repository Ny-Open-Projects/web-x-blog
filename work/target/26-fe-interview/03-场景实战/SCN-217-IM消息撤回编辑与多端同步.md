---
title: [SCN-217] IM 消息撤回与编辑——多端一致与时间窗控制？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-217：消息撤回/编辑功能，前端怎么设计才能多端一致？

**答**:
- 撤回流程：客户端发起撤回请求（带 serverId）→ 服务端校验（时间窗 2 分钟/权限）→ 广播撤回控制消息 → 各端渲染撤回态；撤回也是一条消息（走 seq 流水），保证顺序正确。
- 多端一致：任何端执行撤回，其他端收到控制消息后更新本地消息状态（内容替换为"已撤回"占位）——本地已渲染的消息即时替换（不刷新整列表）；撤回的图片/文件同时清理本地缓存预览。
- 编辑功能：编辑窗（同撤回时间窗）、编辑历史（服务端存版本，UI 可查看编辑记录）、编辑消息带"已编辑"标记（诚信呈现）、其他端收到 edit 控制消息后替换内容+标记。
- 边界处理：撤回请求失败（超窗/权限）→ 明确错误提示（"超过 2 分钟无法撤回"）；撤回后引用失效（引用该消息的引用块同步失效标记）；离线期间的撤回→上线同步时按控制消息补齐。

```javascript
async function recall(msg) {
  if (Date.now() - msg.ts > 2 * 60e3)
    return toast('超过 2 分钟无法撤回');
  const r = await imApi.recall(msg.serverId);
  if (r.ok) applyRecall(msg.serverId);       // 本端即时更新
  else toast(r.reason);
}
ws.on('recall', (e) => {
  const m = store.get(e.serverId);
  if (!m) return pendingRecalls.add(e.serverId); // 消息未到达先缓存
  store.update(e.serverId, { type: 'recalled' });
  clearMediaCache(m);                        // 清理媒体缓存
});
// 编辑同理：ws.on('edit', e => store.update(e.serverId,
//   { content: e.content, edited: true }))。
```

**追问**：

1. 撤回控制消息比原消息先到（乱序）会怎样？ → 按 serverId 暂存 pending 撤回，消息落地时补应用撤回态，不能因为找不到消息就丢弃控制消息。
2. 编辑历史该给谁看？ → 只对发送者展示完整版本，接收方仅看「已编辑」标记，避免把修改痕迹变成纠纷证据。
3. 离线期间对方撤回、本地已有缓存，上线怎么对齐？ → 拉增量 seq 区间重放控制消息，不能只拉新消息，否则旧消息永远停在未撤回态。
