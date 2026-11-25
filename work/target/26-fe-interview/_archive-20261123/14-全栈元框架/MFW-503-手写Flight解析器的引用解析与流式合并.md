---
title: [MFW-503] 手写 Flight 解析器：引用延迟绑定与流式 chunk 合并
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-503：手写 Flight 解析器：引用延迟绑定与流式 chunk 合并

**答**:
- 解析器的三个核心机制：1) **行缓冲**（chunk 可能切断行——按 \n 缓冲，RBL-875 同构）；2) **引用表**（rowId → 值；`$L2` 引用在 row 2 未到时挂起，到达后 resolve——发布订阅式延迟绑定）；3) **流式合并**（`$@` Promise 引用：pending → fulfilled 状态迁移，Suspense 边界的数据到达即触发 UI 补丁）。
- 解析器与 React 的对接：解析产物是「可渲染的虚拟树」（元素树 + client 组件引用）——React 内部的 FlightClient 把 rows 填进一个可增长的模型，`$L` 引用是 lazy 节点（Suspense 消费）。
- 实现要点：引用的「三态」（未到达/已到达/流式 Promise）+ 替换语义（占位对象被真实值 in-place 替换——React 通过引用同一对象感知更新）。
- 追问钩子：为什么引用用「in-place 替换」而不是「重新派发」？——树里的引用点是同一个 JS 对象（占位），到达时改写其内容 → 持有该引用的组件树无需重建（React 的模型：引用相同 = 可变更新）——这与 React 的「同一引用可变更新」契约一致，也是为什么 Flight 解析器不能简单 JSON.parse（JSON 每次生成新对象，引用断裂）。

```javascript
// 极简 Flight 解析器
function createFlightReader() {
  const rows = new Map();                                // id -> value
  const waiters = new Map();                             // id -> [fn]
  const pending = new Map();                             // rowId -> rowId（流式目标）
  let buf = '';
  const resolveRef = (ref) => {                          // '$L2' / '$@1' / '$3'
    const m = /^\$(L?@?)(\d+)$/.exec(ref);
    if (!m) return ref;
    const id = m[2];
    if (rows.has(id)) return rows.get(id);
    return { $$pending: true, id };                      // 占位：到达后 in-place 填充
  };
  function handleLine(line) {
    const m = /^(\d+):([\s\S]*)$/.exec(line);
    if (!m) return;
    const [, id, body] = m;
    let value;
    try { value = JSON.parse(body); } catch { return; }
    // 深度遍历替换 $ 引用
    const walk = (v) => Array.isArray(v) ? v.map(walk)
      : (v && typeof v === 'object')
        ? Object.fromEntries(Object.entries(v).map(([k, x]) => [k, walk(x)]))
        : typeof v === 'string' && v.startsWith('$') ? resolveRef(v) : v;
    value = walk(value);
    rows.set(id, value);
    (waiters.get(id) ?? []).forEach(fn => fn(value));    // 唤醒等待者
    waiters.delete(id);
  }
  return {
    push(chunk) {
      buf += chunk;
      let i;
      while ((i = buf.indexOf('\n')) !== -1) {
        handleLine(buf.slice(0, i)); buf = buf.slice(i + 1);
      }
    },
    get(id) {
      return rows.get(id) ?? new Promise(res => {
        (waiters.get(id) || waiters.set(id, []).get(id)).push(res);
      });
    },
  };
}
```
