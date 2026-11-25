---
title: [MFW-522] Partial Prerendering：静态壳与动态洞的编译期切分
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-522：Partial Prerendering：静态壳与动态洞

**答**:
- PPR 的编译期切分：渲染一次，遇到动态 API（cookies/headers/未缓存 fetch）的「洞」被截断为 Suspense 边界——静态部分构建期预渲染成 HTML+payload，动态洞运行时流式填充；「切分点 = 动态 API 访问点」。
- 切分的实现原理：编译器把组件树按「动态访问」二分——静态子树进 shell（instant，CDN 缓存）；动态子树包进 Suspense（隐式，编译器自动插入）——「每个动态洞 = 一个 Suspense 边界」。
- 与纯静态/纯动态的对比：纯静态（构建期全部）× 纯动态（每请求全量）→ PPR = 静壳 TTFB + 动态内容的个性化——「粒度从路由级到边界级」（RBL-510 粒度演进）。
- 工程约束：动态洞内不能触发「整树动态」（洞内 fetch 必须显式缓存策略）；洞的粒度影响流式成本（洞越小 patch 越多——网络开销 vs 个性化粒度）。
- 追问钩子：为什么 PPR 需要「编译器切分」而不是「开发者手写 Suspense」？——手写 Suspense 的语义是「异步显示占位」（运行时），PPR 需要的是「静态/动态的编译期二分」（切分点决定缓存键）——同一语法两种语义，编译器必须区分「这个 Suspense 是流式占位还是动态洞标记」；experimental_ppr 标志 + 动态 API 检测的自动切分让「意图与机制解耦」——开发者表达意图，编译器决定机制。

```javascript
// PPR 页面
export const experimental_ppr = true;
export default async function Page({ params }) {
  return (
    <>
      <Header />                                         {/* 静态：构建期 */}
      <Suspense>                                          {/* 编译器标记：动态洞 */}
        <UserAvatar />                                    {/* 内部读 cookies → 洞 */}
      </Suspense>
      <Suspense fallback={<ListSkeleton />}>
        <ProductList params={params} />                   {/* 动态 fetch → 洞 */}
      </Suspense>
      <Footer />                                           {/* 静态 */}
    </>
  );
}
// 构建产物：静态壳（Header+Footer+fallbacks）CDN 缓存
// 请求时：静态壳立即返回（instant TTFB）→ 动态洞流式补齐
```
