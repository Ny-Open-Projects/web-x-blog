---
title: [WCN-097] 笔试：手写 Signals 版主题切换（系统跟随 + 持久化 + CSS 变量注入）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-097：笔试：手写 Signals 版主题切换

**题目**：① `theme` signal：'light' | 'dark' | 'system'；② 'system' 跟随 `matchMedia('(prefers-color-scheme: dark)')` 且监听变化；③ 实际生效主题 `effectiveTheme` computed；④ 应用主题 = 给 `document.documentElement` 设置 `data-theme` + 切换 CSS 变量集（两套 token）；⑤ 首次加载防闪烁（读取 localStorage 内联在 head）；⑥ dispose 解除监听。

**答**：

```javascript
import { createSignal, computed, effect, untrack } from './mini.js';

export function createThemeManager() {
  const [theme, setTheme] = createSignal(localStorage.getItem('theme') ?? 'system');
  const mq = matchMedia('(prefers-color-scheme: dark)');
  const [osDark, setOsDark] = createSignal(mq.matches);
  const onMq = (e) => setOsDark(e.matches);
  mq.addEventListener('change', onMq);

  const effective = computed(() => {
    const t = theme();
    if (t === 'system') return osDark() ? 'dark' : 'light';
    return t;
  });

  const tokens = {
    light: { '--bg': '#fff', '--fg': '#111', '--accent': '#2563eb' },
    dark: { '--bg': '#0f172a', '--fg': '#f8fafc', '--accent': '#60a5fa' },
  };
  const stop = effect(() => {
    const t = effective();
    const root = document.documentElement;
    root.dataset.theme = t;
    for (const [k, v] of Object.entries(tokens[t])) root.style.setProperty(k, v);
    localStorage.setItem('theme', untrack(theme));  // 存原始意图（system 也要存）
  });

  return { theme, setTheme, effective,
    dispose() { mq.removeEventListener('change', onMq); stop(); } };
}

// 防闪烁（head 内联，先于 CSS 渲染执行）：
// <script>try{var t=localStorage.getItem('theme');
// var d=t==='dark'||(t!=='light'&&matchMedia('(prefers-color-scheme: dark)').matches);
// document.documentElement.dataset.theme=d?'dark':'light';}catch(e){}</script>
```

**评分点**：
- system 语义正确拆分：原始意图与生效主题两个层（effective computed）。
- matchMedia change 监听驱动 system 切换实时生效。
- 防 FOUC：head 内联脚本先行（SSR 场景关键）。
- tokens 用 CSS 变量注入（组件零改动换肤）；dispose 清理。
