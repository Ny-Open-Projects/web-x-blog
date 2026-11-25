---
title: [TST-250] 组件库如何验证 SSR（Next/自建 SSR）兼容性？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-250：组件库如何验证 SSR（Next/自建 SSR）兼容性？
**答**：
- SSR 渲染冒烟：renderToString 不抛错且输出含关键结构（防访问 window/document）。
- 水合一致性：服务端 HTML 与客户端首帧 DOM 关键节点一致（hydration mismatch 检测）。
- 生命周期守卫：useEffect 内逻辑在服务端不执行的断言（用 mock 监测调用）。
- 组件库提供 SSR-safe 的环境访问封装（safeWindow），测试验证封装路径。

```javascript
import { renderToString } from 'react-dom/server';
test('SSR 冒烟', () => {
  const html = renderToString(<DatePicker defaultValue="2026-01-01" />);
  expect(html).toContain('2026-01');            // 关键结构在首屏 HTML
});
r
```
