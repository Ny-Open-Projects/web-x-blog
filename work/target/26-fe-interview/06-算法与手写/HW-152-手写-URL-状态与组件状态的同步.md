---
title: [HW-152] 手写 URL 状态同步——筛选条件入 URL（可分享可回退）、replace vs push 策略与历史膨胀防护
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-152：手写 URL 状态同步——筛选条件入 URL（可分享可回退）、replace vs push 策略与历史膨胀防护
**答**：筛选条件同步到 URL（可分享/可后退）：① 防抖同步（快速点击筛选，history 不膨胀——连续操作 300ms 内 replace 合并）；② 语义决策——用户主动操作 push（可后退到上次筛选）、程序性更新（默认值恢复）replace；③ URL 编码规范化（数组参数 / 数组逗号——保持稳定键序，可比较）；④ popstate 恢复（回退时解析 URL 恢复筛选）。

```javascript
function urlSyncedState(defaults, { debounceMs = 300 } = {}) {
  let state = { ...defaults, ...readURL() };
  let timer = null;
  function readURL() {
    const p = new URLSearchParams(location.search);
    const out = {};
    for (const k of Object.keys(defaults)) {
      const v = p.get(k);
      if (v != null) out[k] = Array.isArray(defaults[k]) ? v.split(',') : v;
    }
    return out;
  }
  function write(next, { push = true } = {}) {
    const p = new URLSearchParams();
    for (const [k, v] of Object.entries(next)) {
      if (v != null && String(v) !== String(defaults[k] ?? '')) {
        p.set(k, Array.isArray(v) ? v.join(',') : v);       // 默认值不入 URL（保持短链）
      }
    }
    const url = `${location.pathname}${p.toString() ? '?' + p : ''}`;
    push ? history.pushState(null, '', url) : history.replaceState(null, '', url);
  }
  addEventListener('popstate', () => {                       // 后退：恢复筛选
    state = { ...defaults, ...readURL() };
    subscribers.forEach((f) => f(state));
  });
  const subscribers = new Set();
  return {
    get state() { return state; },
    set(next, opts) {                                        // 用户操作：防抖 push
      state = { ...state, ...next };
      clearTimeout(timer);
      timer = setTimeout(() => write(state, { push: opts?.push ?? true }), debounceMs);
      subscribers.forEach((f) => f(state));
    },
    subscribe(fn) { subscribers.add(fn); return () => subscribers.delete(fn); },
  };
}
// push vs replace：用户点击筛选 push（可后退）；程序恢复默认 replace（不产生"无意义历史条目"）
// 防抖 300ms：连续 5 次筛选只留 1 条历史（历史膨胀防护）
```

**评分点**：
- push vs replace 的语义决策（用户操作可后退、程序性更新不进历史）。
- 防抖合并防历史膨胀；默认值不入 URL 保持短链。
- popstate 恢复 + URL 键序规范化。
- 数组参数编码（逗号 join）与解码对称。
