---
title: [TST-087] Vitest + React Testing Library 完整环境搭建清单
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-087：Vitest + React Testing Library 完整环境搭建清单
**答**：
- 依赖四件套：vitest、@testing-library/react、@testing-library/user-event、@testing-library/jest-dom；环境选 jsdom（或 happy-dom）。
- 配置四步：environment: 'jsdom'、globals: true（免 import + 自动 cleanup）、setupFiles 引入 jest-dom/vitest、include 覆盖 *.test.tsx。
- 可选增强：@testing-library/jest-dom 类型进 tsconfig types；MSW setupServer 进 setup；coverage provider v8。
- 自检清单：能否渲染组件（JSX 转换生效）、能否用 toBeInTheDocument（jest-dom 生效）、能否 userEvent.click（事件模拟生效）、渲染两次是否互不污染（cleanup 生效）。

```typescript
// 1. 安装
// npm i -D vitest @testing-library/react @testing-library/user-event @testing-library/jest-dom jsdom

// 2. vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,                       // 自动 cleanup 依赖它
    setupFiles: ['./vitest.setup.ts'],
    include: ['src/**/*.test.{ts,tsx}'],
  },
});

// 3. vitest.setup.ts
import '@testing-library/jest-dom/vitest';

// 4. 自检用例 src/sum.test.tsx
test('环境自检', () => {
  render(<button>点我</button>);
  expect(screen.getByRole('button')).toBeInTheDocument();   // 三层全通即环境 OK
});
```
