---
title: [NODE-056] 模板渲染与 React SSR 的流式输出有何区别？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-056：模板渲染与 React SSR 的流式输出有何区别？
**答**：
- 模板引擎流式：按模板片段顺序拼接字符串（`res.write` 一段段写），逻辑简单但**无法根据后段数据修改前段**（已写出去的 HTML 收不回来），适合顺序文档。
- React 18 流式：基于 **Suspense 边界**拆分——骨架（shell）先发，`<Suspense fallback>` 包裹的慢数据块后到再**用内联 script 补齐 DOM 并完成 hydrate**，支持"后发先至"（先到的数据块不必等后到）。
- 共同约束：流式开始后不能改 status/headers；错误只能通过边界降级；SEO 爬虫若不执行 JS 需要等待 `onAllReady` 全量输出。

```javascript
import { renderToPipeableStream } from 'react-dom/server';
import { Suspense } from 'react';

function Page() {
  return (
    <html>
      <body>
        <Header />                                       {/* 立即可渲染 */}
        <Suspense fallback={<Skeleton rows={5} />}>      {/* 慢数据块：先发骨架 */}
          <Reviews />                                    {/* 内部 await 慢接口 */}
        </Suspense>
        <Suspense fallback={<AdPlaceholder />}>
          <Ads />                                        {/* 另一个独立流块：后发先至 */}
        </Suspense>
      </body>
    </html>
  );
}

app.get('/', (req, res) => {
  const stream = renderToPipeableStream(<Page />, {
    onShellReady() {
      res.setHeader('content-type', 'text/html; charset=utf-8');
      stream.pipe(res);   // shell 立即发送；Reviews/Ads 完成后 React 自动补发对应片段
    },
    onError(err) { console.error('流式中出错，该 Suspense 块降级:', err.message); },
  });
});

// 模板引擎对比（EJS）：只能按顺序 write，前段无法等待后段数据
// res.write(render(headerTpl));
// const reviews = await getReviews();      // 必须等：阻塞了后面所有片段
// res.write(render(reviewTpl, { reviews }));
// res.end(render(footerTpl));
```
