---
title: [CSS-058] CSS-in-JS 的原理与优缺点？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-058：CSS-in-JS 的原理与优缺点？

**答**：
- 运行时方案（styled-components/emotion）在 JS 里写样式，运行时生成唯一类名并注入 `<style>` 标签。
- 优点：天然组件作用域、可读 props/主题做动态样式、无全局冲突。
- 缺点：运行时开销（解析与序列化）、SSR 需要样式提取、包体积、与 React Server Components 存在兼容问题。
- 趋势：编译时方案（vanilla-extract、linaria、panda-css）在构建期产出静态 CSS，规避运行时成本。

```javascript
// styled-components：运行时方案
import styled from 'styled-components';

const Button = styled.button`
  background: ${(p) => (p.$variant === 'danger' ? '#f56c6c' : '#409eff')};
  color: #fff;
  padding: 8px 16px;
`;

export default () => <Button $variant="danger">删除</Button>;
```

```typescript
// vanilla-extract：编译时方案，构建期产出 .css 文件
import { style } from '@vanilla-extract/css';

export const button = style({
  padding: '8px 16px',
  selectors: {
    '&[data-variant="danger"]': { background: '#f56c6c' },
  },
});
```
