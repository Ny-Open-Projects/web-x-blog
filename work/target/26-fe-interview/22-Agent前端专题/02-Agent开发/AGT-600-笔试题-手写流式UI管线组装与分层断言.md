---
title: [AGT-600] 手写 pipe 组装五层管线与分层快照断言（定位卡顿丢字到层）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-600：手写 pipe 组装五层管线与分层快照断言（定位卡顿丢字到层）

**需求与边界**：
- 实现 pipe(...layers) 与 assertLayer(pipeline, layerName, events, snapshot)。
- 边界要求：① 每层输入输出为不可变事件数组（上一输出=下一输入）；② assertLayer 可单独跑某一层（截断管道），与全管道该层输出一致才算通过；③ 层名不存在抛错；④ 重放两遍结果一致（确定性断言）。

**答**：
```javascript
function pipe(...layers) {
  return (events) => layers.reduce((evs, l) => l(evs), events);
}
function assertLayer(pipeline, layerName, events, snapshot) {
  const idx = pipeline.layers.findIndex(l => l.name === layerName);
  if (idx === -1) throw new Error('NO_LAYER: ' + layerName);
  // 截断管道：只跑到目标层
  const partial = (evs) =>
    pipeline.layers.slice(0, idx + 1).reduce((a, l) => l(a), evs);
  const out1 = partial(events);
  const out2 = partial(events);                  // 重放确定性
  const pass = JSON.stringify(out1) === JSON.stringify(out2)
    && JSON.stringify(out1) === JSON.stringify(snapshot);
  return { pass, out: out1, layer: layerName };
}
// 用法：丢字卡顿时逐层断言二分定位
// assertLayer(pipeline, 'buffer', recorded, goldenSnap.buffer)
// assertLayer(pipeline, 'render', recorded, goldenSnap.render)
```

**评分点**:
- 层间契约：数组穿透、不可变（上一输出即下一输入）。
- 截断管道单层断言 + 重放一致性（丢字卡顿可二分定位到层）。
- 层名不存在显式抛错（断言自身可靠）。

