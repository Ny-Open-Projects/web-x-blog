---
title: [MFW-541] 元框架升级 codemod：Pages → App Router 迁移的自动化边界
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-541：Pages → App Router 迁移 codemod 的自动化边界

**答**:
- 可自动化的部分：1) **文件映射**（pages/a/b.tsx → app/a/b/page.tsx；getStaticProps → 静态组件 + generateStaticParams；getServerSideProps → async server component——结构级转换）；2) API 调用机械替换（next/router → next/navigation）；3) data fetching 模式（getInitialProps → RSC loader 形态）。
- 不可自动化的部分（人工清单 RBL-666 哲学）：1) **_app/_document 全局状态**（Provider 迁移到 root layout——状态管理方案依赖）；2) 数据获取语义差异（getServerSideProps 的「每请求重取」→ RSC 缓存语义变化——行为等价需人工决策缓存策略）；3) HOC 模式（withAuth 包页面 → App Router 的 layout/middleware 分发）。
- codemod 的验证基建：迁移前后「语义 diff」（双渲染对比 RBL-540 + 快照测试）——codemod 只保证「结构迁移」，行为等价靠验证闸门。
- 渐进迁移策略：Pages 与 App Router 共存（Next 支持——子目录逐步迁移）；「共存期的路由冲突」（同 URL 两套——编译器检测告警）。
- 追问钩子：为什么「getServerSideProps → RSC」的语义等价不能自动判定？——getServerSideProps 是「显式的每请求数据获取」（强制动态）；RSC 内 fetch 默认有缓存语义（force-cache/revalidate）——同一代码两种缓存行为（结果不同 = 语义漂移）；迁移器无法推断「原意图是缓存还是实时」——意图不可推断的部分必须人工标注（缓存策略清单化迁移：每页声明预期缓存语义，迁移器校验）。

```javascript
// codemod 结构级转换示例（jscodeshift）
// pages/products/[id].tsx → app/products/[id]/page.tsx
export async function getStaticProps({ params }) {       // 转换前
  return { props: { product: await getProduct(params.id) }, revalidate: 60 };
}
// 转换后（App Router）
export const revalidate = 60;                            // revalidate 提升
export default async function Page({ params }) {
  const product = await getProduct(params.id);           // fetch 走 Data Cache
  return <ProductView product={product} />;
}
// 人工清单生成
const MANUAL_STEPS = [
  { pattern: /_app\./, step: 'Provider 状态迁移到 app/layout.tsx——人工评估状态方案' },
  { pattern: /getServerSideProps/, step: '确认缓存语义：原为每请求实时 → RSC 需 cache: no-store 或接受缓存' },
  { pattern: /with[A-Z]\w+\(/, step: 'HOC 页面包装 → layout/middleware 重组' },
];
```
