---
title: [R19-039] flushSync 是什么？什么时候需要它？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-039：flushSync 是什么？什么时候需要它？
**答**：
- flushSync 强制 React 立即同步完成该次更新：重渲染、DOM 提交、layout effect 全部跑完才返回。
- 场景：更新后立刻测量/读取 DOM、第三方库在回调中要求 DOM 已更新、实现某些交互反馈。
- 它是批处理的"逃逸舱口"，代价是打断正常的调度优先级，频繁使用会伤害性能。
- 不能在生命周期和 effect 内部调用，否则 React 会警告。

```jsx
import { flushSync } from 'react-dom';

function CopyButton() {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    await navigator.clipboard.writeText('hello');
    // 强制同步提交，保证下一行读 DOM 时界面已经更新
    flushSync(() => {
      setCopied(true);
    });
    console.log(document.querySelector('p')?.textContent); // 一定是 已复制
  }

  return (
    <>
      <button onClick={handleCopy}>复制</button>
      {copied && <p>已复制</p>}
    </>
  );
}
```
