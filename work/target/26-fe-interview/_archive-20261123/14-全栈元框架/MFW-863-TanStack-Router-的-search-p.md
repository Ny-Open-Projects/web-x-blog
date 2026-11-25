---
title: [MFW-863] TanStack Router 的 search param validator 在什么时候做运行时校验
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-863：TanStack Router 的 search param validator 在什么时候做运行时校验

**答**：
- 结论：validator 在路由匹配/导航时运行，把 URL 字符串解析为强类型对象；非法值走降级或重定向，保证 loader 拿到可信参数。
- 落地：用 zod/valibot 定义 schema，validateSearch 在导航前校验，失败归一化到默认值而非抛错中断导航。
- 追问钩子：为什么不能信任 URL 参数？——用户可手改 URL，类型系统只管编译期，运行时必须校验。

```javascript
import { z } from 'zod';
const SearchSchema = z.object({
  page: z.coerce.number().int().positive().catch(1),
  tab: z.enum(['info', 'comments']).catch('info')
});
export const Route = createFileRoute('/posts')({
  validateSearch: (search) => SearchSchema.parse(search), // 导航时校验
  loader: async ({ search }) => {
    // search 已是 { page:number, tab:'info'|'comments' } 强类型
    return db.posts.list({ page: search.page, tab: search.tab });
  }
});
// /posts?page=abc&tab=x → { page:1, tab:'info' }（降级），不中断导航
```
