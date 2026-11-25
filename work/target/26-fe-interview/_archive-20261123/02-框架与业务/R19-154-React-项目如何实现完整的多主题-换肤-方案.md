---
title: [R19-154] React 项目如何实现完整的多主题（换肤）方案？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-154：React 项目如何实现完整的多主题（换肤）方案？
**答**：
- 主流方案是 **CSS 变量 + data-theme 属性**：`:root` 定义亮色变量，`[data-theme="dark"]` 覆盖暗色，换肤只是切一个属性，零重渲染。
- React 侧封装 `ThemeProvider` + `useTheme`：管理当前主题、写 localStorage、同步 `document.documentElement.dataset.theme`。
- 扩展性：品牌色用 `--brand` 语义变量，组件只消费语义变量；跟随系统的暗色用 `matchMedia('(prefers-color-scheme: dark)')` 做默认值。
- 首屏防闪白：主题读取放在入口同步执行（或内联脚本），SSR 下把 data-theme 渲染在服务端。

```tsx
// theme.tsx —— CSS 变量多主题方案
import { createContext, useContext, useEffect, useState, type ReactNode } from 'react';

type Theme = 'light' | 'dark';
const ThemeCtx = createContext<{ theme: Theme; toggle: () => void }>({ theme: 'light', toggle: () => {} });

function getInitialTheme(): Theme {
  const saved = localStorage.getItem('theme') as Theme | null;
  if (saved) return saved;
  return matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setTheme] = useState<Theme>(getInitialTheme);

  useEffect(() => {
    // 换肤 = 换一个 HTML 属性，全部样式由 CSS 变量级联，React 不参与渲染
    document.documentElement.dataset.theme = theme;
    localStorage.setItem('theme', theme);
  }, [theme]);

  return (
    <ThemeCtx.Provider value={{ theme, toggle: () => setTheme(t => (t === 'light' ? 'dark' : 'light')) }}>
      {children}
    </ThemeCtx.Provider>
  );
}

export const useTheme = () => useContext(ThemeCtx);

/* styles/theme.css —— 语义变量 + 两套取值
:root {
  --brand: #2563eb;
  --bg: #ffffff;
  --text: #111827;
  --card: #f3f4f6;
}
[data-theme="dark"] {
  --brand: #60a5fa;
  --bg: #0f172a;
  --text: #e5e7eb;
  --card: #1e293b;
}
.card { background: var(--card); color: var(--text); }
*/

// ThemeSwitch.tsx —— 使用侧
export function ThemeSwitch() {
  const { theme, toggle } = useTheme();
  return <button onClick={toggle}>{theme === 'light' ? '🌙' : '☀️'}</button>;
}

// 防闪白：index.html 内联脚本在 CSS 加载前同步设置主题
// <script>
//   document.documentElement.dataset.theme =
//     localStorage.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
// </script>
```
