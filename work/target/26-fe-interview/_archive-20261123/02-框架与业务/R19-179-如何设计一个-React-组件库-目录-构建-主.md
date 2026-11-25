---
title: [R19-179] 如何设计一个 React 组件库（目录、构建、主题、文档）？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-179：如何设计一个 React 组件库（目录、构建、主题、文档）？
**答**：
- 目录：`packages/core`（无样式逻辑组件）、`packages/theme`（tokens + CSS 变量）、`packages/icons`、`docs`（Storybook/Dumi）；monorepo + changesets 版本管理。
- 构建：vite lib mode 出 ESM + d.ts，按入口分包支持 tree-shaking；样式与 JS 分离，按需引入靠 `export path`。
- 主题：三层 tokens（基础色板 -> 语义变量 -> 组件变量），运行时换肤切 CSS 变量（见 R19-154），支持 CSS-in-JS 局部覆盖。
- 文档与质量：Storybook 写 story + 交互文档；测试 RTL 单测 + 视觉回归（Storybook test-runner + 截图对比）；发布前 size-limit 体积门禁。

```javascript
// component-library 架构要点代码
// ---- 1. 目录结构 ----
// acme-ui/
//   packages/
//     core/src/
//       button/
//         Button.tsx        # 组件实现
//         button.css        # 样式（只消费主题变量）
//         Button.test.tsx
//         index.ts          # export { Button } from './Button';
//       index.ts            # 全量出口 + 子路径入口
//     theme/src/
//       tokens.css          # 基础色板 -> 语义变量 -> 组件变量
//   docs/                   # Storybook
//   package.json (root)     # changesets + turbo

// ---- 2. 组件实现规范 ----
// packages/core/src/button/Button.tsx
import { forwardRef } from 'react';

export type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: 'primary' | 'ghost';
  size?: 'sm' | 'md';
};

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', className, ...rest }, ref) => (
    <button
      ref={ref}
      // BEM + CSS 变量：组件样式只引用主题层 tokens，不写死颜色
      className={`acme-btn acme-btn--${variant} acme-btn--${size} ${className ?? ''}`}
      {...rest}
    />
  ),
);
Button.displayName = 'Button';

// ---- 3. theme/tokens.css 三层变量 ----
// :root {
//   --acme-blue-500: #2563eb;            /* 基础色板 */
//   --acme-color-primary: var(--acme-blue-500);  /* 语义层 */
//   --acme-btn-height-md: 36px;          /* 组件层 */
// }
// [data-theme="dark"] { --acme-color-primary: #60a5fa; }

// ---- 4. package.json 分包入口（按需引入的关键）----
// {
//   "name": "@acme/ui",
//   "exports": {
//     ".": "./dist/index.js",
//     "./button": "./dist/button/index.js",
//     "./styles.css": "./dist/theme/tokens.css"
//   },
//   "sideEffects": ["**/*.css"]          // CSS 不参与 tree-shaking
// }

// ---- 5. vite.config.ts lib 构建 ----
// export default defineConfig({
//   build: { lib: { entry: 'src/index.ts', formats: ['es'] }, rollupOptions: { external: ['react'] } }
// });

// ---- 6. 发布流水线 ----
// npx changeset            # 记录变更意图
// changeset version        # 合并后升版本写 CHANGELOG
// changeset publish        # 发 npm + GitHub tag
// size-limit 检查 dist 体积超阈值阻断合并
```
