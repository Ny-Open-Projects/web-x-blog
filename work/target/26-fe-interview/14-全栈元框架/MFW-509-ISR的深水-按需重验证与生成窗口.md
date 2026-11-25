---
title: [MFW-509] ISR 深水：按需重验证（On-Demand ISR）与生成窗口控制
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-509：ISR 深水：按需重验证与生成窗口控制

**答**:
- On-Demand ISR：后台事件（CMS 发布/商品改价）主动触发 `res.revalidate('/path')` 或 revalidateTag——比时间窗（revalidate: 60）精确：数据变更即失效，而非等 TTL。
- 生成窗口的风险：**缓存击穿**（过期瞬间 1000 并发请求同时触发重生成——旧值还在但都在等新生成：Next 内部单飞，但「首请求等待新生成」延迟可达秒级）；缓解：stale-while-revalidate 语义（立即返回旧值 + 后台生成）、预热（发布后主动打一遍 URL）。
- ISR 与动态内容的边界：cookie/headers 依赖 → 动态渲染（退出 ISR）；「页面 90% 静态 + 10% 用户态」→ 静态壳 + client fetch 用户态（RSC 的 Suspense 流式版：外壳静态化 + 个人数据流式）。
- 大规模 ISR 的清单管理：百万级 URL 的 on-demand 触发要「增量队列」（CMS webhook → 队列 → 逐个 revalidate + 速率限制——避免重生成风暴打满服务器）。
- 追问钩子：为什么 ISR 的 stale-while-revalidate 语义在电商场景必须谨慎？——价格/库存的旧值直接展示 = 法律与客诉风险（标旧价格下单失败）；高敏感字段用「精确失效」（on-demand）而非「时间窗容忍」——缓存策略与业务风险的映射：时效容忍度决定 TTL vs 事件驱动的选择（与 RBL-618 缓存角色分类同构）。

```javascript
// On-Demand ISR 的队列化
import { revalidatePath, revalidateTag } from 'next/cache';
// CMS webhook -> 队列 worker
const queue = createScheduler({ concurrency: 5 });       // 限速：防重生成风暴
queue.schedule(async () => {
  for (const path of changedPaths) {
    revalidatePath(path);                                // 单飞在框架内，返回旧值
  }
  revalidateTag('products');                             // 数据层联动
}, 1);
// 敏感字段的精确失效 vs 容忍
const product = {
  name: { source: 'cms', revalidate: 3600 },             // 名称可容忍 1h
  price: { source: 'pricing-db', revalidate: 0 },        // 价格精确失效（on-demand）
  stock: { source: 'inventory', dynamic: true },         // 库存必须实时
};
```
