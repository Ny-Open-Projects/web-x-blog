---
title: [NODE-274] SSR 的水合失败与降级重试？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-274：SSR 的水合失败与降级重试？
**答**:
- 水合失败的典型原因：SSR/CSR 渲染结果不一致（随机值/时区/语言）、chunk 加载失败、字典版本不符（ARC-249）。
- React 的处理：水合 mismatch 警告 + 局部重建（React 18 起 mismatch 区域客户端重渲染）——极端情况整页客户端渲染。
- 降级重试策略：chunk 404 → SW 缓存旧 chunk 兜底（ARC-273）+ 上报；字典版本不符 → 客户端拉最新字典后重新水合。
- 预防手段：SSR/CSR 同一渲染函数（NODE-299 思想）、随机值用稳定 seed（性能监控快照 DP-343 同款种子随机）。

```tsx
// 水合安全的随机组件
function Campaign() {
  const [seed] = useState(() => 12345);        // SSR 与 CSR 用同一 seed（不直接 Math.random）
  return <Shuffle items={items} seed={seed}/>;
}
// chunk 加载失败降级：
window.addEventListener('error', (e) => {
  if (e.target instanceof HTMLScriptElement) {          // script 加载失败
    report('chunk-fail', { src: e.target.src });
    if (isStaleChunk(e.target.src)) location.reload();  // 旧 HTML 引用已删 chunk → 刷新拿新 HTML
  }
}, true);
```
