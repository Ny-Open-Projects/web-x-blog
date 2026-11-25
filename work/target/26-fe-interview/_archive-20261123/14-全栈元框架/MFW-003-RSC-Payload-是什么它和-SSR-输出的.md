---
title: [MFW-003] RSC Payload 是什么？SSR 和 RSC 各自输出什么？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-003：RSC Payload 是什么？SSR 和 RSC 各自输出什么？
**答**：
- 一次 Next.js 页面请求，服务端输出两种东西：**SSR 输出 HTML**（给浏览器直接显示首屏）+ **RSC Payload**（一种类 JSX 的序列化格式，嵌在 script 标签里，给 React 运行时重建组件树）。
- RSC Payload 里 Server Component 是「已经算好的结果」（文本/元素描述），Client Component 只是一个**引用**（模块 id + props），客户端拿到引用后再执行真正的组件代码。
- 客户端导航（跳转另一页）时不再请求完整 HTML，而是**只拉新页面的 RSC Payload**，React 在内存里 patch 进当前树——这就是 App Router 导航快的原因。
- 追问钩子：`<Suspense>` 流式响应时，Payload 与 HTML 分段交替下发（HTML 先占位，Payload 到达后替换）。

```jsx
// 服务端组件树
async function Page() {
  const user = await getUser();
  return <ClientGreeting name={user.name} />; // Client Component
}
```

```html
<!-- 服务端返回（示意，有简化） -->
<div>你好，王同学</div>
<script>self.__next_f.push([1, "1:{\"name\":\"王同学\",\"children\":[\"$L2\"]}"])</script>
<script>self.__next_f.push([1, "2:I[\"app/client-greeting\",[\"app/client-greeting\"],\"default\"]"])</script>
<!-- $L2 是对 Client Component 模块的引用：客户端根据模块 id 动态加载并执行它 -->
```

```jsx
// 客户端导航时：Router 只请求 RSC Payload，不解析 HTML
// next/link 点击 -> fetch(target, { RSC: 1 }) -> React patch
router.push('/detail'); // 响应体是 Payload 流，而非 text/html
```
