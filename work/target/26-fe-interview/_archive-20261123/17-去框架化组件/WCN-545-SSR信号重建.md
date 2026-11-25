---
title: [WCN-545] SSR 水合时的「信号重建」：服务端 computed 结果如何传递给客户端而不重复计算？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-545：SSR 水合时的「信号重建」：服务端 computed 结果如何传递给客户端而不重复计算？

**答**：
- 结论：服务端把 computed 结果序列化进 HTML（如 <script type="application/json">），客户端用它作为 computed 的初始缓存。
- 客户端重建 computed 时，若依赖未变则直接用注入值（带依赖版本号校验），跳过首次重算。
- 版本号 = 依赖信号的当前值摘要；不一致说明数据过期，强制重算。
- 追问：注入数据太大怎么办？（答：只注入首屏可见的 computed，其余客户端惰性算）

```javascript
// 服务端注入：<script id="__SIG__" type="application/json">{"total":{v:300,deps:[100,3]}}</script>
function hydrateSignal(name, factory, injected) {
  const c = factory();
  const cached = injected[name];
  if (cached && signature(c.deps) === cached.deps) {
    c.setCache(cached.v);                        // 跳过首次重算
  }
  return c;
}
function signature(deps) { return deps.join(':'); }
```
