---
title: [MFW-686] Client Component 拆分：最小 client 边界
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-686：最小 Client 边界

**答**:
- client 边界的最小化原则：'use client' 的边界 = 「叶子交互组件」（Button/Input 下沉到叶子——父级保持 server）；「整页 'use client'」的反模式（父级 client = 子树全 client——RSC 的流式/缓存/SEO 优势全丢）；「拆分的杠杆」：把 'use client' 从页面级下移到叶子级（页面保持 server——交互部分 client 化）。
- 拆分的收益：client bundle 只含交互叶子（体积小）；server 树保留（数据获取/SEO/流式）——「client 叶子 = server 树的交互节点」。
- 拆分的模式：1) **props 传递**（server 父级传数据给 client 叶子——props 序列化 RBL-502）；2) **children 模式**（server 父级传 children 给 client 壳（Modal/Dropdown——壳 client、内容 server 渲染的 children——最佳实践：children 作为 server 数据的通道）；3) context 的传递（server → client 的 context 边界（context provider 必须 client——provider 包 server children：children 模式绕过）。
- 追问钩子：为什么「children 模式」是 client 拆分的黄金模式？——client 壳（Modal 的开关逻辑）+ server children（modal 内容的 server 渲染——RSC 数据流）：`<Modal>{<ServerContent />}</Modal>`——children 从 server 传入（client 壳只管打开关闭——内容不用 client 化）；「client 壳包 server 内容」= 最小 client 边界的典型模式：交互逻辑 client 化、内容渲染 server 化。

```tsx
// 反模式：整页 client
// app/page.tsx: 'use client' ← 整页 client（RSC 优势全丢）
// 修正：拆分到叶子
// app/page.tsx（server）
export default async function Page() {
  const data = await getData();
  return (
    <div>
      <h1>{data.title}</h1>                                {/* server：SEO/流式 */}
      <Counter />                                          {/* client 叶子：交互 */}
    </div>
  );
}
// components/Counter.tsx ('use client')
export function Counter() { const [n, setN] = useState(0); ... }
// children 模式：client 壳 + server 内容
// components/Modal.tsx ('use client')
export function Modal({ children }: { children: ReactNode }) {  // children 是 server 渲染的
  const [open, setOpen] = useState(false);
  return <>{open && <div className="modal">{children}</div>}
    <button onClick={() => setOpen(!open)}>Toggle</button></>;
}
// server 页面
<Modal><ServerData id={1} /></Modal>                     {/* children 是 server 组件 */}
```
