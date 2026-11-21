---
title: [WCN-153] WCN 与 React Server Components 的关系：边界在哪、如何互补？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-153：WCN 与 React Server Components 的关系：边界在哪、如何互补？

**答**：
- RSC 解决"服务端组件零 JS 下发"（数据获取与静态渲染留在服务器），但产物是 React 专属；WCN 解决"组件跨技术栈消费"。两者方向不同：RSC 是执行位置优化，WCN 是消费端标准化。
- 互补组合：RSC 页面里渲染 WCN——服务端输出 DSD 标记（零客户端 React 成本的部分），客户端交互 islands 用 WC define；RSC 负责"整页骨架与数据"，WC 负责"可移植部件"。
- 边界注意：RSC 不能给 WC 传函数 props（服务端无闭包下发）——交互必须走事件 + 客户端包装层；context 不能穿透到 WC（影子树 + 服务端边界），依赖要显式注入。
- 序列化规则：RSC payload 中的 WC 以 JSX 标签输出，attribute 走字符串；复杂数据用 RSC 的序列化通道（脱敏后）转 property。
- 选型判断：全 React 旗舰应用 → RSC 为主、WC 只用于必须跨栈的部件；多栈平台 → WC 为主、RSC 只在一个栈内用。

```jsx
// RSC 中使用 WCN（Next.js App Router）
export default async function Page() {
  const data = await getSummary();            // 服务端数据获取
  return (
    <>
      <ServerChart data={data} />               {/* RSC：零客户端 JS */}
      <x-filter-panel region="cn" />            {/* WCN：DSD + 客户端 define */}
    </>
  );
}
// 注意：x-filter-panel 若要接收对象 → 由客户端 wrapper 组件桥接（'use client'）
```
